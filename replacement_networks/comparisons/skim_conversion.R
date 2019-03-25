library(tidyverse)
library(sf)
library(foreign)
library(ggplot2)

skims <- read_csv("comparisons/skim_comparison.csv", col_names = FALSE)

skims <- skims %>%
  select(origin = X1,
         destination = X2,
         new_walk = X4,
         old_walk = X6,
         new_bike = X8,
         old_bike = X10,
         new_drive = X12,
         old_drive = X14) 

# skims <- skims %>%
#   mutate(drive_diff = new_drive - old_drive)

skims_temp <- skims %>%
  select(o_temp = destination, d_temp = origin, new_drive_1 = new_drive) %>%
  rename(origin = o_temp, destination = d_temp)

skims <- skims_temp %>% 
  left_join(skims, by = c("origin", "destination")) %>% 
  mutate(drive_diff = new_drive_1 - new_drive)

