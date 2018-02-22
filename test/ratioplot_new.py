import os
from sys import argv, stdout, stderr
import ROOT
import sys

ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

#'''
filepath = "plots/newskim_70140/"
filewoskimB = "crab_projects/crab_plots_Zee_woskim_70140/results/ntuple_woskim_eraB_70140.root"
fileskimB = "crab_projects/crab_plots_Zee_newskim_70140/results/ntuple_newskim_eraB_70140.root"
filewoskimC = "crab_projects/crab_plots_Zee_woskim_eraCv1_70140/results/ntuple_woskim_eraC_70140.root"
fileskimC = "crab_projects/crab_plots_Zee_newskim_eraCv1_70140/results/ntuple_newskim_eraC_70140.root"
filewoskimD = "crab_projects/crab_plots_Zee_woskimcut_eraD_70140/results/ntuple_woskim_eraD_70140.root"
fileskimD = "crab_projects/crab_plots_Zee_newskimcut_eraD_70140/results/ntuple_newskim_eraD_70140.root"
filewoskimE = "crab_projects/crab_plots_Zee_woskim_eraE_70140/results/ntuple_woskim_eraE_70140.root"
fileskimE = "crab_projects/crab_plots_Zee_newskim_eraE_70140/results/ntuple_newskim_eraE_70140.root"
filewoskimF = "crab_projects/crab_plots_Zee_woskim_eraF_70140/results/ntuple_woskim_eraF_70140.root"
fileskimF = "crab_projects/crab_plots_Zee_newskim_eraF_70140/results/ntuple_newskim_eraF_70140.root"
filewoskimMC = "crab_projects/crab_plots_Zee_cut_MCv10ext1v2_withoutmatch_70140/results/ntuple_woskim_MCv10ext1v2_womatch_70140.root"
fileskimMC = "crab_projects/crab_plots_Zee_newskimcut_MCv10ext1v2_withoutmatch_70140/results/ntuple_newskim_MCv10ext1v2_womatch_70140.root"
filewoskimMCmatch = "crab_projects/crab_plots_Zee_cut_MCv10ext1v2_70140/results/ntuple_woskim_MCv10ext1v2_70140.root"
fileskimMCmatch = "crab_projects/crab_plots_Zee_newskimcut_MCv10ext1v2_70140/results/ntuple_newskim_MCv10ext1v2_70140.root"
#'''
'''
filepath = "plots/oldskim/"
filewoskimB = "crab_projects/crab_plots_Zee_woskim/results/ntuple_woskim_eraB.root"
fileskimB = "crab_projects/crab_plots_Zee/results/ntuple_skim_eraB.root"
filewoskimC = "crab_projects/crab_plots_Zee_woskim_eraCv1/results/ntuple_woskim_eraC.root"
fileskimC = "crab_projects/crab_plots_Zee_eraCv1/results/ntuple_skim_eraC.root"
filewoskimD = "crab_projects/crab_plots_Zee_woskimcut_eraD/results/ntuple_woskim_eraD.root"
fileskimD = "crab_projects/crab_plots_Zee_cut_eraD/results/ntuple_skim_eraD.root"
filewoskimE = "crab_projects/crab_plots_Zee_woskim_eraE/results/ntuple_woskim_eraE.root"
fileskimE = "crab_projects/crab_plots_Zee_eraE/results/ntuple_skim_eraE.root"
filewoskimF = "crab_projects/crab_plots_Zee_woskim_eraF/results/ntuple_woskim_eraF.root"
fileskimF = "crab_projects/crab_plots_Zee_eraF/results/ntuple_skim_eraF.root"
filewoskimMC = "crab_projects/crab_plots_Zee_cut_MCv10ext1v2_withoutmatch/results/ntuple_woskim_MCv10ext1v2.root"
fileskimMC = "crab_projects/crab_plots_Zee_skimcut_MCv10ext1v2_withoutmatch/results/ntuple_skim_MCv10ext1v2.root"
filewoskimMCmatch = "crab_projects/crab_plots_Zee_cut_MCv10ext1v2/results/ntuple_woskim_MCv10ext1v2.root"
fileskimMCmatch = "crab_projects/crab_plots_Zee_skimcut_MCv10ext1v2/results/ntuple_skim_MCv10ext1v2.root"
'''

try:
    os.stat(filepath)
except:
    os.mkdir(filepath)
 
canvas = ROOT.TCanvas("canvas","canvas",800,800)
legend = ROOT.TLegend(0.7,0.80,0.95,1.0)

filelist = [filewoskimB, fileskimB, filewoskimC, fileskimC, filewoskimD, fileskimD, filewoskimE, fileskimE, filewoskimF, fileskimF, filewoskimMC, fileskimMC, filewoskimMCmatch, fileskimMCmatch]

f1 = ROOT.TFile(filelist[0])
f2 = ROOT.TFile(filelist[1])
f3 = ROOT.TFile(filelist[2])
f4 = ROOT.TFile(filelist[3])
f5 = ROOT.TFile(filelist[4])
f6 = ROOT.TFile(filelist[5])
f7 = ROOT.TFile(filelist[6])
f8 = ROOT.TFile(filelist[7])
f9 = ROOT.TFile(filelist[8])
f10 = ROOT.TFile(filelist[9])
f11 = ROOT.TFile(filelist[10])
f12 = ROOT.TFile(filelist[11])
f13 = ROOT.TFile(filelist[12])
f14 = ROOT.TFile(filelist[13])

gendir = f1.Get('ntupler')
hlist = gendir.GetListOfKeys()
iter = ROOT.TIter(hlist)
for i in iter:
	if i.GetName()=='hits' or i.GetName()=='validhits' or i.GetName()=='en1' or i.GetName()=='en2': continue

	m1 = f1.Get('ntupler/'+i.GetName())
	m2 = f2.Get('ntupler/'+i.GetName())
        m3 = f3.Get('ntupler/'+i.GetName())
        m4 = f4.Get('ntupler/'+i.GetName())
        m5 = f5.Get('ntupler/'+i.GetName())
        m6 = f6.Get('ntupler/'+i.GetName())
        m7 = f7.Get('ntupler/'+i.GetName())
        m8 = f8.Get('ntupler/'+i.GetName())
        mF = f9.Get('ntupler/'+i.GetName())
        mFskim = f10.Get('ntupler/'+i.GetName())
        mMC = f11.Get('ntupler/'+i.GetName())
        mMCskim = f12.Get('ntupler/'+i.GetName())
        mMCmatch = f13.Get('ntupler/'+i.GetName())
        mMCskimmatch = f14.Get('ntupler/'+i.GetName())

	canvas.cd()  # Go back to the main canvas before defining  
	pad1 = ROOT.TPad("pad1", "pad1", 0, 0.0, 1, 1.0)
	pad1.SetBottomMargin(1)  # Upper and lower plot are joined
	pad1.SetGridx()  # Vertical grid
	pad1.SetGridy()  # Horizontal grid
	pad1.Draw()  # Draw the upper pad: pad1
	pad1.cd()  # pad1 becomes the current pad 

	m9 = m2.Clone('m9')
	m9.SetLineColor(3)
	if i.GetName()=='mass':
            m9.GetXaxis().SetTitle("Mass(GeV)")
            m9.SetMinimum(0.0)
            m9.SetMaximum(1.0)
	elif i.GetName()=='pt1' or i.GetName()=='pt2':
            m9.GetXaxis().SetTitle("Pt(GeV)")
            m9.GetXaxis().SetRangeUser(0,100)
            m9.SetMinimum(0.0)
            m9.SetMaximum(1.0)
	elif i.GetName()=='eta1' or i.GetName()=='eta2':
            m9.GetXaxis().SetTitle("eta")
            m9.SetMinimum(0.2)
            m9.SetMaximum(1.0)
        elif i.GetName()=='phi1' or i.GetName()=='phi2':
            m9.GetXaxis().SetTitle("phi")
            m9.SetMinimum(0.2)
            m9.SetMaximum(1.0)


	m9.Sumw2()
	m9.SetStats(0)  # No statistics on lower plot 
	m9.Divide(m1)
        m9.SetMarkerColor(3)
	m9.SetMarkerStyle(20)
        m9.SetMarkerSize(0.5)
	m9.Draw("ep")  # Draw the ratio plot
	m9.SetTitle("")  # Remove the ratio title

	# Y axis ratio plot settings                                                                                        
	m9.GetYaxis().SetTitle("ratio Skim/WithoutSkim")
	m9.GetYaxis().SetNdivisions(505)
	m9.GetYaxis().SetTitleSize(18)
	m9.GetYaxis().SetTitleFont(43)
	m9.GetYaxis().SetTitleOffset(1.7)
	m9.GetYaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
	m9.GetYaxis().SetLabelSize(15)
		
	# X axis ratio plot settings
	m9.GetXaxis().SetTitleSize(20)
	m9.GetXaxis().SetTitleFont(43)
	m9.GetXaxis().SetTitleOffset(1.0)
	m9.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)    
	m9.GetXaxis().SetLabelSize(15)

        m10 = m4.Clone('m10')
        m10.SetLineColor(2)
        m10.Sumw2()
        m10.SetStats(0)
        m10.Divide(m3)
        m10.SetMarkerColor(2)
        m10.SetMarkerStyle(20)
        m10.SetMarkerSize(0.5)
        m10.Draw("ep SAME")
        m10.SetTitle("")

        m11 = m6.Clone('m11')
        m11.SetLineColor(4)
        m11.Sumw2()
        m11.SetStats(0)
        m11.Divide(m5)
        m11.SetMarkerColor(4)
        m11.SetMarkerStyle(20)
        m11.SetMarkerSize(0.5)
        m11.Draw("ep SAME")
        m11.SetTitle("")
	
        m12 = m8.Clone('m12')
        m12.SetLineColor(9)
        m12.Sumw2()
        m12.SetStats(0)
        m12.Divide(m7)
        m12.SetMarkerColor(9)
        m12.SetMarkerStyle(20)
        m12.SetMarkerSize(0.5)
        m12.Draw("ep SAME")
        m12.SetTitle("")

        m13 = mFskim.Clone('m13')
        m13.SetLineColor(6)
        m13.Sumw2()
        m13.SetStats(0)
        m13.Divide(mF)
        m13.SetMarkerColor(6)
        m13.SetMarkerStyle(20)
        m13.SetMarkerSize(0.5)
        m13.Draw("ep SAME")
        m13.SetTitle("")

        m14 = mMCskim.Clone('m14')
        m14.SetLineColor(1)
        m14.Sumw2()
        m14.SetStats(0)
        m14.Divide(mMC)
        m14.SetMarkerColor(1)
        m14.SetMarkerStyle(20)
        m14.SetMarkerSize(0.5)
        m14.Draw("ep SAME")
        m14.SetTitle("")

        m15 = mMCskimmatch.Clone('m15')
        m15.SetLineColor(8)
        m15.Sumw2()
        m15.SetStats(0)
        m15.Divide(mMCmatch)
        m15.SetMarkerColor(8)
        m15.SetMarkerStyle(20)
        m15.SetMarkerSize(0.5)
        m15.Draw("ep SAME")
        m15.SetTitle("")

        legend.AddEntry(m9,"EraB ","lep")
        legend.AddEntry(m10,"EraC ","lep")
        legend.AddEntry(m11,"EraD ","lep")
        legend.AddEntry(m12,"EraE ","lep")
        legend.AddEntry(m13,"EraF ","lep")
        legend.AddEntry(m14,"DYJetsToLL w/o match ","lep")
        legend.AddEntry(m15,"DYJetsToLL with match ","lep")
        legend.Draw()

	if i.GetName()=='mass':
            canvas.SaveAs(filepath+'mass.png')
        elif i.GetName()=='pt1':
            canvas.SaveAs(filepath+'pt1.png')
        elif i.GetName()=='pt2':
            canvas.SaveAs(filepath+'pt2.png')
        elif i.GetName()=='eta1':
            canvas.SaveAs(filepath+'eta1.png')
        elif i.GetName()=='eta2':
            canvas.SaveAs(filepath+'eta2.png')
        elif i.GetName()=='phi1':
            canvas.SaveAs(filepath+'phi1.png')
        elif i.GetName()=='phi2':
            canvas.SaveAs(filepath+'phi2.png')
        canvas.Clear()
        legend.Clear()

