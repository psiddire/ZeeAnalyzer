import FWCore.ParameterSet.Config as cms

process = cms.Process("TestElectrons")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_Candidate_forECALStudies', '')

# input
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

inputFilesMing = cms.untracked.vstring(
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_1.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_10.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_11.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_13.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_14.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_16.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_17.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_18.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_19.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_2.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_21.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_22.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_24.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_25.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_26.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_27.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_28.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_29.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_30.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_32.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_33.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_35.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_37.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_38.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_39.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_4.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_40.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_41.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_42.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_43.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_44.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_45.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_46.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_5.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_50.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_51.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_52.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_53.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_54.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_56.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_57.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_58.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_59.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_6.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_60.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_61.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_62.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_63.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_64.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_65.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_66.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_67.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_68.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_69.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_7.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_71.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_72.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_73.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_74.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_75.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_76.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_77.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_78.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_79.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_8.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_80.root',
    '/store/group/dpg_ecal/comm_ecal/test/ming/job_Zee_NoPU_RECO_940pre2_v1/Zee13TeV_940pre2/Zee_NoPU_RECO_940pre2_v1/171019_132414/0000/step3_RAW2DIGI_L1Reco_RECO_EI_PAT_9.root'
    )    

inputFiles = inputFilesMing
outputFile = "electron_ntuple.root"
process.source = cms.Source ("PoolSource", fileNames = inputFiles )                             

process.ntupler = cms.EDAnalyzer(
    'ElectronPlots',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    genEventInfoProduct = cms.InputTag('generator'),
    electrons    = cms.InputTag("gedGsfElectrons"),
    genParticles = cms.InputTag("genParticles"),
    vertices     = cms.InputTag("offlinePrimaryVertices"),
    conversions  = cms.InputTag('allConversions'),
    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( outputFile )
                                   )

process.p = cms.Path(process.ntupler)
