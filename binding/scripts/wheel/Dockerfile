# Use a base image that includes Python and pip
FROM python:3.8-slim

# Install system dependencies and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    libopencv-dev \
    libglm-dev \
    fuse \
    libfuse2 \
    ocl-icd-opencl-dev \
    libassimp-dev \
    libgsl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pybind11 and other Python packages
RUN pip3 install pybind11 setuptools wheel

# Copy your package's source code into the Docker container
COPY . /io

# Set the working directory
WORKDIR /io

# Install your package
RUN python3 setup.py sdist bdist_wheel

# RUN touch dist/toto
# RUN echo `pwd`
RUN ls dist/.

# Copy the wheel to the host machine
# COPY dist /dist
COPY dist/pyhighmap-0.0.0-cp38-cp38-linux_x86_64.whl /.

