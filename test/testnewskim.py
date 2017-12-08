import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_Candidate_forECALStudies', '')

inputFilesData = cms.untracked.vstring(
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/008329E5-368F-E711-A1CD-02163E01A21D.root',
)

inputFiles = inputFilesData
#outputFile = "ntuple_newskim_eraD.root"
outputFile = "newskim.root"
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
process.source = cms.Source ("PoolSource", fileNames = inputFiles ) 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) ) 

process.ntupler = cms.EDAnalyzer(
    'ElectronPlots',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    electrons = cms.InputTag("slimmedElectrons"),
    inputLeptonRho = cms.InputTag("fixedGridRhoFastjetAll"),
    isMC = cms.bool(False)
    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( outputFile )
                                   )

#process.load("Demo/DemoAnalyzer/ZElectronsSelector_cfi") 
process.load("Demo/DemoAnalyzer/ZMassSkim_cff")
#process.load("Demo/DemoAnalyzer/ZElectronSkim_cff")
process.p = cms.Path(process.zdiElectronSequence*process.ntupler)


