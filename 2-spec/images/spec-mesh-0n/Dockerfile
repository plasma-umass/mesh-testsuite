# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:mesh0n .
FROM bpowers/mesh:git-0ab3a2e343db105d5310bbbdbcb761b1d6df8631 as mesh

FROM bpowers/mesh-artifact-2-spec:mesh-base
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ mesh"

COPY --from=mesh /usr/local/lib/libmesh0n.so /usr/local/lib/libmesh.so
