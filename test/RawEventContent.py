import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_Candidate_forECALStudies', '')

inputFilesData = cms.untracked.vstring(
'/store/relval/CMSSW_9_2_0/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_91X_mcRun2_asymptotic_v3-v1/10000/00D37868-DF3C-E711-A345-002618FDA21D.root',
#'/store/relval/CMSSW_9_2_9/RelValZEE_13/GEN-SIM-DIGI-RAW/PU25ns_92X_upgrade2017_realistic_v10-v1/00000/04D468FE-5581-E711-B966-0CC47A4C8F18.root',
)

inputFiles = inputFilesData

process.source = cms.Source ("PoolSource", 
                             fileNames = inputFiles,
                             inputCommands=cms.untracked.vstring(
                             "keep *",
                             "drop  *_simEmtfDigis_*_HLT",
                             #"drop  *_simEmtfDigis_RPC_HLT",
                )
) 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) ) 

#process.RAWEventContent = cms.PSet(
#     outputCommands = cms.untracked.vstring('keep *',
#         'keep  FEDRawDataCollection_rawDataCollector_*_*',
#         'keep  FEDRawDataCollection_source_*_*'),
#     splitLevel = cms.untracked.int32(0),
# )


process.RAWoutput = cms.OutputModule("PoolOutputModule",
#     outputCommands = process.RAWEventContent.outputCommands,
     fileName = cms.untracked.string('RawOutput_1.root'),
     dataset = cms.untracked.PSet(
         filterName = cms.untracked.string(''),
         dataTier = cms.untracked.string('')
     )
 )

#process.p = cms.Path(process.zdiElectronSequence)

process.output_step = cms.EndPath(process.RAWoutput)

process.schedule = cms.Schedule(process.output_step)#process.p
