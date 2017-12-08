import FWCore.ParameterSet.Config as cms
import copy

userDataElectrons = cms.EDProducer(
    "ZEEUserData",
    src = cms.InputTag("slimmedElectrons"),
    inputRho = cms.InputTag("fixedGridRhoFastjetAll")
    )

