import FWCore.ParameterSet.Config as cms
#import FWCore.PythonUtilities.LumiList as LumiList

process = cms.Process('Demo')

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_Candidate_forECALStudies', '')

# input
inputFilesData = cms.untracked.vstring(
#'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/030/00000/E69F63AA-EE8E-E711-8121-02163E019BAF.root',
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/008329E5-368F-E711-A1CD-02163E01A21D.root',      
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/04BB9D82-398F-E711-B74B-02163E019BDF.root',
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/407638D4-4B8F-E711-AC24-02163E01437E.root',
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/44B91A0E-488F-E711-A372-02163E019CA5.root',
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/5479D9DF-3C8F-E711-BCF4-02163E01A5EB.root',
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/6496C386-518F-E711-B09E-02163E01341D.root'
)

inputFiles = inputFilesData
outputFile = "ntuple_woskim_eraD.root"
#process.source = cms.Source ("PoolSource", fileNames = inputFiles )                             
#process.source.lumisToProcess = LumiList.LumiList(filename = 'eraB.json').getVLuminosityBlockRange()

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

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

process.load("Demo/DemoAnalyzer/ZMassSkim_cff") 
process.p = cms.Path(process.zdiElectronSequence*process.ntupler)

