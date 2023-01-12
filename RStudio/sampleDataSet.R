library(LaF)

sample1 <- function(file, n) {
  lf <- laf_open(detect_dm_csv(file, sep = ",", header = TRUE, factor_fraction = -1))
  newData <- read_lines(lf, sample(1:nrow(lf), n))
  return(newData)
}
