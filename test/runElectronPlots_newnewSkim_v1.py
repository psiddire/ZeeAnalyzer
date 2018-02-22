import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v11', '')

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

#inputFilesData = cms.untracked.vstring(
#'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/030/00000/E69F63AA-EE8E-E711-8121-02163E019BAF.root',
#'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/008329E5-368F-E711-A1CD-02163E01A21D.root',
#'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/04BB9D82-398F-E711-B74B-02163E019BDF.root'
#)

#inputFiles = inputFilesData
#outputFile = "ntuple_newskim_eraB.root"
outputFile = "electron_ntuple_newskim.root"
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

process.load("Demo/DemoAnalyzer/ZElectronsSelector_new_cfi") 
process.p = cms.Path(process.zdiElectronSequence*process.ntupler)

