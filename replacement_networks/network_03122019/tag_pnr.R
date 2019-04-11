library(tidyverse)
library(sf)
options(stringsAsFactors = FALSE)


old_pnr_df <- read.csv("lookup_files/met_council_default_pnr.csv")
old_nodes_df <- st_read("client_network2015_gdb/client_node_2015.shp")
new_nodes_df <- st_read("network_03122019/drive_node_with_rail.shp")

old_pnr_df <- old_pnr_df %>%
  mutate(access_node = str_extract(node, "[0-9]+")) %>%
  mutate(stop_node = str_extract(node, "(?<=-| )[0-9]+"))

old_nodes_df <- old_nodes_df %>%
  mutate(match_node = st_nearest_feature(old_nodes_df, new_nodes_df)) %>%
  left_join()
