#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// system include files                                                                                                               
#include <vector>
#include <memory>

// user include files                                                                                                                 
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/PatCandidates/interface/VIDCutFlowResult.h"

#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"
#include "TLorentzVector.h"
#include "Math/VectorUtil.h"

using namespace edm;
using namespace std;
using namespace reco;
using namespace isodeposit;
//using namespace pat;

class ZEEUserData : public edm::EDProducer {
public:
  ZEEUserData( const edm::ParameterSet & );
private:
  void produce( edm::Event &, const edm::EventSetup & ) override;

  EDGetTokenT<vector<pat::Electron> > srcToken_;
  //EDGetToken srcToken_;
  double rho_;
  EDGetTokenT<double> rhoToken_;
};

ZEEUserData::ZEEUserData( const ParameterSet & cfg ){
  //  srcToken_ = consumes<edm::View<pat::Electron> >(cfg.getParameter<InputTag>("src"));
  srcToken_ = consumes<vector<pat::Electron> >(cfg.getParameter<InputTag>("src"));
  rhoToken_ = consumes<double>(cfg.getParameter<edm::InputTag>("inputRho"));
  }

void ZEEUserData::produce( Event & evt, const EventSetup & ) {
  Handle<vector<pat::Electron> > electrons;
  evt.getByToken(srcToken_,electrons);

  double rho=0;
  Handle< double > rhoH;
  evt.getByToken(rhoToken_,rhoH);
  rho = *rhoH;

  unique_ptr<vector<pat::Electron> > electronColl( new vector<pat::Electron> (*electrons) );
  for (unsigned int i = 0; i < electronColl->size(); ++i){
    pat::Electron & e = (*electronColl)[i];
    e.addUserFloat("rho", rho); 
  }

  evt.put(std::move(electronColl));
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( ZEEUserData );
