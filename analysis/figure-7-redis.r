library(ggplot2)
library(grid)
library(scales)

dat_glibc <- read.delim('results/1-redis/memory/libc.tsv', header = TRUE, sep = '\t')
dat_glibc$alloc <- 'glibc'
dat_glibc$heap <- (dat_glibc$rss + dat_glibc$kernel) / 1024.0 / 1024.0
dat_glibc$time <- dat_glibc$time / 1000000000.0

dat_jemalloc <- read.delim('results/1-redis/memory/jemalloc.tsv', header = TRUE, sep = '\t')
dat_jemalloc$alloc <- 'jemalloc + activedefrag'
dat_jemalloc$heap <- (dat_jemalloc$rss + dat_jemalloc$kernel) / 1024.0 / 1024.0
dat_jemalloc$time <- dat_jemalloc$time / 1000000000.0

dat_mesh0n <- read.delim('results/1-redis/memory/mesh0n.tsv', header = TRUE, sep = '\t')
dat_mesh0n$alloc <- 'Mesh (meshing disabled)'
dat_mesh0n$heap <- (dat_mesh0n$rss + dat_mesh0n$kernel) / 1024.0 / 1024.0
dat_mesh0n$time <- dat_mesh0n$time / 1000000000.0

dat_mesh2y <- read.delim('results/1-redis/memory/mesh2y.tsv', header = TRUE, sep = '\t')
dat_mesh2y$alloc <- 'Mesh'
dat_mesh2y$heap <- (dat_mesh2y$rss + dat_mesh2y$kernel) / 1024.0 / 1024.0
dat_mesh2y$time <- dat_mesh2y$time / 1000000000.0


p <- ggplot() +
    geom_line(data=dat_mesh0n, size=.3, aes(x=time, y=heap, color=alloc, group=2)) +
    geom_line(data=dat_mesh2y, size=.3, aes(x=time, y=heap, color=alloc, group=5)) +
    geom_line(data=dat_jemalloc, linetype='dotted', size=.4, aes(x=time, y=heap, color=alloc, group=4)) +
    scale_y_continuous('RSS (MiB)', expand = c(0, 0), limits = c(0, 300)) +
    scale_x_continuous('Time Since Program Start (seconds)', expand = c(0, 0), limits = c(0, 6.0)) +
    theme_bw(10, 'Times') +
    guides(colour = guide_legend(nrow = 1)) +
    theme(
        plot.title = element_text(size=10, face='bold'),
        strip.background = element_rect(color='dark gray', linetype=0.5),
        plot.margin = unit(c(.1, .1, 0, 0), 'in'),
        panel.border = element_rect(colour='gray'),
        panel.margin = unit(c(0, 0, -0.5, 0), 'in'),
        legend.position = 'bottom',
        legend.key = element_rect(color=NA),
        legend.key.size = unit(0.15, 'in'),
        legend.margin = unit(0, 'in'),
        legend.title=element_blank(),
        axis.title.y = element_text(size=9),
        axis.text.x = element_text(angle = 0, hjust = 1)
    )

ggsave(p, filename='results/1-redis/figure-7-redis.pdf', width=3.4, height=1.5)
