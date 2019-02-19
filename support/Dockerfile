# To build use:
# docker build -t bpowers/mesh-artifact-support .
FROM ubuntu:18.04
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="Ubuntu Dev"

ENV DEBIAN_FRONTEND noninteractive

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
  make \
  gdb \
  lcov \
  gfortran \
  r-base \
  python-pygments \
  python3 \
  tzdata \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8 \
 && rm -rf /usr/local/lib/python3.6

COPY install-packages.r /tmp/install-packages.r

RUN R --vanilla --silent --no-readline </tmp/install-packages.r

RUN apt-get update && apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg2 \
  software-properties-common \
 && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey \
 && add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable" \
 && apt-get update \
 && apt-get -y install docker-ce \
 && rm -rf /var/lib/apt/lists/*
