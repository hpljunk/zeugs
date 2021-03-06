#!/usr/bin/env python2.4

import wx

#______________________________________________

class BitmapPanel(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, size = (200,200))
		self.Bind(wx.EVT_PAINT,self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.OnSize()
				
	def OnPaint(self,event):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.bitmap,0,0)

	def OnSize(self, event=None):
		self.CreateBitmap()
		self.DrawGrid()
		
	def CreateBitmap(self):
		width, height = self.GetSize()
		self.bitmap = wx.EmptyBitmap(width,height)
	
	def DrawGrid(self):
		border = 5
		size = 24
		lineNumber = 20
		
		dc = wx.MemoryDC()
		dc.SelectObject(self.bitmap)
		dc.SetBackground(wx.Brush("Red"))

		brush = wx.Brush(wx.Colour(120,120,120),wx.SOLID)
		pen = wx.Pen(wx.Colour(120,120,120),3,wx.SOLID)
		pen.SetCap(wx.CAP_BUTT)
		dc.SetBrush(brush)
		dc.SetPen(pen)
		for i in range(lineNumber):
			#draw vertical lines
			
			dc.DrawLine(border+i*size,border,border+i*size,border+(lineNumber-1)*size)
			#draw horizontal lines

			dc.DrawLine(border,border+i*size,border+(lineNumber-1)*size,border+i*size)

	def SaveImage(self, FileName):
		self.bitmap.SaveFile(FileName, wx.BITMAP_TYPE_PNG)
				
#______________________________________________

class VirtualBitmap(wx.MemoryDC):
	def __init__(self,width=200,height=200):
		wx.MemoryDC.__init__(self)
		self.width = width
		self.height = height
		self.bitmap = wx.EmptyBitmap(width,height)
		self.SelectObject(self.bitmap)
		self.Clear()

	def SaveFile(self,name,bmptype=wx.BITMAP_TYPE_PNG):
		return self.bitmap.SaveFile(name, bmptype)
#______________________________________________

def DrawGrid(panel):
	border = 5
	size = 24
	lineNumber = 30
	panel.bitmap.SetWidth(lineNumber*size+border*2)
	panel.bitmap.SetHeight(lineNumber*size+border*2)

	for i in range(lineNumber):
		#draw vertical lines
		panel.DrawLine(border+i*size,border,border+i*size,border+(lineNumber-1)*size)
		#draw horizontal lines
		panel.DrawLine(border,border+i*size,border+(lineNumber-1)*size,border+i*size)

		
class MyFrame(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title)
		self.Panel = BitmapPanel(self, -1)
	
	def SaveImage(self, FileName):
		self.Panel.SaveImage(FileName)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame =MyFrame("View")
	#bool = img.SaveFile("wxBitmap.png",wx.BITMAP_TYPE_PNG)
	#if not bool:
	#    print "Couldn't save"
	frame.Show(True)
	frame.SaveImage("wxBitmap.png")
	app.MainLoop()

	
