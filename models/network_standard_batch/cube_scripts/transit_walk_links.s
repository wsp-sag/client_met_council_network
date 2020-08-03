; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=NETWORK MSG='Add walk links to transit network'
FILEO NETO = "%SCENARIO_DIR%\complete_transit_network.NET"
FILEI NETI[1] = "%SCENARIO_DIR%\HWY_LDNET_%ITER%_%PER%.NET"
FILEI NETI[2] = "%SCENARIO_DIR%\walk.net"

MERGE RECORD = TRUE FIRST=A,B, model_link_id,distance,roadway,name,drive_access,
                          walk_access,bike_access,truck_access,bus_only,
                          rail_only,assign_group,managed,segment_id,area_type,
                          county,centroidconnect,mpo,roadway_class,AADT,
                          count_AM,count_MD,count_PM,count_NT,count_daily,
                          count_year,trn_priority_AM,trn_priority_MD,
                          trn_priority_PM,trn_priority_NT,ttime_assert_AM,
                          ttime_assert_MD,ttime_assert_PM,ttime_assert_NT,
                          lanes_AM,lanes_MD,lanes_PM,lanes_NT,ML_lanes_AM,
                          ML_lanes_MD,ML_lanes_PM,ML_lanes_NT,price_sov_AM,
                          price_hov2_AM,price_hov3_AM,price_truck_AM,
                          price_sov_MD,price_hov2_MD,price_hov3_MD,
                          price_truck_MD,price_sov_PM,price_hov2_PM,
                          price_hov3_PM,price_truck_PM,price_sov_NT,
                          price_hov2_NT,price_hov3_NT,price_truck_NT,access_AM,
                          access_MD,access_PM,access_NT,RCI,LANES,LINKCLASS,SPEED,
                          CAPACITY,TIME,AMCAP,OFFCAP,PMCAP,NEWVOLAM,CONGAM,
                          NEWVOLMD,CONGMD,SEGMENT_IDY,ALPHA,BETA


ZONES = %zones%
PHASE=LINKMERGE
ENDPHASE

ENDRUN