#!/usr/bin/env python3

import argparse
import sys
import os
import csv
import numpy

from os import path
from collections import defaultdict


BASE_DIR = 'results/1-redis'
MEMORY_DIR = path.join(BASE_DIR, 'memory')
SPEED_DIR = path.join(BASE_DIR, 'speed')

TEST_END = 7.5 # seconds


def slurp(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()


def collect_memory():
    allocators = defaultdict(list)

    # for every file in results/1-redis/memory (that isn't symlink)
    # find heap size at 7.5 seconds
    for filename in os.listdir(MEMORY_DIR):
        filepath = path.join(MEMORY_DIR, filename)
        if path.islink(filepath):
            continue

        heap_at_test_end_mb = None
        with open(filepath) as log_file:
            reader = csv.DictReader(log_file, dialect=csv.excel_tab)
            for row in reader:
                time_ns = int(row['time'])
                time_s = time_ns / 1e9
                if time_s >= TEST_END:
                    heap = int(row['rss']) + int(row['kernel'])
                    heap_mb = heap/1024.0/1024.0
                    heap_at_test_end_mb = heap_mb
                    break

        assert heap_at_test_end_mb is not None

        allocator = filename.split('.')[0]
        allocators[allocator].append(heap_at_test_end_mb)

    base_mean = None
    with open(path.join(BASE_DIR, 'memory.absolute.tsv'), 'w') as results:
        results.write('allocator\tmean\tmedian\tstddev\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            median = numpy.median(usage)
            stddev = numpy.std(usage)

            if allocator == 'mesh0n':
                base_mean = mean

            results.write('%s\t%s\t%s\t%s\n' % (allocator, mean, median, stddev))

    with open(path.join(BASE_DIR, 'memory.relative.tsv'), 'w') as results:
        results.write('allocator\trelative_heap\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            relative = mean / base_mean

            results.write('%s\t%s\n' % (allocator, relative))


def collect_speed():
    allocators = defaultdict(list)

    # for every file in results/1-redis/speed
    # collect allocator stats
    for filename in os.listdir(SPEED_DIR):
        filepath = path.join(SPEED_DIR, filename)

        heap_at_test_end_mb = None
        with open(filepath) as log_file:
            reader = csv.DictReader(log_file, dialect=csv.excel_tab)
            for row in reader:
                allocator = row['config']
                time_s = float(row['seconds'])
                allocators[allocator].append(time_s)

    base_mean = None
    with open(path.join(BASE_DIR, 'speed.absolute.tsv'), 'w') as results:
        results.write('allocator\tmean\tmedian\tstddev\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            median = numpy.median(usage)
            stddev = numpy.std(usage)

            if allocator == 'jemalloc':
                base_mean = mean

            results.write('%s\t%s\t%s\t%s\n' % (allocator, mean, median, stddev))

    with open(path.join(BASE_DIR, 'speed.relative.tsv'), 'w') as results:
        results.write('allocator\ttime_seconds\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            relative = mean / base_mean

            results.write('%s\t%s\n' % (allocator, relative))


def main():
    collect_memory()
    collect_speed()


if __name__ == '__main__':
    import sys
    sys.exit(main())
