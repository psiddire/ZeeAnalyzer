import os
from sys import argv, stdout, stderr
import ROOT
import sys

ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

#'''
s = "eraB"
filepath = "plots/comp_"+s+"/"
filewoskim = "crab_projects/crab_plots_Zee_woskim/results/ntuple_woskim_"+s+".root"
fileskim = "crab_projects/crab_plots_Zee/results/ntuple_skim_"+s+".root"
filenewskim = "crab_projects/crab_plots_Zee_newskim/results/ntuple_newskim_"+s+".root"
filenewnewskim = "crab_projects/crab_plots_Zee_newnewskim/results/ntuple_newnewskim_"+s+".root"
#filenewnewskim70110 = "crab_projects/crab_plots_Zee_newnewskim_eraF_70110/results/ntuple_newnewskim_eraF_70110.root"
#'''

try:
    os.stat(filepath)
except:
    os.mkdir(filepath)
 
canvas = ROOT.TCanvas("canvas","canvas",800,800)
legend = ROOT.TLegend(0.7,0.80,0.95,1.0)

filelist = [filewoskim, fileskim, filenewskim, filenewnewskim]

f1 = ROOT.TFile(filelist[0])
f2 = ROOT.TFile(filelist[1])
f3 = ROOT.TFile(filelist[2])
f4 = ROOT.TFile(filelist[3])

gendir = f1.Get('ntupler')
hlist = gendir.GetListOfKeys()
iter = ROOT.TIter(hlist)
for i in iter:
	if i.GetName()=='hits' or i.GetName()=='validhits' or i.GetName()=='en1' or i.GetName()=='en2' or i.GetName()=='mass' or i.GetName()=='pt1' or i.GetName()=='pt2': continue

	m1 = f1.Get('ntupler/'+i.GetName())
	m2 = f2.Get('ntupler/'+i.GetName())
        m3 = f3.Get('ntupler/'+i.GetName())
        m4 = f4.Get('ntupler/'+i.GetName())

	canvas.cd()  # Go back to the main canvas before defining  
	pad1 = ROOT.TPad("pad1", "pad1", 0, 0.0, 1, 1.0)
	pad1.SetBottomMargin(1)  # Upper and lower plot are joined
	pad1.SetGridx()  # Vertical grid
	pad1.SetGridy()  # Horizontal grid
	pad1.Draw()  # Draw the upper pad: pad1
	pad1.cd()  # pad1 becomes the current pad 

	m9 = m2.Clone('m9')
	m9.SetLineColor(3)
	if i.GetName()=='eta1' or i.GetName()=='eta2':
            m9.GetXaxis().SetTitle("eta")
            m9.SetMinimum(0.2)
            m9.SetMaximum(0.8)
        elif i.GetName()=='phi1' or i.GetName()=='phi2':
            m9.GetXaxis().SetTitle("phi")
            m9.SetMinimum(0.2)
            m9.SetMaximum(0.8)


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

        m10 = m3.Clone('m10')
        m10.SetLineColor(2)
        m10.Sumw2()
        m10.SetStats(0)
        m10.Divide(m1)
        m10.SetMarkerColor(2)
        m10.SetMarkerStyle(20)
        m10.SetMarkerSize(0.5)
        m10.Draw("ep SAME")
        m10.SetTitle("")

        m11 = m4.Clone('m11')
        m11.SetLineColor(4)
        m11.Sumw2()
        m11.SetStats(0)
        m11.Divide(m1)
        m11.SetMarkerColor(4)
        m11.SetMarkerStyle(20)
        m11.SetMarkerSize(0.5)
        m11.Draw("ep SAME")
        m11.SetTitle("")
	
        legend.AddEntry(m9,"Old Skim","lep")
        legend.AddEntry(m10,"Summer16 Skim","lep")
        legend.AddEntry(m11,"Latest Skim","lep")
        legend.Draw()

        if i.GetName()=='eta1':
            canvas.SaveAs(filepath+'eta1.png')
        elif i.GetName()=='eta2':
            canvas.SaveAs(filepath+'eta2.png')
        elif i.GetName()=='phi1':
            canvas.SaveAs(filepath+'phi1.png')
        elif i.GetName()=='phi2':
            canvas.SaveAs(filepath+'phi2.png')
        canvas.Clear()
        legend.Clear()

