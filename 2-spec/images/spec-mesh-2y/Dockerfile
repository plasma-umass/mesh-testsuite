# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:mesh2y .
FROM bpowers/mesh:git-be630c4aeeef2103e4b6357550d02c3469a212df as mesh

FROM bpowers/mesh-artifact-2-spec:mesh-base
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ mesh"

COPY --from=mesh /usr/local/lib/libmesh2y.so /usr/local/lib/libmesh.so
