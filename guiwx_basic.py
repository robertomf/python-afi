import wx

class App(wx.App):
	def OnInit(self):
		self.frame=wx.Frame(None,-1,title='Mi primera ventana', \
		size=(300,150))
		self.cajatexto=wx.TextCtrl(self.frame, -1, size=(220, -1), \
		pos=(40,10))
		self.Bind(wx.EVT_KEY_UP, self.OnKeyUP,self.cajatexto)
		butclose=wx.Button(self.frame, -1, 'Close',pos=(40,50))
		self.Bind(wx.EVT_BUTTON, self.OnClose, butclose)
		self.frame.Show()
		# self.frame.Fit()
		return True

	def OnClose(self,event):
		self.frame.Destroy()

	def OnKeyUP(self, event):
		keycode = event.GetKeyCode()
		if keycode==13:
			# Codigo para el Intro
			print ' Valor de la caja de texto= ', self.cajatexto.GetValue()
			self.cajatexto.SetValue("")

app=App(0)
app.MainLoop()

