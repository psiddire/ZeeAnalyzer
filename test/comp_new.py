import os
from sys import argv, stdout, stderr
import ROOT
import sys

ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

filepath = "plots/comp_alleras/"
filewoskim0 = "crab_projects/crab_plots_Zee_woskim/results/ntuple_woskim_eraB.root"
fileskim0 = "crab_projects/crab_plots_Zee/results/ntuple_skim_eraB.root"
filenewskim0 = "crab_projects/crab_plots_Zee_newskim/results/ntuple_newskim_eraB.root"
filenewnewskim0 = "crab_projects/crab_plots_Zee_newnewskim/results/ntuple_newnewskim_eraB.root"
filewoskim1 = "crab_projects/crab_plots_Zee_woskim_eraCv1/results/ntuple_woskim_eraC.root"
fileskim1 = "crab_projects/crab_plots_Zee_eraCv1/results/ntuple_skim_eraC.root"
filenewskim1 = "crab_projects/crab_plots_Zee_newskim_eraCv1/results/ntuple_newskim_eraC.root"
filenewnewskim1 = "crab_projects/crab_plots_Zee_newnewskim_eraCv1/results/ntuple_newnewskim_eraC.root"
filewoskim2 = "crab_projects/crab_plots_Zee_woskim_eraD/results/ntuple_woskim_eraD.root"
fileskim2 = "crab_projects/crab_plots_Zee_eraD/results/ntuple_skim_eraD.root"
filenewskim2 = "crab_projects/crab_plots_Zee_newskim_eraD/results/ntuple_newskim_eraD.root"
filenewnewskim2 = "crab_projects/crab_plots_Zee_newnewskim_eraD/results/ntuple_newnewskim_eraD.root"
filewoskim3 = "crab_projects/crab_plots_Zee_woskim_eraE/results/ntuple_woskim_eraE.root"
fileskim3 = "crab_projects/crab_plots_Zee_eraE/results/ntuple_skim_eraE.root"
filenewskim3 = "crab_projects/crab_plots_Zee_newskim_eraE/results/ntuple_newskim_eraE.root"
filenewnewskim3 = "crab_projects/crab_plots_Zee_newnewskim_eraE/results/ntuple_newnewskim_eraE.root"
filewoskim4 = "crab_projects/crab_plots_Zee_woskim_eraF/results/ntuple_woskim_eraF.root"
fileskim4 = "crab_projects/crab_plots_Zee_eraF/results/ntuple_skim_eraF.root"
filenewskim4 = "crab_projects/crab_plots_Zee_newskim_eraF/results/ntuple_newskim_eraF.root"
filenewnewskim4 = "crab_projects/crab_plots_Zee_newnewskim_eraF/results/ntuple_newnewskim_eraF.root"



try:
    os.stat(filepath)
except:
    os.mkdir(filepath)
 
canvas = ROOT.TCanvas("canvas","canvas",800,800)
legend = ROOT.TLegend(0.7,0.80,0.95,1.0)

filelist = [filewoskim0, fileskim0, filenewskim0, filenewnewskim0, filewoskim1, fileskim1, filenewskim1, filenewnewskim1, filewoskim2, fileskim2, filenewskim2, filenewnewskim2, filewoskim3, fileskim3, filenewskim3, filenewnewskim3, filewoskim4, fileskim4, filenewskim4, filenewnewskim4]

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
f15 = ROOT.TFile(filelist[14])
f16 = ROOT.TFile(filelist[15])
f17 = ROOT.TFile(filelist[16])
f18 = ROOT.TFile(filelist[17])
f19 = ROOT.TFile(filelist[18])
f20 = ROOT.TFile(filelist[19])

gendir = f1.Get('ntupler')
hlist = gendir.GetListOfKeys()
iter = ROOT.TIter(hlist)
for i in iter:
	if i.GetName()=='hits' or i.GetName()=='validhits' or i.GetName()=='en1' or i.GetName()=='en2' or i.GetName()=='mass' or i.GetName()=='pt1' or i.GetName()=='pt2': continue

	m1 = f1.Get('ntupler/'+i.GetName())
	m2 = f2.Get('ntupler/'+i.GetName())
        m3 = f3.Get('ntupler/'+i.GetName())
        m4 = f4.Get('ntupler/'+i.GetName())
        m5 = f5.Get('ntupler/'+i.GetName())
        m6 = f6.Get('ntupler/'+i.GetName())
        m7 = f7.Get('ntupler/'+i.GetName())
        m8 = f8.Get('ntupler/'+i.GetName())
        m9 = f9.Get('ntupler/'+i.GetName())
        m10 = f10.Get('ntupler/'+i.GetName())
        m11 = f11.Get('ntupler/'+i.GetName())
        m12 = f12.Get('ntupler/'+i.GetName())
        m13 = f13.Get('ntupler/'+i.GetName())
        m14 = f14.Get('ntupler/'+i.GetName())
        m15 = f15.Get('ntupler/'+i.GetName())
        m16 = f16.Get('ntupler/'+i.GetName())
        m17 = f17.Get('ntupler/'+i.GetName())
        m18 = f18.Get('ntupler/'+i.GetName())
        m19 = f19.Get('ntupler/'+i.GetName())
        m20 = f20.Get('ntupler/'+i.GetName())

	canvas.cd()  # Go back to the main canvas before defining  
	pad1 = ROOT.TPad("pad1", "pad1", 0, 0.0, 1, 1.0)
	pad1.SetBottomMargin(1)  # Upper and lower plot are joined
	pad1.SetGridx()  # Vertical grid
	pad1.SetGridy()  # Horizontal grid
	pad1.Draw()  # Draw the upper pad: pad1
	pad1.cd()  # pad1 becomes the current pad 

	ma = m2.Clone('ma')
	ma.SetLineColor(3)
	if i.GetName()=='eta1' or i.GetName()=='eta2':
            ma.GetXaxis().SetTitle("eta")
            ma.SetMinimum(0.0)
            ma.SetMaximum(1.0)
        elif i.GetName()=='phi1' or i.GetName()=='phi2':
            ma.GetXaxis().SetTitle("phi")
            ma.SetMinimum(0.0)
            ma.SetMaximum(1.0)


	ma.Sumw2()
	ma.SetStats(0)  # No statistics on lower plot 
	ma.Divide(m1)
        ma.SetMarkerColor(3)
	ma.SetMarkerStyle(20)
        ma.SetMarkerSize(0.5)
	ma.Draw("ep")  # Draw the ratio plot
	ma.SetTitle("")  # Remove the ratio title

	# Y axis ratio plot settings                                                                                        
	ma.GetYaxis().SetTitle("ratio Skim/WithoutSkim")
	ma.GetYaxis().SetNdivisions(505)
	ma.GetYaxis().SetTitleSize(18)
	ma.GetYaxis().SetTitleFont(43)
	ma.GetYaxis().SetTitleOffset(1.7)
	ma.GetYaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
	ma.GetYaxis().SetLabelSize(15)
		
	# X axis ratio plot settings
	ma.GetXaxis().SetTitleSize(20)
	ma.GetXaxis().SetTitleFont(43)
	ma.GetXaxis().SetTitleOffset(1.0)
	ma.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)    
	ma.GetXaxis().SetLabelSize(15)

        mb = m3.Clone('mb')
        mb.SetLineColor(2)
        mb.Sumw2()
        mb.SetStats(0)
        mb.Divide(m1)
        mb.SetMarkerColor(2)
        mb.SetMarkerStyle(20)
        mb.SetMarkerSize(0.5)
        mb.Draw("ep SAME")
        mb.SetTitle("")

        mc = m4.Clone('mc')
        mc.SetLineColor(4)
        mc.Sumw2()
        mc.SetStats(0)
        mc.Divide(m1)
        mc.SetMarkerColor(4)
        mc.SetMarkerStyle(20)
        mc.SetMarkerSize(0.5)
        mc.Draw("ep SAME")
        mc.SetTitle("")

        md = m6.Clone('md')
        md.SetLineColor(5)
        md.Sumw2()
        md.SetStats(0)
        md.Divide(m5)
        md.SetMarkerColor(5)
        md.SetMarkerStyle(20)
        md.SetMarkerSize(0.5)
        md.Draw("ep SAME")
        md.SetTitle("")

        me = m7.Clone('me')
        me.SetLineColor(6)
        me.Sumw2()
        me.SetStats(0)
        me.Divide(m5)
        me.SetMarkerColor(6)
        me.SetMarkerStyle(20)
        me.SetMarkerSize(0.5)
        me.Draw("ep SAME")
        me.SetTitle("")

        mf = m8.Clone('mf')
        mf.SetLineColor(7)
        mf.Sumw2()
        mf.SetStats(0)
        mf.Divide(m5)
        mf.SetMarkerColor(7)
        mf.SetMarkerStyle(20)
        mf.SetMarkerSize(0.5)
        mf.Draw("ep SAME")
        mf.SetTitle("")

        mg = m10.Clone('mg')
        mg.SetLineColor(8)
        mg.Sumw2()
        mg.SetStats(0)
        mg.Divide(m9)
        mg.SetMarkerColor(8)
        mg.SetMarkerStyle(20)
        mg.SetMarkerSize(0.5)
        mg.Draw("ep SAME")
        mg.SetTitle("")

        mh = m11.Clone('mh')
        mh.SetLineColor(9)
        mh.Sumw2()
        mh.SetStats(0)
        mh.Divide(m9)
        mh.SetMarkerColor(9)
        mh.SetMarkerStyle(20)
        mh.SetMarkerSize(0.5)
        mh.Draw("ep SAME")
        mh.SetTitle("")

        mi = m12.Clone('mi')
        mi.SetLineColor(20)
        mi.Sumw2()
        mi.SetStats(0)
        mi.Divide(m9)
        mi.SetMarkerColor(20)
        mi.SetMarkerStyle(20)
        mi.SetMarkerSize(0.5)
        mi.Draw("ep SAME")
        mi.SetTitle("")

        mj = m14.Clone('mj')
        mj.SetLineColor(30)
        mj.Sumw2()
        mj.SetStats(0)
        mj.Divide(m13)
        mj.SetMarkerColor(30)
        mj.SetMarkerStyle(20)
        mj.SetMarkerSize(0.5)
        mj.Draw("ep SAME")
        mj.SetTitle("")

        mk = m15.Clone('mk')
        mk.SetLineColor(40)
        mk.Sumw2()
        mk.SetStats(0)
        mk.Divide(m13)
        mk.SetMarkerColor(40)
        mk.SetMarkerStyle(20)
        mk.SetMarkerSize(0.5)
        mk.Draw("ep SAME")
        mk.SetTitle("")

        ml = m16.Clone('ml')
        ml.SetLineColor(26)
        ml.Sumw2()
        ml.SetStats(0)
        ml.Divide(m13)
        ml.SetMarkerColor(26)
        ml.SetMarkerStyle(20)
        ml.SetMarkerSize(0.5)
        ml.Draw("ep SAME")
        ml.SetTitle("")

        mm = m18.Clone('mm')
        mm.SetLineColor(36)
        mm.Sumw2()
        mm.SetStats(0)
        mm.Divide(m17)
        mm.SetMarkerColor(36)
        mm.SetMarkerStyle(20)
        mm.SetMarkerSize(0.5)
        mm.Draw("ep SAME")
        mm.SetTitle("")

        mn = m19.Clone('mn')
        mn.SetLineColor(46)
        mn.Sumw2()
        mn.SetStats(0)
        mn.Divide(m17)
        mn.SetMarkerColor(46)
        mn.SetMarkerStyle(20)
        mn.SetMarkerSize(0.5)
        mn.Draw("ep SAME")
        mn.SetTitle("")

        mo = m4.Clone('mo')
        mo.SetLineColor(49)
        mo.Sumw2()
        mo.SetStats(0)
        mo.Divide(m17)
        mo.SetMarkerColor(49)
        mo.SetMarkerStyle(20)
        mo.SetMarkerSize(0.5)
        mo.Draw("ep SAME")
        mo.SetTitle("")

        legend.AddEntry(ma,"Era B Old Skim","lep")
        legend.AddEntry(mb,"Era B Summer16 Skim","lep")
        legend.AddEntry(mc,"Era B Latest Skim","lep")
        legend.AddEntry(md,"Era C Old Skim","lep")
        legend.AddEntry(me,"Era C Summer16 Skim","lep")
        legend.AddEntry(mf,"Era C Latest Skim","lep")
        legend.AddEntry(mg,"Era D Old Skim","lep")
        legend.AddEntry(mh,"Era D Summer16 Skim","lep")
        legend.AddEntry(mi,"Era D Latest Skim","lep")
        legend.AddEntry(mj,"Era E Old Skim","lep")
        legend.AddEntry(mk,"Era E Summer16 Skim","lep")
        legend.AddEntry(ml,"Era E Latest Skim","lep")
        legend.AddEntry(mm,"Era F Old Skim","lep")
        legend.AddEntry(mn,"Era F Summer16 Skim","lep")
        legend.AddEntry(mo,"Era F Latest Skim","lep")
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

