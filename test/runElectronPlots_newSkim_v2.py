import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v11', '')

outputFile = "ntuple_newskim_eraBv2.root"
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())

process.ntupler = cms.EDAnalyzer(
    'ElectronPlots',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    electrons    = cms.InputTag("slimmedElectrons"),
    inputLeptonRho      = cms.InputTag("fixedGridRhoFastjetAll"),
    isMC         = cms.bool(False)
    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( outputFile )
                                   )

process.load("Demo/DemoAnalyzer/ZElectronsSelector_cfi") 
process.p = cms.Path(process.zdiElectronSequence*process.ntupler)

