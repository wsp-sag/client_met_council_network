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
link_shp_path <- "input/base_network_link.shp"
node_shp_path <- "input/base_network_node.shp"
taz_

centroid_links_out_path <- "output/centroid_links.csv"
centroid_nodes_out_path <- "output/input_centroid_nodes.csv"

# Read in files
link_shp <- st_read(link_shp_path) %>% 
  rename_all(tolower)
node_shp <- st_read(node_shp_path) %>%
  rename_all(tolower)

link_shp <- link_shp %>% 
  mutate()