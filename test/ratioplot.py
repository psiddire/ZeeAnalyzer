import os
from sys import argv, stdout, stderr
import ROOT
import sys

ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

#filepath = "plots/MCv10ext1v2_withoutmatch_newskim/"
#filewoskim = "crab_projects/crab_plots_Zee_cut_MCv10ext1v2_withoutmatch/results/ntuple_woskim_MCv10ext1v2.root"
#fileskim = "crab_projects/crab_plots_Zee_newskimcut_MCv10ext1v2_withoutmatch/results/ntuple_newskim_MCv10ext1v2.root"

#filepath = "plots/MCv10ext1v1/"
#filewoskim = "crab_projects/crab_plots_Zee_cut_MCv10ext1v1/results/ntuple_woskim_MCv10ext1v1.root"
#fileskim = "crab_projects/crab_plots_Zee_skimcut_MCv10ext1v1/results/ntuple_skim_MCv10ext1v1.root"

filepath = "plots/newnewskim/"
filewoskim = "crab_projects/crab_plots_Zee_woskim_eraF/results/ntuple_woskim_eraF.root"
fileskim = "crab_projects/crab_plots_Zee_newnewskim_eraF/results/ntuple_newnewskim_eraF.root"

#filepath = "plots/eraCv2/"
#filewoskim = "crab_projects/crab_plots_Zee_woskim_eraCv2/results/ntuple_woskim_eraCv2.root"
#fileskim = "crab_projects/crab_plots_Zee_eraCv2/results/ntuple_skim_eraCv2.root"

try:
    os.stat(filepath)
except:
    os.mkdir(filepath)
 
canvas = ROOT.TCanvas("canvas","canvas",800,800)
legend = ROOT.TLegend(0.7,0.75,0.95,0.95)

filelist = [filewoskim, fileskim]

f1 = ROOT.TFile(filelist[0])
f2 = ROOT.TFile(filelist[1])
gendir = f1.Get('ntupler')
hlist = gendir.GetListOfKeys()
n1 = f1.Get('ntupler/mass').GetEntries()
n2 = f2.Get('ntupler/mass').GetEntries()

iter = ROOT.TIter(hlist)
for i in iter:
	if i.GetName()=='hits' or i.GetName()=='validhits' or i.GetName()=='en1' or i.GetName()=='en2': continue

	# Upper plot will be in pad1
	pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
	pad1.SetBottomMargin(1)  # Upper and lower plot are joined
	pad1.SetGridx()  # Vertical grid
	pad1.Draw()  # Draw the upper pad: pad1
	pad1.cd()  # pad1 becomes the current pad 

	m1 = f1.Get('ntupler/'+i.GetName())
	m1.SetLineWidth(2)
	m1.SetLineColor(2)
	if i.GetName()=='mass':
		m1.SetTitle("Invariant Mass of Z->ee")
		m1.GetXaxis().SetTitle("Mass(GeV)")
		m1.GetYaxis().SetTitle("Number of events per 4GeV")
                max1 = m1.GetMaximum()
	elif i.GetName()=='pt1':
                m1.SetTitle("Electron 1 Pt")
                m1.GetXaxis().SetTitle("Pt(GeV)")
		m1.GetYaxis().SetTitle("Number of events per 4GeV")
		m1.GetXaxis().SetRangeUser(0,100) 
	elif i.GetName()=='pt2':
                m1.SetTitle("Electron 2 Pt")
                m1.GetXaxis().SetTitle("Pt(GeV)")
		m1.GetYaxis().SetTitle("Number of events per 4GeV")
		m1.GetXaxis().SetRangeUser(0,100)
	elif i.GetName()=='eta1':
                m1.SetTitle("Electron 1 eta")
                m1.GetXaxis().SetTitle("eta")
		m1.GetYaxis().SetTitle("Number of events")
                m1.SetMinimum(0)
                m1.SetMaximum(1.2*m1.GetMaximum())#(170000) 
	elif i.GetName()=='eta2':
                m1.SetTitle("Electron 2 eta")
                m1.GetXaxis().SetTitle("eta")
		m1.GetYaxis().SetTitle("Number of events")
                m1.SetMinimum(0)
                m1.SetMaximum(1.2*m1.GetMaximum())#(170000)
	elif i.GetName()=='phi1':
                m1.SetTitle("Electron 1 phi")
                m1.GetXaxis().SetTitle("phi")
		m1.GetYaxis().SetTitle("Number of events")
                #m1.GetYaxis().SetRange(0,68000)#int(1.2*m1.GetMaximum()))
                m1.SetMinimum(0.2*m1.GetMinimum())#(38000)
                m1.SetMaximum(1.2*m1.GetMaximum())#(68000)
        elif i.GetName()=='phi2':
                m1.SetTitle("Electron 2 phi")
                m1.GetXaxis().SetTitle("phi")
		m1.GetYaxis().SetTitle("Number of events")
                #m1.GetYaxis().SetRange(0,68000)#int(1.2*m1.GetMaximum()))
                m1.SetMinimum(0.2*m1.GetMinimum())#(38000)
                m1.SetMaximum(1.2*m1.GetMaximum())#(68000)
        m1.GetYaxis().SetTitleSize(18)
	m1.GetYaxis().SetTitleFont(43)
	m1.GetYaxis().SetTitleOffset(1.7)
	m1.Draw('hist')
		
	m2 = f2.Get('ntupler/'+i.GetName())
	m2.SetLineWidth(2)
	m2.SetLineColor(3)
        if i.GetName()=='mass':
            max2 = m2.GetMaximum()
	m2.Draw('hist SAME')

	legend.AddEntry(m1,"Without Skim "+str(n1),"l")
	legend.AddEntry(m2,"With Skim "+str(n2),"l")
	legend.Draw()

        # lower plot will be in pad
	canvas.cd()  # Go back to the main canvas before defining 
	pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
	pad2.SetTopMargin(0)
	pad2.SetBottomMargin(0.2)
	pad2.SetGridx()  # vertical grid
	pad2.Draw()
	pad2.cd() # pad2 becomes the current pad    

	m3 = m2.Clone('m3')
	m3.SetLineColor(1)
	if i.GetName()=='phi1' or i.GetName()=='phi2':
            m3.SetMinimum(0.0) # Define Y ..
            m3.SetMaximum(1.0)
	elif i.GetName()=='pt1' or i.GetName()=='pt2':
            m3.SetMinimum(0.0)
            m3.SetMaximum(1.5)
            m3.GetXaxis().SetRangeUser(0,100)
        else:
            m3.SetMinimum(0.0) # Define Y ..   
            m3.SetMaximum(1.0)
	m3.Sumw2()
	m3.SetStats(0)  # No statistics on lower plot 
	m3.Divide(m1)
	m3.SetMarkerStyle(21)
	m3.Draw("ep")  # Draw the ratio plot
	m3.SetTitle("")  # Remove the ratio title

	# Y axis ratio plot settings                                                                                        
	m3.GetYaxis().SetTitle("ratio Skim/WithoutSkim")
	m3.GetYaxis().SetNdivisions(505)
	m3.GetYaxis().SetTitleSize(18)
	m3.GetYaxis().SetTitleFont(43)
	m3.GetYaxis().SetTitleOffset(1.7)
	m3.GetYaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
	m3.GetYaxis().SetLabelSize(15)
		
	# X axis ratio plot settings
	m3.GetXaxis().SetTitleSize(20)
	m3.GetXaxis().SetTitleFont(43)
	m3.GetXaxis().SetTitleOffset(4.)
	m3.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)    
	m3.GetXaxis().SetLabelSize(15)
	
	if i.GetName()=='mass':
            print "woskim max: ", max1, " skim max: ", max2, " Peak Efficiency: ", max2/max1
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
