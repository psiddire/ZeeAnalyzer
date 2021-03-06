// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/PatCandidates/interface/VIDCutFlowResult.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"
#include "TLorentzVector.h"
#include "Math/VectorUtil.h"

class ElectronPlots : public edm::EDAnalyzer {
public:
  explicit ElectronPlots(const edm::ParameterSet&);
  ~ElectronPlots();
  
  enum ElectronMatchType {UNMATCHED = 0, 
			  TRUE_PROMPT_ELECTRON = 2, 
			  TRUE_ELECTRON_FROM_Z = 1,
			  TRUE_NON_PROMPT_ELECTRON = 3}; // The last does not include tau parents
  
private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  
  int matchToTruth(const edm::Ptr<pat::Electron> el, 
		   const edm::Handle<edm::View<reco::GenParticle>>  &prunedGenParticles);
  
  void findFirstNonElectronMother(const reco::Candidate *particle,
				  int &ancestorPID, int &ancestorStatus);
  
  // ----------member data ---------------------------
  //int nEvents=0;
  bool isMC=false; 
  bool flag=false; 
  // Data members
  edm::EDGetTokenT<double> rhoToken_;
  edm::EDGetTokenT<reco::BeamSpot> beamSpotToken_;
  edm::EDGetTokenT<GenEventInfoProduct> genEventInfoProduct_;
  //edm::EDGetTokenT<edm::View<reco::GsfElectron> > electronsToken_;  
  edm::EDGetToken electronsToken_;
  edm::EDGetTokenT<edm::View<reco::GenParticle> > genParticlesToken_;
  edm::EDGetTokenT<reco::VertexCollection> vtxToken_;
  edm::EDGetTokenT<reco::ConversionCollection> conversionsToken_;

  // Histos
  TH1F *h_eta1, *h_phi1, *h_pt1, *h_en1, *h_eta2, *h_phi2, *h_pt2, *h_en2, *h_hits, *h_validhits, *h_mass;
};

ElectronPlots::ElectronPlots(const edm::ParameterSet& iConfig) {

  isMC=iConfig.getParameter<bool>("isMC");
  
  rhoToken_ = consumes<double>
    (iConfig.getParameter <edm::InputTag>
     ("inputLeptonRho"));
  // double "fixedGridRhoFastjetAll" "" "RECO" 

  beamSpotToken_ = consumes<reco::BeamSpot>
    (iConfig.getParameter <edm::InputTag>
     ("beamSpot"));
  // reco::BeamSpot "offlineBeamSpot"
  
  //electronsToken_ = mayConsume<edm::View<reco::GsfElectron> >
  // (iConfig.getParameter<edm::InputTag>                                                                                               
  // ("electrons"));        

  electronsToken_ = mayConsume<edm::View<pat::Electron> >                                           
    (iConfig.getParameter<edm::InputTag>                                                                
     ("electrons"));
  // vector<pat::Electron> "slimmedElectrons"
  
  if (isMC==true){
    genParticlesToken_ = mayConsume<edm::View<reco::GenParticle> >
    (iConfig.getParameter<edm::InputTag>
     ("genParticles"));
  }

  edm::Service<TFileService> fs;
  h_eta1 = fs->make<TH1F>("eta1", "eta1", 100,-2.5,2.5);
  h_phi1 = fs->make<TH1F>("phi1", "phi1", 100,-2.5,2.5);
  h_pt1 = fs->make<TH1F>("pt1", "pt1", 50,0.,200.);
  h_en1 = fs->make<TH1F>("en1", "en1", 50,0.,200.);
  h_eta2 = fs->make<TH1F>("eta2", "eta2", 100,-2.5,2.5);
  h_phi2 = fs->make<TH1F>("phi2", "phi2", 100,-2.5,2.5);
  h_pt2 = fs->make<TH1F>("pt2", "pt2", 50,0.,200.);
  h_en2 = fs->make<TH1F>("en2", "en2", 50,0.,200.);
  h_mass = fs->make<TH1F>("mass", "mass", 50,0.,200.);
  h_hits = fs->make<TH1F>("hits", "hits", 30,0.,30.);
  h_validhits = fs->make<TH1F>("validhits", "validhits", 30,0.,30.);
}


ElectronPlots::~ElectronPlots() { }

void ElectronPlots::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

  using namespace std;
  using namespace edm;
  using namespace reco;

  // Get the beam spot
  edm::Handle<reco::BeamSpot> theBeamSpot;
  iEvent.getByToken(beamSpotToken_,theBeamSpot);  
  
  // Get electrons
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByToken(electronsToken_, electrons);
  //edm::Handle<edm::View<reco::GsfElectron> > electrons;                                                                             //iEvent.getByToken(electronsToken_, electrons);

  double rho=0;
  edm::Handle< double > rhoH;
  iEvent.getByToken(rhoToken_,rhoH);
  rho = *rhoH;
  
  //nEvents+=1;
  std::cout << iEvent.id().event() << " " << rho << " " << *(rhoH.product()) <<  std::endl;
  
  if (isMC==true){
  // Get MC Collection
    Handle<edm::View<reco::GenParticle> > genParticles;
    iEvent.getByToken(genParticlesToken_,genParticles);

  // Loop over electrons
    for (size_t i = 0; i < electrons->size(); ++i){
      const auto el1 = electrons->ptrAt(i);
      for (size_t j = i+1; j < electrons->size(); ++j){
	const auto el2 = electrons->ptrAt(j);

        // acceptance
	if( el1->pt() < 5 or el2->pt() < 5) continue;
	if( fabs(el1->eta()) > 2.5 or fabs(el2->eta()) > 2.5) continue;
    
	TLorentzVector pfz;
	pfz.SetPxPyPzE(el1->px()+el2->px(),el1->py()+el2->py(),el1->pz()+el2->pz(),el1->energy()+el2->energy());
        
	if( pfz.M() < 40 or pfz.M() > 140) continue;
	if ( el1->pt() < 20 or el2->pt() < 10 ) continue;
	
        //if ( matchToTruth( el1, genParticles)!=1 or matchToTruth( el2, genParticles)!=1) continue;
        // Fill if above cuts are met
	h_mass -> Fill(pfz.M());
	h_eta1 -> Fill(el1->eta());
	h_phi1 -> Fill(el1->phi());
	h_pt1 -> Fill(el1->pt());
	h_en1 -> Fill(el1->energy());
	h_eta2 -> Fill(el2->eta());
	h_phi2 -> Fill(el2->phi());
	h_pt2 -> Fill(el2->pt());
	h_en2 -> Fill(el2->energy());
	h_hits -> Fill(el1->gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::TRACK_HITS));
	h_validhits -> Fill(el1->gsfTrack()->hitPattern().numberOfValidHits());
	flag = true;
	//cout <<__LINE__<< " " << iEvent.id().event() << " " << el1->pt() << el2->pt() << matchToTruth( el1, genParticles) << matchToTruth( el2, genParticles) << endl;
	break;
      }
      if (flag == true){ 
	flag = false;
	break;
      }
    } // Loop over electrons
  }
  else{
    // Data
    const auto el1 = electrons->ptrAt(0);
    const auto el2 = electrons->ptrAt(1);
      
    TLorentzVector pfz;
    pfz.SetPxPyPzE(el1->px()+el2->px(),el1->py()+el2->py(),el1->pz()+el2->pz(),el1->energy()+el2->energy());

    if (fabs(el1->eta()) < 2.5 and fabs(el2->eta()) < 2.5 and pfz.M() > 70 and pfz.M() < 110 and el1->pt() > 20 and el2->pt() > 10){//pfz.M() < 110
      // Fill if above cuts are met                                                                                            
      h_mass -> Fill(pfz.M());
      h_eta1 -> Fill(el1->eta());
      h_phi1 -> Fill(el1->phi());
      h_pt1 -> Fill(el1->pt());
      h_en1 -> Fill(el1->energy());
      h_eta2 -> Fill(el2->eta());
      h_phi2 -> Fill(el2->phi());
      h_pt2 -> Fill(el2->pt());
      h_en2 -> Fill(el2->energy());
      h_hits -> Fill(el1->gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::TRACK_HITS));
      h_validhits -> Fill(el1->gsfTrack()->hitPattern().numberOfValidHits());
    }
  }
}


void ElectronPlots::beginJob() { }

void ElectronPlots::endJob() { }

int ElectronPlots::matchToTruth(const edm::Ptr<pat::Electron> el, const edm::Handle<edm::View<reco::GenParticle>> &prunedGenParticles){

  // Find the closest status 1 gen electron to the reco electron
  double dR = 999;
  const reco::Candidate *closestElectron = 0;
  for(size_t i=0; i<prunedGenParticles->size();i++){
    const reco::Candidate *particle = &(*prunedGenParticles)[i];
    // Drop everything that is not electron or not status 1
    if( abs(particle->pdgId()) != 11 || particle->status() != 1 )
      continue;
    //
    double dRtmp = ROOT::Math::VectorUtil::DeltaR( el->p4(), particle->p4() );
    if( dRtmp < dR ){
      dR = dRtmp;
      closestElectron = particle;
    }
  }
  // See if the closest electron (if it exists) is close enough.
  // If not, no match found.
  if( !(closestElectron != 0 && dR < 0.1) ) {
    return UNMATCHED;
  }

  // 
  int ancestorPID = -999; 
  int ancestorStatus = -999;
  findFirstNonElectronMother(closestElectron, ancestorPID, ancestorStatus);
  
  if( ancestorPID == -999 && ancestorStatus == -999 ){
    // No non-electron parent??? This should never happen.
    // Complain.
    printf("ElectronNtupler: ERROR! Electron does not apper to have a non-electron parent\n");
    return UNMATCHED;
  }
  if( abs(ancestorPID) > 50 )// && ancestorStatus == 2 )
    return TRUE_NON_PROMPT_ELECTRON;

  if( abs(ancestorPID) == 23 && ancestorStatus == 22 )
    return TRUE_ELECTRON_FROM_Z;

  // What remains is true prompt electrons
  return TRUE_PROMPT_ELECTRON;
}

void ElectronPlots::findFirstNonElectronMother(const reco::Candidate *particle,
						 int &ancestorPID, int &ancestorStatus){

  if( particle == 0 ){
    printf("ElectronNtupler: ERROR! null candidate pointer, this should never happen\n");
    return;
  }

  // Is this the first non-electron parent? If yes, return, otherwise go deeper into recursion
  if( abs(particle->pdgId()) == 11 || (abs(particle->pdgId()) == 23 && (particle->status())!=22)){
    //std::cout << "Electron Ancestor " << particle->mother(0)->pdgId() << " Status " << particle->mother(0)->status() <<std::endl; 
    findFirstNonElectronMother(particle->mother(0), ancestorPID, ancestorStatus);
  }
  else{
    ancestorPID = particle->pdgId();
    ancestorStatus = particle->status();
    //std::cout << "Particle Id " << ancestorPID << " Status " << ancestorStatus <<std::endl;
  }
  return;
}

//define this as a plug-in
DEFINE_FWK_MODULE(ElectronPlots);
