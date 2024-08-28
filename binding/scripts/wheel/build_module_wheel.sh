#!/bin/sh
docker -D build -t manylinux_build .
# docker run --rm -v $(pwd)/dist:/dist manylinux_build
auditwheel show dist/pyhighmap-0.0.0-cp38-cp38-manylinux2014_x86_64.whl
