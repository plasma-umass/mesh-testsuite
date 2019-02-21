# To build use:
# docker build -t bpowers/mesh-artifact-2-spec:mesh2y .
FROM bpowers/mesh:git-5408d826cdd59d5bd8778762bb963ec171264066 as mesh

FROM bpowers/mesh-artifact-2-spec:mesh-base
MAINTAINER Bobby Powers <bpowers@cs.umass.edu>

LABEL description="SPEC w/ mesh"

COPY --from=mesh /usr/local/lib/libmesh2y.so /usr/local/lib/libmesh.so
