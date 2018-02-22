# from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'plots_Zee_newnewskim_eraD'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runElectronPlots_newnewSkim_eraD.py'

config.Data.inputDataset = '/DoubleEG/Run2017D-PromptReco-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'NewJson.txt'
config.Data.runRange = '302031-302663'
#config.Data.totalUnits = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag =  'Zee_ElectronPlots_newnewskim_eraD'

config.Site.storageSite = 'T2_CH_CERN'

#all the configuration parameters https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
#all crab commands https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3Commands
