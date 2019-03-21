library(tidyverse)
library(foreign)

walk_net <- read.dbf("network_03122019/walk_link.dbf") 
walk_node <- read.dbf("network_03122019/walk_node.dbf")

a_count <- walk_net %>% 
  group_by(A) %>% 
  summarise(n = n()) 

b_count <- walk_net %>%
  group_by(B) %>%
  summarise(n = n())

# Remove dead end links
walk_net_write <- walk_net %>%
  left_join(a_count, by = "A") %>%
  filter(n > 1 | CENTROID == 1) %>%
  select(-n) %>% 
  left_join(b_count, by = "B") %>%
  filter(n > 1 | CENTROID == 1) %>%
  select(-n)

walk_node_write <- walk_node %>%
  left_join(a_count, by = c("N" = "A")) %>% 
  filter(n > 1) %>% 
  select(-1)

# Remove intermediate nodes
replacement_links <- walk_net %>%
  left_join(a_count, by = "A") %>%
  filter(n == 2) %>% 
  filter(A == 3280 | B == 3280) %>% 
  select(A, B, DISTANCE)

replacement_links <- replacement_links %>%
  rename(d1 = DISTANCE) %>%
  left_join(replacement_links %>% select(d2 = DISTANCE), by = c("A" = "B"))


write.dbf(walk_net_write, "network_03122019/test_walk_link.dbf")
write.dbf(walk_node_write, "network_03122019/test_walk_node.dbf")

result <- read_csv("comparisons/walk_comparison.csv", col_names = FALSE) 
