# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:jemalloc .
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat
FROM bpowers/mstatgcc:git-5e94c47aba5edabc23e741e394a3b568881a3370 as mstatgcc

FROM bpowers/spec:v2
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ jemalloc"

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mstatgcc /usr/local/bin/mstatgcc /usr/local/bin/mstatgcc
COPY --from=mstatgcc /usr/local/bin/mstatgcc /usr/local/bin/mstatg++

COPY ./Linux-jemalloc-mstat.cfg /spec/config/

RUN apt-get update && apt-get install -y \
  libjemalloc-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /spec

RUN . ./shrc \
  && runspec --config=Linux-jemalloc-mstat.cfg --action=build --tune=base int
