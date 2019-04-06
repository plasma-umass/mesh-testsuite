# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:mesh-base .

FROM bpowers/mesh:git-0ab3a2e343db105d5310bbbdbcb761b1d6df8631 as mesh
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat
FROM bpowers/mstatgcc:git-5e94c47aba5edabc23e741e394a3b568881a3370 as mstatgcc

FROM bpowers/spec:v2
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ mesh"

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mstatgcc /usr/local/bin/mstatgcc /usr/local/bin/mstatgcc
COPY --from=mstatgcc /usr/local/bin/mstatgcc /usr/local/bin/mstatg++
# copy mesh with full randomization as `libmesh.so`
COPY --from=mesh /usr/local/lib/libmesh2y.so /usr/local/lib/libmesh.so
RUN ldconfig

COPY ./Linux-mesh-mstat.cfg /spec/config/

WORKDIR /spec

RUN . ./shrc \
  && runspec --config=Linux-mesh-mstat.cfg --action=build --tune=base int
