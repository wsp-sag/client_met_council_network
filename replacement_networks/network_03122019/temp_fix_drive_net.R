library(tidyverse)
library(sf)

drive_link <- st_read("network_03122019/drive_link.shp")
drive_node <- st_read("network_03122019/drive_node.shp")

colnames(drive_link)

drive_link <- drive_link %>%
  mutate(RC_NUM = ifelse(RC_NUM == 0, 20, RC_NUM)) %>%
  mutate(ASGNGRP = ifelse(ASGNGRP == 0, 15, ASGNGRP))

st_write(drive_link, "network_03122019/fixed_drive_link.shp")
