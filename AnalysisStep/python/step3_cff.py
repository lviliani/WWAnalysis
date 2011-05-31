import FWCore.ParameterSet.Config as cms

nverticesModule = cms.EDProducer("VertexMultiplicityCounter",
    probes = cms.InputTag("REPLACE_ME"),
    objects = cms.InputTag("offlinePrimaryVertices"),
    objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
)

step3Tree = cms.EDFilter("ProbeTreeProducer",
    cut = cms.string("q(0)*q(1) < 0 && !isSTA(0) && !isSTA(1) && "+
                     "leptEtaCut(2.4,2.5) && "+
                     "ptMax > 20 && "+
                     "((abs(pdgIdByPt(1)) == 13 && ptMin > 10) || "+
                     " (abs(pdgIdByPt(1)) == 11 && ptMin > 15)) && "
                     "nExtraLep(10) == 0 "
                    +" && passesIP"
                   +(" && triggerMatchingCut('DATASET')")
    ),
    variables = cms.PSet(
        hypo = cms.string("hypo()"),
        mll  = cms.string("mll()"),
        ptll = cms.string("pTll()"),
        yll  = cms.string("yll()"),
        pt1  = cms.string("ptMax"),
        pt2  = cms.string("ptMin"),
        met  = cms.string("pfMet"),
        mmet = cms.string("minMet"),
        pmet = cms.string("projPfMet"),
        pmmet = cms.string("min(projPfMet,projChargedMet)"), ##note: min of proj and proj of min are not the same
        dphill = cms.string("dPhill()"),
        drll   = cms.string("dRll()"),
        dphilljet  = cms.string("dPhillLeadingJet(5.0)"),
        dphillcjet = cms.string("dPhillLeadingJet(2.5)"),
        dphillmet  = cms.string("dPhillMet('PFMET')"),
        dphillmmet = cms.string("dPhillMet('MINMET')"),
        dphilmet = cms.string("dPhilMet('PFMET')"),
        mtw1 = cms.string("mTByPt(0,'PFMET')"),
        mtw2 = cms.string("mTByPt(1,'PFMET')"),
        mth  = cms.string("mTHiggs('PFMET')"),
        gammaMRStar = cms.string("gammaMRStar"),
        njet  = cms.string("nJets(30)"),
        ncjet = cms.string("nCentralJets(30,2.5)"),
        nbjet = cms.string("bTaggedJetsOver(30,2.1)"),
        bestiso  = cms.string("allIsoByIso(0)/ptByIso(0)"),
        worstiso = cms.string("allIsoByIso(1)/ptByIso(1)"),
        worstJetLepPt = cms.string("max(matchedJetPt(0, 0.5)/pt(0), matchedJetPt(1, 0.5)/pt(1))"),
        dataset = cms.string("REPLACE_ME")
    ),
    flags = cms.PSet(
        sameflav = cms.string("hypo == 3 || hypo == 6"),
        zveto    = cms.string("abs(mll-91.1876)>15 || hypo == 4 || hypo == 5"),
        bveto    = cms.string("bTaggedJetsUnder(30,2.1) == 0 && nSoftMu(3) == 0"),
        bveto_ip = cms.string("bTaggedJetsUnder(30,2.1) == 0"),
        bveto_mu = cms.string("nSoftMu(3) == 0"),
    ),
)

from WWAnalysis.AnalysisStep.pileupReweighting_cfi import reWeightVector
mcWeight     = cms.EDProducer("CombinedWeightProducer",
    baseWeight = cms.double(1.0),
    puWeight   = cms.vdouble(*reWeightVector[:]),
    puLabel    = cms.InputTag("addPileupInfo"),
)
higgsPt = cms.EDProducer("HWWKFactorProducer",
    genParticlesTag = cms.InputTag("onlyHiggsGen"),
    inputFilename = cms.untracked.string("REPLACE_ME"),
    ProcessID = cms.untracked.int32(10010),
    Debug =cms.untracked.bool(False)
)