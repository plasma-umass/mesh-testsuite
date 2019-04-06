import collections

# Config = collections.namedtuple('Config', ['name', 'use_flags', 'ldflags'])

class Config:
    def __init__(self, name, use_flags, ldflags=None, skip=False, defrag=False):
        self.name = name
        self.use_flags = use_flags
        self.ldflags = ldflags
        self.skip = skip
        self.defrag = defrag

configs = [
    Config('libc',          'USE_JEMALLOC=no'),
    Config('mesh0n',        'USE_JEMALLOC=no',          '-Wl,--no-as-needed -lmesh0n'),
    Config('mesh0y',        'USE_JEMALLOC=no',          '-Wl,--no-as-needed -lmesh0y'),
    Config('mesh1y',        'USE_JEMALLOC=no',          '-Wl,--no-as-needed -lmesh1y'),
    Config('mesh2y',        'USE_JEMALLOC=no',          '-Wl,--no-as-needed -lmesh2y'),
    Config('tcmalloc',      'USE_TCMALLOC_MINIMAL=yes'),
    Config('jemalloc',      'USE_JEMALLOC=yes',         defrag=True),
]
