; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = HIGHWAY MSG = 'Skim Free Flow Network'

FILEI NETI = "{SCENARIO_DIR}\ALL_NET.net"

FILEO MATO[1] = "{SCENARIO_DIR}\HWY_SKIM.tmp",
  MO = 1-16, NAME = daptime, daptoll, dantime, dantoll, dapdist, a2ptime, a2ptoll, 
                    a2ntime, a2ntoll, a2pdist, a3ptime, a3ptoll, a3ntime, a3ntoll, 
                    a3pdist, lnrtdist

PROCESS PHASE = ILOOP

    PATHLOAD PATH = TIME,  
    MW[1] = PATHTRACE(TIME) NOACCESS = 1000,
    MW[5] = PATHTRACE(li.DISTANCE) NOACCESS = 1000 

    ; Intrazonal time / distance is half that to nearest zone
    MW[1][I] = LOWEST(1, 1, 0.1, 999, I) / 2 
    MW[5][I] = LOWEST(5, 1, 0.1, 999, I) / 2 

    MW[2] = 0
    MW[3] = MW[1]
    MW[4] = MW[2]
    
    ; SR2
    MW[6] = MW[1]
    MW[7] = MW[2]
    MW[8] = MW[3]
    MW[9] = MW[4]
    MW[10] = MW[5]
    
    ; SR3
    MW[11] = MW[1]
    MW[12] = MW[2]
    MW[13] = MW[3]
    MW[14] = MW[4]
    MW[15] = MW[5]   
    
    ; ln(RT Dist + 1)
    MW[16] = LN(2 * MW[5] + 1)
    
ENDPROCESS

ENDRUN
