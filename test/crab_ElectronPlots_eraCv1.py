# from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'plots_Zee_eraCv1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runElectronPlots_Skim_eraCv1.py'

config.Data.inputDataset = '/DoubleEG/Run2017C-PromptReco-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'NewJson.txt'
config.Data.runRange = '299368-302029'
#config.Data.totalUnits = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag =  'Zee_ElectronPlots_eraCv1'

config.Site.storageSite = 'T2_CH_CERN'

#all the configuration parameters https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
#all crab commands https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3Commands
