# docker build -t bpowers/mesh-artifact-0-firefox .

FROM bpowers/mesh:git-0ab3a2e343db105d5310bbbdbcb761b1d6df8631 as mesh
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat
FROM bpowers/hoard:git-761c11f966d2891b1800844bffe10e176b66d04b as hoard


FROM bpowers/mesh-artifact-0-firefox-base:latest

RUN apt-get update && apt-get install -y \
  python2-dev \
  linux-tools-common \
  linux-tools-generic \
  gdb \
  strace \
  libgoogle-perftools-dev \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir /data

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
COPY --from=mesh /usr/local/lib/libmesh2y.so /usr/local/lib/libmesh.so
COPY --from=hoard /usr/local/lib/libhoard.so /usr/local/lib/

RUN ldconfig

WORKDIR /src

COPY . .

RUN cd /src/atsy/atsy \
 && ../env/bin/python setup.py develop

CMD [ "./entrypoint.sh" ]
