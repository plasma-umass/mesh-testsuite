# docker build -t bpowers/mesh-artifact-3-ruby .

FROM bpowers/mesh:git-0ab3a2e343db105d5310bbbdbcb761b1d6df8631 as mesh
FROM bpowers/mstat:git-497eeeee07e6813ebc4d557d50ebe82bbfc05318 as mstat


FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  python3 \
  ruby \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
 && rm -rf /usr/local/lib/python3.6 \
 && mkdir /data

COPY --from=mstat /usr/local/bin/mstat /usr/local/bin/
COPY --from=mesh /usr/local/lib/libmesh* /usr/local/lib/
RUN ldconfig

WORKDIR /src

COPY . .

CMD [ "./test", "--data-dir=/data/3-ruby" ]
