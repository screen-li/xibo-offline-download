#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Oct 31 14:49:59 2010

import wx

# begin wxGlade: extracode
# end wxGlade



class AddDisplayUI(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AddDisplayUI.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.lblClientName = wx.StaticText(self, -1, _("Client Name"))
        self.txtClientName = wx.TextCtrl(self, -1, "")
        self.lblClientKey = wx.StaticText(self, -1, _("Client Key"))
        self.txtClientKey = wx.TextCtrl(self, -1, "")
        self.panel_1 = wx.Panel(self, -1)
        self.btnCreateDisplay = wx.Button(self, -1, _("Add Display"))
        self.btnGenerateKey = wx.Button(self, -1, _("Generate Key"))
        self.btnCancel = wx.Button(self, -1, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onCreateDisplay, self.btnCreateDisplay)
        self.Bind(wx.EVT_BUTTON, self.onGenerateKey, self.btnGenerateKey)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.btnCancel)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AddDisplayUI.__set_properties
        self.SetTitle(_("Add Display"))
        self.txtClientName.SetToolTipString(_("The name of the client to add as it will appear on the server"))
        self.btnGenerateKey.SetToolTipString(_("Generate a random client license key"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AddDisplayUI.__do_layout
        grid_sizer_3 = wx.FlexGridSizer(3, 3, 0, 0)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_3.Add(self.lblClientName, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add((20, 20), 0, 0, 0)
        grid_sizer_3.Add(self.txtClientName, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.lblClientKey, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add((20, 20), 0, 0, 0)
        grid_sizer_3.Add(self.txtClientKey, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_3.Add((20, 20), 0, 0, 0)
        sizer_1.Add(self.btnCreateDisplay, 0, 0, 0)
        sizer_1.Add(self.btnGenerateKey, 0, 0, 0)
        sizer_1.Add(self.btnCancel, 0, 0, 0)
        grid_sizer_3.Add(sizer_1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        grid_sizer_3.AddGrowableCol(2)
        self.Layout()
        # end wxGlade

    def onCreateDisplay(self, event): # wxGlade: AddDisplayUI.<event_handler>
        print "Event handler `onCreateDisplay' not implemented!"
        event.Skip()

    def onGenerateKey(self, event): # wxGlade: AddDisplayUI.<event_handler>
        print "Event handler `onGenerateKey' not implemented!"
        event.Skip()

    def onCancel(self, event): # wxGlade: AddDisplayUI.<event_handler>
        print "Event handler `onCancel' not implemented!"
        event.Skip()

# end of class AddDisplayUI

class XiboOfflineDownloadUI(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: XiboOfflineDownloadUI.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.Tabs = wx.Notebook(self, -1, style=0)
        self.Tabs_Displays = wx.Panel(self.Tabs, -1)
        self.Tabs_Download = wx.Panel(self.Tabs, -1)
        self.selectedDisplays = wx.ListBox(self.Tabs_Download, -1, choices=[], style=wx.LB_MULTIPLE|wx.LB_ALWAYS_SB)
        self.lblSelection = wx.StaticText(self.Tabs_Download, -1, _("Selection:"))
        self.btnAll = wx.Button(self.Tabs_Download, -1, _("All"))
        self.btnNone = wx.Button(self.Tabs_Download, -1, _("None"))
        self.btnInvert = wx.Button(self.Tabs_Download, -1, _("Invert"))
        self.lblDisplays = wx.StaticText(self.Tabs_Download, -1, _("Displays:"))
        self.btnAdd = wx.Button(self.Tabs_Download, -1, _("Add"))
        self.btnRemove = wx.Button(self.Tabs_Download, -1, _("Delete"))
        self.panel_3 = wx.Panel(self.Tabs_Download, -1)
        self.txtOutput = wx.TextCtrl(self.Tabs_Download, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_LINEWRAP)
        self.btnDownload = wx.Button(self.Tabs_Download, -1, _("Download"))
        self.btnCancel = wx.Button(self.Tabs_Download, -1, _("Cancel"))
        self.lblServerURL = wx.StaticText(self.Tabs_Displays, -1, _("Server URL"))
        self.txtServerURL = wx.TextCtrl(self.Tabs_Displays, -1, "")
        self.lblServerKey = wx.StaticText(self.Tabs_Displays, -1, _("Server Key"))
        self.txtServerKey = wx.TextCtrl(self.Tabs_Displays, -1, "")
        self.lblVerbose = wx.StaticText(self.Tabs_Displays, -1, _("Verbose Output"))
        self.chkVerbose = wx.CheckBox(self.Tabs_Displays, -1, "")
        self.panel_4 = wx.Panel(self.Tabs_Displays, -1)
        self.btnSave = wx.Button(self.Tabs_Displays, -1, _("Save"))
        self.lnHorizontalLine = wx.StaticLine(self, -1)
        self.Logo = wx.StaticBitmap(self, -1, wx.Bitmap("logo.jpg", wx.BITMAP_TYPE_ANY), style=wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX_DCLICK, self.onDisplayListDClick, self.selectedDisplays)
        self.Bind(wx.EVT_LISTBOX, self.onDisplayListClick, self.selectedDisplays)
        self.Bind(wx.EVT_BUTTON, self.onSelectAll, self.btnAll)
        self.Bind(wx.EVT_BUTTON, self.onSelectNone, self.btnNone)
        self.Bind(wx.EVT_BUTTON, self.onSelectInvert, self.btnInvert)
        self.Bind(wx.EVT_BUTTON, self.onAddDisplay, self.btnAdd)
        self.Bind(wx.EVT_BUTTON, self.onDeleteDisplay, self.btnRemove)
        self.Bind(wx.EVT_BUTTON, self.onDownload, self.btnDownload)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.btnCancel)
        self.Bind(wx.EVT_TEXT, self.onServerUrlChange, self.txtServerURL)
        self.Bind(wx.EVT_TEXT, self.onServerKeyChange, self.txtServerKey)
        self.Bind(wx.EVT_CHECKBOX, self.onVerboseChange, self.chkVerbose)
        self.Bind(wx.EVT_BUTTON, self.onConfigSave, self.btnSave)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: XiboOfflineDownloadUI.__set_properties
        self.SetTitle(_("Xibo Offline Download Application"))
        self.SetSize((750, 500))
        self.selectedDisplays.SetMinSize((368, 300))
        self.btnRemove.Enable(False)
        self.txtOutput.SetMinSize((369, 300))
        self.btnDownload.SetDefault()
        self.btnCancel.Enable(False)
        self.btnSave.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: XiboOfflineDownloadUI.__do_layout
        frmMainSizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(4, 2, 2, 2)
        tabDownloadSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 4, 2, 2)
        sizer_5.Add(self.selectedDisplays, 0, 0, 0)
        grid_sizer_1.Add(self.lblSelection, 0, 0, 0)
        grid_sizer_1.Add(self.btnAll, 0, 0, 0)
        grid_sizer_1.Add(self.btnNone, 0, 0, 0)
        grid_sizer_1.Add(self.btnInvert, 0, 0, 0)
        grid_sizer_1.Add(self.lblDisplays, 0, 0, 0)
        grid_sizer_1.Add(self.btnAdd, 0, 0, 0)
        grid_sizer_1.Add(self.btnRemove, 0, 0, 0)
        grid_sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableCol(0)
        sizer_5.Add(grid_sizer_1, 1, wx.EXPAND, 10)
        tabDownloadSizer.Add(sizer_5, 1, 0, 0)
        tabDownloadSizer.Add((20, 20), 0, 0, 0)
        sizer_6.Add(self.txtOutput, 0, 0, 0)
        sizer_7.Add(self.btnDownload, 0, 0, 0)
        sizer_7.Add(self.btnCancel, 0, 0, 0)
        sizer_6.Add(sizer_7, 1, wx.ALIGN_RIGHT, 0)
        tabDownloadSizer.Add(sizer_6, 1, wx.EXPAND, 0)
        self.Tabs_Download.SetSizer(tabDownloadSizer)
        grid_sizer_2.Add(self.lblServerURL, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.txtServerURL, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.lblServerKey, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.txtServerKey, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.lblVerbose, 0, 0, 0)
        grid_sizer_2.Add(self.chkVerbose, 0, 0, 0)
        grid_sizer_2.Add(self.panel_4, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.btnSave, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        self.Tabs_Displays.SetSizer(grid_sizer_2)
        grid_sizer_2.AddGrowableCol(1)
        self.Tabs.AddPage(self.Tabs_Download, _("Download"))
        self.Tabs.AddPage(self.Tabs_Displays, _("Configuration"))
        frmMainSizer.Add(self.Tabs, 1, wx.EXPAND, 0)
        frmMainSizer.Add(self.lnHorizontalLine, 0, wx.EXPAND, 0)
        frmMainSizer.Add(self.Logo, 0, wx.ALL|wx.EXPAND|wx.ALIGN_BOTTOM, 0)
        self.SetSizer(frmMainSizer)
        self.Layout()
        # end wxGlade

    def onSelectAll(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onSelectAll' not implemented!"
        event.Skip()

    def onSelectNone(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onSelectNone' not implemented!"
        event.Skip()

    def onSelectInvert(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onSelectInvert' not implemented!"
        event.Skip()

    def onAddDisplay(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onAddDisplay' not implemented!"
        event.Skip()

    def onDeleteDisplay(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onDeleteDisplay' not implemented!"
        event.Skip()

    def onDownload(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onDownload' not implemented!"
        event.Skip()

    def onCancel(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onCancel' not implemented!"
        event.Skip()

    def onConfigSave(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onConfigSave' not implemented!"
        event.Skip()

    def onDisplayListDClick(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onDisplayListDClick' not implemented"
        event.Skip()

    def onDisplayListClick(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onDisplayListClick' not implemented"
        event.Skip()

    def onServerUrlChange(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onServerUrlChange' not implemented"
        event.Skip()

    def onServerKeyChange(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onServerKeyChange' not implemented"
        event.Skip()

    def onVerboseChange(self, event): # wxGlade: XiboOfflineDownloadUI.<event_handler>
        print "Event handler `onVerboseChange' not implemented"
        event.Skip()

# end of class XiboOfflineDownloadUI


if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frmMain = XiboOfflineDownloadUI(None, -1, "")
    app.SetTopWindow(frmMain)
    frmMain.Show()
    app.MainLoop()
