# To build use:
# docker build -t bpowers/dev:v2 .
FROM ubuntu:18.04
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="Ubuntu Dev"

RUN apt-get update && apt-get install -y \
  build-essential \
  git \
  gcc \
  llvm \
  clang \
  cmake \
  gcc-8 \
  g++-8 \
  linux-tools-common \
  linux-tools-generic \
  libtool \
  libevent-dev \
  make \
  gdb \
  lcov \
  gfortran \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8 \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
 && rm -rf /usr/local/lib/python3.6
