# docker build -t bpowers/mesh-artifact-1-redis .

FROM bpowers/mesh:git-b32b9029e84ced9e15d8271d85dfb8648f26a5b7 as mesh
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat

FROM ubuntu:18.04 as builder
MAINTAINER Bobby Powers <bobbypowers@gmail.com>

RUN apt-get update && apt-get install -y \
  build-essential \
  git \
  gcc-8 \
  g++-8 \
  python3 \
  sudo \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8 \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
 && rm -rf /usr/local/lib/python3.6

COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
RUN ldconfig

WORKDIR /src

COPY . .

RUN ./build


FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  python3 \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
 && rm -rf /usr/local/lib/python3.6 \
 && mkdir /data

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
RUN ldconfig

WORKDIR /src

COPY . .

COPY --from=builder /src/bin/* /src/bin/

CMD [ "./test", "--data-dir=/data/1-redis" ]
