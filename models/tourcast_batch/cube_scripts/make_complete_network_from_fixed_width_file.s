RUN PGM = NETWORK MSG = "Read in network from fixed width file"
FILEI LINKI[1] = %LINK_DATA_PATH%, VAR=model_link_id, BEG=1, LEN=7, VAR=A, BEG=9, LEN=6, VAR=B, BEG=16, LEN=6, VAR=shstGeometryId(C32), BEG=23, LEN=32, VAR=distance, BEG=56, LEN=22, VAR=roadway(C33), BEG=79, LEN=33, VAR=name(C111), BEG=113, LEN=111, VAR=roadway_class, BEG=225, LEN=2, VAR=bike_access, BEG=228, LEN=1, VAR=transit_access, BEG=230, LEN=1, VAR=walk_access, BEG=232, LEN=1, VAR=drive_access, BEG=234, LEN=1, VAR=truck_access, BEG=236, LEN=1, VAR=trn_priority_AM, BEG=238, LEN=1, VAR=trn_priority_MD, BEG=240, LEN=1, VAR=trn_priority_PM, BEG=242, LEN=1, VAR=trn_priority_NT, BEG=244, LEN=1, VAR=ttime_assert_AM, BEG=246, LEN=4, VAR=ttime_assert_MD, BEG=251, LEN=4, VAR=ttime_assert_PM, BEG=256, LEN=4, VAR=ttime_assert_NT, BEG=261, LEN=4, VAR=lanes_AM, BEG=266, LEN=1, VAR=lanes_MD, BEG=268, LEN=1, VAR=lanes_PM, BEG=270, LEN=1, VAR=lanes_NT, BEG=272, LEN=1, VAR=price_sov_AM, BEG=274, LEN=1, VAR=price_hov2_AM, BEG=276, LEN=1, VAR=price_hov3_AM, BEG=278, LEN=1, VAR=price_truck_AM, BEG=280, LEN=1, VAR=price_sov_MD, BEG=282, LEN=1, VAR=price_hov2_MD, BEG=284, LEN=1, VAR=price_hov3_MD, BEG=286, LEN=1, VAR=price_truck_MD, BEG=288, LEN=1, VAR=price_sov_PM, BEG=290, LEN=1, VAR=price_hov2_PM, BEG=292, LEN=1, VAR=price_hov3_PM, BEG=294, LEN=1, VAR=price_truck_PM, BEG=296, LEN=1, VAR=price_sov_NT, BEG=298, LEN=1, VAR=price_hov2_NT, BEG=300, LEN=1, VAR=price_hov3_NT, BEG=302, LEN=1, VAR=price_truck_NT, BEG=304, LEN=1, VAR=assign_group, BEG=306, LEN=2, VAR=access_AM(C15), BEG=309, LEN=15, VAR=access_MD(C15), BEG=325, LEN=15, VAR=access_PM(C15), BEG=341, LEN=15, VAR=access_NT(C15), BEG=357, LEN=15, VAR=mpo, BEG=373, LEN=1, VAR=area_type, BEG=375, LEN=1, VAR=county, BEG=377, LEN=2, VAR=centroidconnect, BEG=380, LEN=1, VAR=AADT, BEG=382, LEN=6, VAR=count_year, BEG=389, LEN=4, VAR=count_AM, BEG=394, LEN=5, VAR=count_MD, BEG=400, LEN=5, VAR=count_PM, BEG=406, LEN=5, VAR=count_NT, BEG=412, LEN=5, VAR=count_daily, BEG=418, LEN=6, VAR=HOV, BEG=425, LEN=3
FILEI NODEI[1] = %NODE_DATA_PATH%, VAR=N, BEG=1, LEN=6, VAR=osm_node_id(C10), BEG=8, LEN=10, VAR=bike_node, BEG=19, LEN=1, VAR=transit_node, BEG=21, LEN=1, VAR=walk_node, BEG=23, LEN=1, VAR=drive_node, BEG=25, LEN=1, VAR=X, BEG=27, LEN=18, VAR=Y, BEG=46, LEN=18
FILEO NETO = "%SCENARIO_DIR%/complete_network.net"
    ZONES = %zones%

ENDRUN
