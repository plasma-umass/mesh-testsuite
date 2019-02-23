library(ggplot2)
library(grid)
library(scales)

dat_jemalloc <- read.delim('results/0-firefox/memory/jemalloc.tsv', header = TRUE, sep = '\t')
dat_jemalloc$alloc <- 'jemalloc'
dat_jemalloc$heap <- (dat_jemalloc$rss + dat_jemalloc$kernel) / 1024.0 / 1024.0
dat_jemalloc$time <- dat_jemalloc$time / 1000000000.0

dat_mesh2y <- read.delim('results/0-firefox/memory/mesh.tsv', header = TRUE, sep = '\t')
dat_mesh2y$alloc <- 'Mesh'
dat_mesh2y$heap <- (dat_mesh2y$rss + dat_mesh2y$kernel) / 1024.0 / 1024.0
dat_mesh2y$time <- dat_mesh2y$time / 1000000000.0

p <- ggplot() +
    geom_line(data=dat_mesh2y, size=.5, aes(x=time, y=heap, color=alloc, group=1)) +
    geom_line(data=dat_jemalloc, size=.5, aes(x=time, y=heap, color=alloc, group=8)) +
    scale_y_continuous('RSS (MiB)', expand = c(0, 0), limits = c(0, 900)) +
    scale_x_continuous('Time Since Program Start (seconds)', expand = c(0, 0), limits = c(0, 144)) +
    theme_bw(20, 'Times') +
    guides(colour = guide_legend(nrow = 1)) +
    theme(
        plot.title = element_text(size=10, face='bold'),
        strip.background = element_rect(color='dark gray', linetype=0.5),
        plot.margin = unit(c(.1, .1, 0.1, 0), 'in'),
        panel.border = element_rect(colour='gray'),
        panel.margin = unit(c(0, 0, 0, 0), 'in'),
        legend.position = 'bottom',
        legend.key = element_rect(color=NA),
        legend.key.size = unit(0.15, 'in'),
        legend.margin = unit(0.1, 'in'),
        legend.title=element_blank(),
        axis.title.y = element_text(size=20),
        axis.text.x = element_text(angle = 0, hjust = 1)
    )

ggsave(p, filename='results/0-firefox/figure-6-firefox.pdf', width=7, height=2.75)
