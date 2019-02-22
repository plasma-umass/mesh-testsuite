# To build use:
# docker build -t bpowers/mesh-artifact-support .
FROM bpowers/dev:v3
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="Ubuntu Dev"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
  r-base \
  python-pygments \
  python3 \
  tzdata \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /usr/local/lib/python3.6

COPY install-packages.r /tmp/install-packages.r

RUN R --vanilla --silent --no-readline </tmp/install-packages.r
