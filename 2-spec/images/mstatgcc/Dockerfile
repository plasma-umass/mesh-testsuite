# docker build -t bpowers/mstatgcc .
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

WORKDIR /src

COPY . .

RUN make \
 && sudo make install


FROM ubuntu:18.04

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=builder /usr/local/bin/mstat* /usr/local/bin/
