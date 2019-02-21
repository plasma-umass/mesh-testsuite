# docker build -t bpowers/mesh-artifact-0-firefox .

FROM bpowers/mesh:git-be630c4aeeef2103e4b6357550d02c3469a212df as mesh
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat


FROM bpowers/mesh-artifact-0-firefox-base:latest

RUN apt-get update && apt-get install -y \
  python2-dev \
  linux-tools-common \
  linux-tools-generic \
  gdb \
  strace \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir /data

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
# COPY --from=mesh /usr/local/lib/libmesh2y.so /usr/local/lib/libmesh.so

COPY libmesh.so /usr/local/lib/libmesh.so

RUN ldconfig

WORKDIR /src

COPY . .

RUN cd /src/atsy/atsy \
 && ../env/bin/python setup.py develop

CMD [ "./entrypoint.sh" ]
