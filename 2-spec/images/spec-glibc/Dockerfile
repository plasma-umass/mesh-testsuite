# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:glibc .
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat
FROM bpowers/mstatgcc:git-5e94c47aba5edabc23e741e394a3b568881a3370 as mstatgcc

FROM bpowers/spec:v2
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ glibc"

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mstatgcc /usr/local/bin/mstatgcc /usr/local/bin/mstatgcc
COPY --from=mstatgcc /usr/local/bin/mstatgcc /usr/local/bin/mstatg++

COPY ./Linux-glibc-mstat.cfg /spec/config/

WORKDIR /spec

RUN . ./shrc \
  && runspec --config=Linux-glibc-mstat.cfg --action=build --tune=base int
