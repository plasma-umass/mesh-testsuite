Mesh PLDI Artifact
==================

Getting Started Guide
---------------------

The provided Linux virtual machine (in VirtualBox VMDK format) has a
user named 'mesh' with the password 'mesh', and should be able to
`sudo` without needing to enter the password.  The VM is recommended
to be run with 4 GB of RAM and 2 processors allocated to it.

Upon launching the VM, you should be treated to a stock Ubuntu 18.10
Linux Desktop with an open terminal.  Run:

```sh
$ ./getting-started
```

To run through all of the tests with a reduced number of iterations
and, in the case of SPEC, a smaller dataset.

This script will take around half an hour (or maybe an hour) depending
on processor speed.  Please disable sleep and ensure you are plugged
into power before running, and if possible don't use the computer
while the test is running (try getting a coffee!).


Step-by-Step Instructions
-------------------------

There are 2 high-level steps for evaluating this artifact:

1. Running the benchmarks
2. Comparing the results to the claims in the paper

### Running the Benchmarks

```sh
$ ./run
```

Invoking the `run` script will kick off executing all benchmarks with
a larger number of iterations than run under "Getting Started" and
with reference workloads for SPEC.

This `run` script will also re-generate the figures used in the paper,
and parse the raw data (without deleting or modifying the raw data)
into tables that make evaluating our claims straightforward.


### Claims not supported by the artifact

At the end of Section 6.2.2 (Evaluation: Redis), we claim:

> During execution with Mesh, a total of 0.23s are spent meshing (the
> longest pause is 22 ms), while active defragmentation accounts for
> 1.49s (5.5× slower).

We believe this statement to be accurate, but were not able to
automate re-collection of this data into this artifact in the time
alloted.

### Common Problems

#### Firefox times out

Virtual machines are slow, and Firefox may not complete the
Speedometer test before the test suite grows impatient and moves on.
If this happens, edit `./firefox-wait-seconds` to be a larger integer
number of seconds and re-run `./run` or `./getting-started`.

When running the Redis tests under Docker on macOS, we have seen Mesh
take an order of magnitude longer under the `fragperf` test.  We
believe this to be some issue regarding nested virtualization and page
table modification (as Docker on macOS manages a Linux VM under the
covers to run containers in), but haven't been able to track it down.
Restarting either Docker or the machine resolves the issue in some
cases.

### Evaluating Paper Claims

#### 0. Firefox

> Reduces the memory consumption of Firefox by 16% compared to Firefox’s bundled jemalloc allocator.

> Mesh requires 530 MB (σ = 22.4 MB) to complete the benchmark, while the Mozilla allocator needs 632 MB (σ = 25.3 MB).

This artifact reproduces these results, which can be verified via the data in the generated files `results/0-firefox/memory.relative.tsv` and `results/0-firefox/speed.relative.tsv`.


#### 1. Redis

> Using Mesh automatically and portably achieves the same heap size reduction (39%) as Redis’s active defragmentation.

> With Mesh, insertion takes 1.76s, while with Redis’s default of jemalloc, insertion takes 1.72s.

These results can be verified in the data in the generated files `results/1-redis/memory.relative.tsv` and `results/1-redis/speed.relative.tsv`.


#### 2. SPEC

> Mesh modestly decreases average memory consumption (geomean: −2.4%) vs. glibc, while imposing minimal execution time overhead (geomean: 0.7%).

> Perlbench.400: glibc peak RSS is 664MB, Mesh reduces its peak RSS to 564MB (a 15% reduction) while increasing its runtime overhead by only 3.9%.

These results can be verified in the data in the generated files `results/2-spec/results.tsv`.


#### 3. Empirical value of randomization

> Tested with Firefox + Redis and found no significant differences when randomization was disabled


##### Ruby example

> meshing disabled: similar runtime + heap size to jemalloc

> meshing enabled but randomization disabled: 4% runtime overhead, 3% reduction in heap size

> randomization on has time overhead of 10.7% compared to jemalloc, 19% heap size reduction

These results can be verified in the data in the generated files `results/3-ruby/memory.relative.tsv` and  `results/3-ruby/speed.relative.tsv`
