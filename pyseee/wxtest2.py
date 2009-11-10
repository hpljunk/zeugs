    import wx
    ID_ABOUT=101
    ID_EXIT=110
    class MainWindow(wx.Frame):
        def __init__(self,parent,id,title):
            wx.Frame.__init__(self,parent,wx.ID_ANY, title, size = (200,100))
            self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
            self.CreateStatusBar() # A Statusbar in the bottom of the window
            # Setting up the menu.
           filemenu= wx.Menu()
           filemenu.Append(ID_ABOUT, "&About"," Information about this program")
           filemenu.AppendSeparator()
           filemenu.Append(ID_EXIT,"E&xit"," Terminate the program")
           # Creating the menubar.
           menuBar = wx.MenuBar()
           menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
           self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
           self.Show(True)
   app = wx.PySimpleApp()
   frame = MainWindow(None, -1, "Sample editor")
   app.MainLoop()
