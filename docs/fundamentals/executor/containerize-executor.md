# Dockerize your Executor

Once you have understood what an `Executor` is and how it can be used inside a `Flow`, you may be interested in wrapping this Executor into a container
so that you can isolate its dependencies and make it ready to run in the cloud or in Kubernetes.

One option is to leverage {ref}`Jina Hub <hub/index>` infrastructure to make sure your Executor can run as a container.

However, you can also build a Docker image yourself and use it like any other Executor. There are some requirements
on how this image needs to be built, the main ones being:

- Jina must be installed inside the image
- The Jina CLI command to start the Executor has to be the default entrypoint

## Prerequisites

To understand how a container image for an Executor is built, you need a basic understanding of [Docker](https://docs.docker.com/), both of how to write 
a [Dockerfile](https://docs.docker.com/engine/reference/builder/), and how to build a Docker image.

To reproduce the example below it is required to have Docker installed locally.


## Install Jina in the Docker image

Jina **must** be installed inside the Docker image. This can be achieved in one of two ways:

- Use a [Jina based image](https://hub.docker.com/r/jinaai/jina) as the base image in your Dockerfile.
This will make sure that everything needed for Jina to run the Executor is installed.

```dockerfile
FROM jinaai/jina:3.0-py37-perf
```

- Install Jina like any other Python package. You can do this by specifying Jina in the `requirements.txt`, 
or by including the `pip install jina` command as part of the image building process.  

```dockerfile
RUN pip install jina==3.0
```

## Set Jina Executor CLI as entrypoint

When a containerized Executor is run inside a Flow,
under the hood Jina executes `docker run` with extra arguments.

This means that Jina assumes that whatever runs inside the container, also runs like it would in a regular OS process. Therefore, you need to make sure that
the basic entrypoint of the image calls `jina executor` {ref}`CLI <../api/cli>` command.

```dockerfile
ENTRYPOINT ["jina", "executor", "--uses", "PATH_TO_YOUR_EXECUTOR_CONFIGURATION"]
```

## Example: Dockerized Executor

Here we will show how to build a basic Executor with a dependency on another external package


### Write the Executor

You can define your soon-to-be-Dockerized Executor exactly like any other Executor.
We do this here in the `my_executor.py` file.

```python
import torch  # Our Executor has dependency on torch
from jina import Executor, requests


class ContainerizedEncoder(Executor):
    @requests
    def foo(self, docs, **kwargs):
        for doc in docs:
            doc.text = 'This Document is embedded by ContainerizedEncoder'
            doc.embedding = torch.randn(10)
```

### Write the Executor YAML file

The YAML configuration, as a minimal working example, is required to point to the file containing the Executor.


```{admonition} More YAML options
:class: seealso
To discover what else can be configured using Jina's YAML interface, see {ref}`here <executor-api>`.
```

This is necessary for the Executor to be put inside the Docker image,
and we can define such a configuration in `config.yml`:

```yaml
jtype: ContainerizedEncoder
metas:
  py_modules:
    - my_executor.py
```

### Write `requirements.txt`

In this case, our Executor has only one requirement besides Jina: `torch`.

In `requirements.txt`, we specify a single requirement:

```requirements.txt
torch
```

### Write the Dockerfile

The last step is to write a `Dockerfile`, which has to do little more than launching the Executor via the Jina CLI:

```dockerfile
FROM jinaai/jina:3.0-py37-perf

# make sure the files are copied into the image
COPY . /executor_root/

WORKDIR /executor_root

RUN pip install -r requirements.txt

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
```

### Build the image

At this point we have a folder structure that looks like this:

```
.
├── my_executor.py
└── requirements.txt
└── config.yml
└── Dockerfile
```

We just need to build the image:

```bash
docker build -t my_containerized_executor .
```

Once the build is successful, this is what you should see under `docker images`:

```console
REPOSITORY                       TAG                IMAGE ID       CREATED          SIZE
my_containerized_executor        latest             5cead0161cb5   13 seconds ago   2.21GB
```

### Use the containerized Executor

The containerized Executor can be used like any other, the only difference being the 'docker' prefix in the `uses`
 parameter:
```python
from docarray import DocumentArray, Document
from jina import Flow

f = Flow().add(uses='docker://my_containerized_executor')

with f:
    returned_docs = f.post(on='/', inputs=DocumentArray([Document()]))

for doc in returned_docs:
    print(f'Document returned with text: "{doc.text}"')
    print(f'Document embedding of shape {doc.embedding.shape}')
```

```console
Document returned with text: "This Document is embedded by ContainerizedEncoder"
Document embedding of shape torch.Size([10])
```

### Mount volumes

You can mount volumes into your dockerized Executor by passing a list of volumes to the `volumes` argument:

```python
f = Flow().add(
    uses='docker://my_containerized_executor',
    volumes=['host/path:/path/in/container', 'other/volume:/app'],
)
```

````{admonition} Hint
:class: hint
If you want your containerized Executor to operate inside one of these volumes, remember to set its {ref}`workspace <executor-workspace>` accordingly!
````

If you do not specify `volumes`, Jina will automatically mount a volume into the container.
In this case, the volume source will be your {ref}`default Executor workspace <executor-workspace>`, and the volume destination will
be `/app`. Additionally, automatic volume setting will try to move the Executor's workspace into the volume destination.
Depending on the default executor workspace on your system this may not always succeed, so explicitly mounting a volume and setting
a workspace is recommended.

You can disable automatic volume setting by passing `f.add(..., disable_auto_volume=True)`.