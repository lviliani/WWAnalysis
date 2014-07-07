How to run skim
=======

    cd src/WWAnalysis/SkimStep/test
    cmsRun latinosYieldSkim.py print inputFiles=file:/data/amassiro/CMSSWRoot/Summer12/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/28DCA073-84D4-E111-A8D0-F04DA23BCE4C.root isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_WWmg.root   correctMetPhi=False
    cmsRun latinosYieldSkim.py print inputFiles=file:/data/amassiro/CMSSWRoot/Summer12/GluGluToHHTo2B2WToLNuLNu_mH-125_8TeV-madgraph-pythia6-tauola_AODSIM_PU_S10_START53_V19-v1/4486E5A3-3EF7-E211-A407-0017A4770834.root  isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_HH.root   correctMetPhi=False

to skip any filter at skim level: to be done only for GEN samples needed for unfolding purposes (doNoFilter=True)

    cmsRun latinosYieldSkim.py print inputFiles=file:/data/amassiro/CMSSWRoot/Summer12/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/28DCA073-84D4-E111-A8D0-F04DA23BCE4C.root isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_WWmg.root   correctMetPhi=False    doNoFilter=True


    cmsRun latinosYieldSkim_ggWW.py print inputFiles=file:/afs/cern.ch/user/k/kbutanov/WORK/public/HWWwidth/Hw25/Sig_OnPeak/AODSIM_1.root isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_ggWW.root   correctMetPhi=False    doNoFilter=True


Working examples
=======

    cmsRun latinosYieldSkim.py print inputFiles=file:/data/amassiro/CMSSWRoot/Summer12/ZllHWWlvlv_private_production/AODSIM-ZHWWlvlv.root    isMC=True globalTag=GR_R_52_V7  outputFile=/tmp/amassiro/latinosYieldSkim_MC_ZHWW.root   correctMetPhi=False
