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
'/store/data/Run2017D/DoubleEG/MINIAOD/PromptReco-v1/000/302/031/00000/008329E5-368F-E711-A1CD-02163E01A21D.root',      
)

inputFilesMC = cms.untracked.vstring(
'/store/mc/RunIISummer17MiniAOD/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/92X_upgrade2017_realistic_v7-v1/110000/2057EC95-8975-E711-8966-0CC47A7C3444.root'
)

#inputFiles = inputFilesData
outputFile = "ntuple_skim_MCv10ext1v2.root"
#process.source = cms.Source ("PoolSource", fileNames = inputFiles )                             
#process.source.lumisToProcess = LumiList.LumiList(filename = 'eraB.json').getVLuminosityBlockRange()

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.ntupler = cms.EDAnalyzer(
    'ElectronPlots',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    electrons    = cms.InputTag("slimmedElectrons"),
    genParticles = cms.InputTag("prunedGenParticles"),
    inputLeptonRho      = cms.InputTag("fixedGridRhoFastjetAll"),
    isMC         = cms.bool(True)
    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( outputFile )
                                   )

process.load("Demo/DemoAnalyzer/ZElectronSkim_cff") 
process.p = cms.Path(process.zdiElectronSequence*process.ntupler)

