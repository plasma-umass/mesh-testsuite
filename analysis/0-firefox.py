#!/usr/bin/env python3

import argparse
import sys
import os
import csv
import numpy

from os import path
from collections import defaultdict


BASE_DIR = 'results/0-firefox'
MEMORY_DIR = path.join(BASE_DIR, 'memory')
SPEED_DIR = path.join(BASE_DIR, 'speed')


def slurp(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()


TEST_END = float(slurp('firefox-wait-seconds').strip()) # seconds


def collect_memory():
    allocators = defaultdict(list)

    for filename in os.listdir(MEMORY_DIR):
        filepath = path.join(MEMORY_DIR, filename)
        if path.islink(filepath):
            continue
        # mstat recursively records stuff including short lived subprocesses
        if path.getsize(filepath) < 10000:
            continue

        heap_usage_mb = []
        with open(filepath) as log_file:
            reader = csv.DictReader(log_file, dialect=csv.excel_tab)
            for row in reader:
                time_ns = int(row['time'])
                time_s = time_ns / 1e9
                heap = int(row['rss']) + int(row['kernel'])
                heap_mb = heap/1024.0/1024.0
                heap_usage_mb.append(heap_mb)
                # normalize the lengths of the test
                if time_s >= TEST_END:
                    break

        usage = numpy.array(heap_usage_mb)
        average = numpy.mean(usage)

        allocator = filename.split('.')[1]
        allocators[allocator].append(average)

    base_mean = None
    with open(path.join(BASE_DIR, 'memory.absolute.tsv'), 'w') as results:
        results.write('allocator\tmean\tmedian\tstddev\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            median = numpy.median(usage)
            stddev = numpy.std(usage)

            if allocator == 'jemalloc':
                base_mean = mean

            results.write('%s\t%.1f\t%.1f\t%.1f\n' % (allocator, mean, median, stddev))

    with open(path.join(BASE_DIR, 'memory.relative.tsv'), 'w') as results:
        results.write('allocator\trelative_heap\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            relative = mean / base_mean

            results.write('%s\t%.3f\n' % (allocator, relative))


def collect_speed():
    allocators = defaultdict(list)

    firefox_speed_data = slurp(path.join(SPEED_DIR, 'results.tsv')).splitlines()
    # for every file in results/3-ruby/speed
    # collect allocator stats
    for line in firefox_speed_data:
        parts = line.split('\t')
        allocator = parts[0]
        score = float(parts[1])

        allocators[allocator].append(score)

    base_mean = None
    with open(path.join(BASE_DIR, 'speed.absolute.tsv'), 'w') as results:
        results.write('allocator\tmean_score\tmedian_score\tstddev\n')
        for allocator, scores in allocators.items():
            usage = numpy.array(scores)
            mean = numpy.mean(usage)
            median = numpy.median(usage)
            stddev = numpy.std(usage)

            if allocator == 'jemalloc':
                base_mean = mean

            results.write('%s\t%.3f\t%.3f\t%.3f\n' % (allocator, mean, median, stddev))

    with open(path.join(BASE_DIR, 'speed.relative.tsv'), 'w') as results:
        results.write('allocator\trelative_speedometer_score\n')
        for allocator, stats in allocators.items():
            usage = numpy.array(stats)
            mean = numpy.mean(usage)
            relative = mean / base_mean

            results.write('%s\t%.3f\n' % (allocator, relative))


def main():
    collect_memory()
    collect_speed()


if __name__ == '__main__':
    import sys
    sys.exit(main())
