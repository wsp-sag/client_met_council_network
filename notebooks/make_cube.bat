SET LINK_DATA_PATH=links.txt
SET NODE_DATA_PATH=nodes.txt
SET zones=3061
SET SCENARIO_DIR=.
runtpp make_complete_network_from_fixed_width_file.s
runtpp make_roadway_network.s

