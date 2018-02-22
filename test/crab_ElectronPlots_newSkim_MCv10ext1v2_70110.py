from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'plots_Zee_newskimcut_MCv10ext1v2_70110'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runElectronPlots_newSkim_MCv10ext1v2.py'

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v2/MINIAODSIM'
#/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1/MINIAODSIM
#/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1/MINIAODSIM
#/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v2/MINIAODSIM
#/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v7-v1/MINIAODSIM
#/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_Candidate_forECALStudies_ext1-v1/MINIAODSIM
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'Zee_ElectronPlots_newskimcut_MCv10ext1v2_70110'

config.Site.storageSite = 'T2_CH_CERN'
