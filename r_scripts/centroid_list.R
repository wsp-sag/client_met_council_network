################################################################################
# Title: Create input_centroid_nodes.csv and centroid_links.csv
# Purpose: A database of centroid and centroid connector node numbers and 
#          coordinates from the existing MetCouncil network , with flags 
#          indicating which zones are external. A second database of centroid
#          connector links, A & B nodes, from the existing MetCouncil Network.
# Author: John Helsel
# Date: 21 January 2019

# Libraries & packages
library(foreign)
library(tidyverse)
library(sf)

options(stringsAsFactors = FALSE)

# IO Paths
link_df_path <- "input/base_network_link.shp"
node_df_path <- "input/base_network_node.shp"
taz_df_path <- "input/Zones_2015.dbf"

centroid_links_out_path <- "output/centroid_links.csv"
centroid_nodes_out_path <- "output/input_centroid_nodes.csv"

# Read in files
link_df <- st_read(link_df_path) %>% 
  rename_all(tolower)
st_geometry(link_df) <- NULL

node_df <- st_read(node_df_path) %>%
  rename_all(tolower)
st_geometry(node_df) <- NULL


rm(link_df_path, node_df_path)

# Find centroids
external_node_list <- link_df %>%
  filter(a < 3200) %>% 
  filter(county == 10) %>%
  .$a

node_df <- node_df %>%
  mutate(centroid = ifelse(n < 3200, 1, 0),
         external = ifelse(n %in% external_node_list, 1, 0))

centroid_link_df <- link_df %>%
  filter(a < 3200 | b < 3200) %>%
  select(a, b)

#Write results
write.csv(centroid_link_df, centroid_links_out_path)
write.csv(node_df, centroid_nodes_out_path)