# Process statistics on outputs from loaded highway network
library(tidyverse)
library(foreign)

options(stringsAsFactors = FALSE)

loaded_network_path <- "../network_test_outputs/HWY_LDNET_4_AM.dbf"

loaded_network_df <- read.dbf(loaded_network_path)

