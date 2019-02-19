dir.create(Sys.getenv("R_LIBS_USER"), showWarnings = FALSE, recursive = TRUE)

install.packages(c("dplyr", "forcats", "ggplot2", "grid", "scales"), Sys.getenv("R_LIBS_USER"), repos="https://cran.case.edu/")
