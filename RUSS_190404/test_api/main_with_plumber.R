library(plumber)
r <- plumb("with_plumber.R")
r$run(port=8000)
