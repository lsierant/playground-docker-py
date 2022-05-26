import docker as docker
import logging
import random
import sys

dockerfile = sys.argv[1]
logging.basicConfig(level="DEBUG")
client = docker.client.from_env()
image_name = "test-image-{}".format(random.randint(1, 10000))
print(f"Building image {image_name}")
_, _ = client.images.build(path="context", dockerfile=dockerfile, tag=image_name, platform="linux/amd64", nocache=True)
