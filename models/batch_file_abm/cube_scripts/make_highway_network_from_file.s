RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI NETI = "%SCENARIO_DIR%/complete_network.net"

IF (drive_access = 0 & transit_access = 0) DELETE
/*
IS_ML = 0

IF (model_link_id = 416366) SEGMENT_ID = 5
IF (model_link_id = 414813) SEGMENT_ID = 5
IF (model_link_id = 381248) SEGMENT_ID = 5
IF (model_link_id = 381223) SEGMENT_ID = 5
IF (model_link_id = 417878) SEGMENT_ID = 5
IF (model_link_id = 418556) SEGMENT_ID = 5
IF (model_link_id = 418512) SEGMENT_ID = 5
IF (model_link_id = 419032) SEGMENT_ID = 5
IF (model_link_id = 419044) SEGMENT_ID = 5
IF (model_link_id = 419040) SEGMENT_ID = 5
IF (model_link_id = 419637) SEGMENT_ID = 5
IF (model_link_id = 419634) SEGMENT_ID = 5
IF (model_link_id = 417947) SEGMENT_ID = 5
IF (model_link_id = 420448) SEGMENT_ID = 5
IF (model_link_id = 420447) SEGMENT_ID = 5
IF (model_link_id = 394057) SEGMENT_ID = 5

IF (model_link_id = 416366) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 414813) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 381248) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 381223) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 417878) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 418556) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 418512) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 419032) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 419044) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 419040) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 419637) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 419634) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 417947) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 420448) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 420447) SEGMENT_ID = 5, IS_ML = 1
IF (model_link_id = 394057) SEGMENT_ID = 5, IS_ML = 1
*/
FILEO NETO = "%SCENARIO_DIR%/highway.net"

ENDRUN
