import docker as docker
import logging
import random

logging.basicConfig(level="DEBUG")

client = docker.client.from_env()
image_name = "test-image-{}".format(random.randint(1, 10000))
image, _ = client.images.build(path="context", dockerfile="Dockerfile.builder", tag=image_name, platform="linux/amd64", nocache=True)
print(image)
