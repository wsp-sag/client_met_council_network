CONVERTMAT FROM="%SCENARIO_DIR%\XIT_WK_SKIM_%ITER%_%TPER%.SKM" TO="%SCENARIO_DIR%\XIT_WK_SKIM_%ITER%_%TPER%.OMX" FORMAT=OMX COMPRESSION=0
CONVERTMAT FROM="%SCENARIO_DIR%\XIT_DR_SKIM_%ITER%_%TPER%.SKM" TO="%SCENARIO_DIR%\XIT_DR_SKIM_%ITER%_%TPER%.OMX" FORMAT=OMX COMPRESSION=0

; CONVERTMAT FROM="..\..\data\test_new_network_outputs\XIT_WK_SKIM_%ITER%_PK.SKM" TO="..\..\data\test_new_network_outputs\XIT_WK_SKIM_%ITER%_PK.OMX" FORMAT=OMX COMPRESSION=0