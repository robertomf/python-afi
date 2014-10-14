import wx
import thread
from time import sleep

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.label = wx.StaticText(self, label="Listo")
        self.btn = wx.Button(self, label="Empezar")
        self.gauge = wx.Gauge(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label, proportion=1, flag=wx.EXPAND)
        sizer.Add(self.btn, proportion=0, flag=wx.EXPAND)
        sizer.Add(self.gauge, proportion=0, flag=wx.EXPAND)

        self.SetSizerAndFit(sizer)

        self.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, evt):
        self.btn.Enable(False)
        self.gauge.SetValue(0)
        self.label.SetLabel("Ejecutando")
        # Comenzamos un nuevo thread, donde se ejecuta el sleep
        thread.start_new_thread(self.longRunning, ())

    def onLongRunDone(self):
        self.gauge.SetValue(100)
        self.label.SetLabel("Listo!")
        self.btn.Enable(True)

    def longRunning(self):
        """Esto se ejecuta en otro thread.  Llamamos a Sleep para simular la otra tarea que se esta realizando."""
        #Para hacer llamadas a widgets de la GUI desde este Thread, necesitamos enmplear
        # wx.CallAfter
        for i in range(4):
            print ' Estamos trabajado....'
            sleep(2)
        wx.CallAfter(self.gauge.SetValue, 20)
        sleep(5)
        wx.CallAfter(self.gauge.SetValue, 50)
        sleep(1)
        wx.CallAfter(self.gauge.SetValue, 70)
        sleep(10)
        wx.CallAfter(self.onLongRunDone)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.TopWindow = MainFrame(None)
    app.TopWindow.Show()
    app.MainLoop()
