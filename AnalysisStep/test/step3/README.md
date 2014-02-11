How to run step 2+3
=======

for MC

    cd src/WWAnalysis/AnalysisStep/test/step3
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_WWmg.root  label=WW id=123456789  scale=1 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_WWmg.root
    cmsRun step3.py print inputFiles=file:/tmp/amassiro/latinosYieldSkim_MC_HH.root    label=HH id=123456789  scale=1 outputFile=/tmp/amassiro/step3_latinosYieldSkim_MC_HH.root



for DATA

    cd src/WWAnalysis/AnalysisStep/test/step3
    cmsRun step3.py print inputFiles=file:data.root    label=MuEG id=1234 outputFile=latinosStep3_DATA_202075_VBF.root json=certifiedLatinos.53X.Moriond

label should be one of the following (used for "trigger" to avoid double counting):

    'SingleElectron', 'DoubleElectron', 'SingleMuon', 'DoubleMuon', 'MuEG'


