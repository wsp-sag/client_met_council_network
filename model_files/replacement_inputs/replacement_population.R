# Short Household and person DBF

library(tidyverse)
library(foreign)

person_path <- "../WSPHandoff_Jan2019/ABM 2017/Input/Persons2015.dbf"
household_path <- "../WSPHandoff_Jan2019/ABM 2017/Input/Households2015.dbf"

person_df <- read.dbf(person_path)
household_df <- read.dbf(household_path)

household_df <- household_df %>% 
  filter(HHID <= 100)

person_df <- person_df %>%
  filter(HHID %in% household_df$HHID)

write.dbf(household_df, "Households2015_custom.dbf")
write.dbf(person_df, "Persons2015_custom.dbf")
