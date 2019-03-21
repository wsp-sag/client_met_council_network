library(tidyverse)
library(sf)
library(foreign)
library(ggplot2)

nm <- read_csv("comparisons/walk_comparison.csv", col_names = FALSE)

nm <- nm %>%
  select(origin = X1,
         destination = X2,
         new_walk = X4,
         old_walk = X6) 

# qplot(data = nm, x = new_walk, y = old_walk)

nm_trimmed <- nm %>%
  filter(old_walk < 1000)
