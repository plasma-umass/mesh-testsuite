import collections

class Config:
    def __init__(self, name, docker_image, dir_name=None):
        self.name = name
        self.docker_image = docker_image
        if dir_name:
            self.dir_name = dir_name
        else:
            self.dir_name = name

configs = [
    Config('jemalloc', 'bpowers/mesh-artifact-2-spec:jemalloc'),
    Config('glibc', 'bpowers/mesh-artifact-2-spec:glibc'),
    Config('mesh', 'bpowers/mesh-artifact-2-spec:mesh0n', 'mesh-0n'),
    Config('mesh', 'bpowers/mesh-artifact-2-spec:mesh0y', 'mesh-0y'),
    Config('mesh', 'bpowers/mesh-artifact-2-spec:mesh1y', 'mesh-1y'),
    Config('mesh', 'bpowers/mesh-artifact-2-spec:mesh2y', 'mesh-2y'),
]
