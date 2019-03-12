library(tidyverse) 

drive_link <- read.csv("network_03042019/drive_network_for_modeling.csv")
drive_node <- read.csv("network_03042019/osm_drive_nodes_with_centroid.csv")

drive_link <- drive_link %>%
  select(-ID, -geometry)


drive_node <- drive_node %>%
  mutate(geometry = as.character(geometry)) %>%
  mutate(geometry = str_replace(geometry, "POINT \\(", ""),
         geometry = str_replace(geometry, "\\)", "")) %>%
  mutate(X = as.numeric(str_extract(geometry, ".*(?= )")),
         Y = as.numeric(str_extract(geometry, "(?<= ).*"))) %>%
  select(N = id, X, Y, OSMID = osmid)

write_csv(drive_link, "network_03042019/fixed_drive_network_for_modeling.csv", col_names = FALSE)
write_csv(drive_node, "network_03042019/fixed_osm_drive_nodes_with_centroid.csv", col_names = FALSE)

bike_link <- read.csv("network_03042019/bike_network_for_modeling.csv")
bike_node <- read.csv("network_03042019/osm_bike_nodes_with_centroid.csv")

bike_link <- bike_link %>%
  mutate(BIKE = 3) %>% 
  select(A, B, DISTANCE, COUNTY, AREA< CENTROID, BIKE, isBikeLink)


bike_node <- bike_node %>%
  mutate(geometry = as.character(geometry)) %>%
  mutate(geometry = str_replace(geometry, "POINT \\(", ""),
         geometry = str_replace(geometry, "\\)", "")) %>%
  mutate(X = as.numeric(str_extract(geometry, ".*(?= )")),
         Y = as.numeric(str_extract(geometry, "(?<= ).*"))) %>%
  select(N = id, X, Y, OSMID = osmid)

write_csv(bike_link, "network_03042019/fixed_bike_network_for_modeling.csv", col_names = FALSE)
write_csv(bike_node, "network_03042019/fixed_osm_bike_nodes_with_centroid.csv", col_names = FALSE)

walk_link <- read.csv("network_03042019/walk_network_for_modeling.csv")
walk_node <- read.csv("network_03042019/osm_walk_nodes_with_centroid.csv")

walk_link <- walk_link %>%
  select(-ID, -geometry)


walk_node <- walk_node %>%
  mutate(geometry = as.character(geometry)) %>%
  mutate(geometry = str_replace(geometry, "POINT \\(", ""),
         geometry = str_replace(geometry, "\\)", "")) %>%
  mutate(X = as.numeric(str_extract(geometry, ".*(?= )")),
         Y = as.numeric(str_extract(geometry, "(?<= ).*"))) %>%
  select(N = id, X, Y, OSMID = osmid)

write_csv(walk_link, "network_03042019/fixed_walk_network_for_modeling.csv", col_names = FALSE)
write_csv(walk_node, "network_03042019/fixed_osm_walk_nodes_with_centroid.csv", col_names = FALSE)
