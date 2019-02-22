# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:mesh0n .
FROM bpowers/mesh:git-b32b9029e84ced9e15d8271d85dfb8648f26a5b7 as mesh

FROM bpowers/mesh-artifact-2-spec:mesh-base
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ mesh"

COPY --from=mesh /usr/local/lib/libmesh0n.so /usr/local/lib/libmesh.so
