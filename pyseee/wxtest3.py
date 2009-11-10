import os
import wx
ID_ABOUT=101
ID_EXIT=110
class MainWindow(wx.Frame):
    def __init__(main,parent,id,title):
        wx.Frame.__init__(main,parent,wx.ID_ANY, title, size = (200,100))
        main.control = wx.TextCtrl(main, 1, style=wx.TE_MULTILINE)
        main.CreateStatusBar() # A StatusBar in the bottom of the window
        # Setting up the menu.
        filemenu= wx.Menu()
        filemenu.Append(ID_ABOUT, "&About"," ok this is here")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"E&xit"," Terminate the program")
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        main.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        wx.EVT_MENU(main, ID_ABOUT, main.OnAbout) # attach the menu-event ID_ABOUT to the
                                                                                # method self.OnAbout
        wx.EVT_MENU(main, ID_EXIT, main.OnExit)   # attach the menu-event ID_EXIT to the
                                                            # method self.OnExit
        main.Show(True)
    def OnAbout(main,e):
        d= wx.MessageDialog( main, " a sample simple sniffenow longer than bfore /n"
                                            " in wxPython for learning","a sniffer",wx.CANCEL | wx.YES_NO)      # Create a message dialog box
        d.ShowModal() # Shows it
        d.Destroy() # finally destroy it when finished.
       # main.Close(True)  # Close the frame.    
        print 'can do more'
    def OnExit(main,e):
        main.Close(True)  # Close the frame.
app = wx.PySimpleApp()
frame = MainWindow(None, -1, "Sample editor")
app.MainLoop()
    if (d == wxYES)
    main.Close(True)  # Close the frame.