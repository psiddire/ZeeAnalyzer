void ratioplot() {
  //TH1F *h1 = new TH1F("h1", "h1", 25, 0, 100);
  //TH1F *h2 = new TH1F("h2", "h2", 25, 0, 100);
  //  h1->FillRandom("gaus");
  //  h2->FillRandom("gaus");
  TFile *f1 = new TFile("crab_projects/crab_plots_Zee_woskimcut_eraD/results/ntuple_woskim_eraD.root");
  f1->ls();
  TFile *f2 = new TFile("crab_projects/crab_plots_Zee_cut_eraD/results/ntuple_skim_eraD.root");
  f2->ls();
  /*
  const char *a[9];
  a[0] = "pt1";
  a[1] = "pt2";
  a[2] = "eta1";
  a[3] = "eta2";
  a[4] = "phi1";
  a[5] = "phi2";
  a[6] = "mass";
  a[7] = "ntupler/";
  a[8] = "plots/";
  char b[7][20];
  char d[7][20];
  */
  //for(int i = 0; i < 7; i++){
  //cout << i << b[i] << endl;
  //strcat(b[i],a[7]);
  //cout << i << b[i] << endl;
  //strcat(b[i],a[i]);  
  //cout << i << b[i] << endl;
  TH1F *h1 = (TH1F*)f1->Get("ntupler/phi2");
  TH1F *h2 = (TH1F*)f2->Get("ntupler/phi2");
  //cout << "Got Histos" << endl;

  // Define the Canvas
  TCanvas *c = new TCanvas("c", "canvas", 800, 800);

  // Upper plot will be in pad1
  TPad *pad1 = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
  pad1->SetBottomMargin(0); // Upper and lower plot are joined
  pad1->SetGridx();         // Vertical grid
  pad1->Draw();             // Draw the upper pad: pad1
  pad1->cd();               // pad1 becomes the current pad
  //h1->SetStats(0);          // No statistics on upper plot
  h1->Draw();               // Draw h1
  h2->Draw("same");         // Draw h2 on top of h1

  // Do not draw the Y axis label on the upper plot and redraw a small
  // axis instead, in order to avoid the first label (0) to be clipped.
  h1->GetYaxis()->SetLabelSize(0.);
  TGaxis *axis = new TGaxis( -5, 20, -5, 220, 20,220,510,"");
  axis->SetLabelFont(43); // Absolute font size in pixel (precision 3)
  axis->SetLabelSize(15);
  axis->Draw();

  // lower plot will be in pad
  c->cd();          // Go back to the main canvas before defining pad2
  TPad *pad2 = new TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
  pad2->SetTopMargin(0);
  pad2->SetBottomMargin(0.2);
  pad2->SetGridx(); // vertical grid
  pad2->Draw();
  pad2->cd();       // pad2 becomes the current pad

  // Define the ratio plot
  TH1F *h3 = (TH1F*)h2->Clone("h3");
  h3->SetLineColor(kBlack);
  h3->SetMinimum(0.0);  // Define Y ..
  h3->SetMaximum(1.0); // .. range
  h3->Sumw2();
  h3->SetStats(0);      // No statistics on lower plot
  h3->Divide(h1);
  h3->SetMarkerStyle(21);
  h3->Draw("ep");       // Draw the ratio plot

  // h1 settings
  h1->SetLineColor(kBlue+1);
  h1->SetLineWidth(2);

  // Y axis h1 plot settings
  h1->GetYaxis()->SetTitleSize(20);
  h1->GetYaxis()->SetTitleFont(43);
  h1->GetYaxis()->SetTitleOffset(1.55);

  // h2 settings
  h2->SetLineColor(kRed);
  h2->SetLineWidth(2);

  // Ratio plot (h3) settings
  h3->SetTitle(""); // Remove the ratio title

  // Y axis ratio plot settings
  h3->GetYaxis()->SetTitle("ratio h2/h1 ");
  h3->GetYaxis()->SetNdivisions(505);
  h3->GetYaxis()->SetTitleSize(20);
  h3->GetYaxis()->SetTitleFont(43);
  h3->GetYaxis()->SetTitleOffset(1.55);
  h3->GetYaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
  h3->GetYaxis()->SetLabelSize(15);

  // X axis ratio plot settings
  h3->GetXaxis()->SetTitleSize(20);
  h3->GetXaxis()->SetTitleFont(43);
  h3->GetXaxis()->SetTitleOffset(4.);
  h3->GetXaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
  h3->GetXaxis()->SetLabelSize(15);

  //strcat(d[i],a[8]);
  //strcat(d[i],a[i]);
  //strcat(str1,a[i]);
  //strcat(d[i],".png");
  //cout << "plot" << " " << d[i] << endl;

  c->SaveAs("plots/oldskim_phi2.png");
  /*
  if (c) {
    c->Close();
    gSystem->ProcessEvents();
  }

  delete h1;
  delete h2;
  delete h3;
  
  }*/
}
