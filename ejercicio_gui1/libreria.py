#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Feb 21 09:57:58 2013

import wx
from controlador import *
import thread
import time
# begin wxGlade: extracode
# end wxGlade



class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        
        # Menu Bar
        self.frame_2_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(1, "Conectar BD", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(2, "Exit", "", wx.ITEM_NORMAL)
        self.frame_2_menubar.Append(wxglade_tmp_menu, "File")
        self.SetMenuBar(self.frame_2_menubar)
        # Menu Bar end
        self.label_1 = wx.StaticText(self.notebook_1_pane_1, -1, "Autor")
        self.label_2 = wx.StaticText(self.notebook_1_pane_1, -1, u"Título")
        self.button_3 = wx.Button(self.notebook_1_pane_1, -1, "Buscar Libro")
        self.combo_box_1 = wx.ComboBox(self.notebook_1_pane_1, -1, choices=[], style=wx.CB_DROPDOWN)
        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.list_ctrl_1 = wx.ListCtrl(self.notebook_1_pane_1, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.label_3 = wx.StaticText(self.notebook_1_pane_2, -1, "Titulo:")
        self.text_ctrl_titulo = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_4 = wx.StaticText(self.notebook_1_pane_2, -1, "Autor:")
        self.text_ctrl_autor = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_8 = wx.StaticText(self.notebook_1_pane_2, -1, "Editorial:")
        self.text_ctrl_editorial = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_5 = wx.StaticText(self.notebook_1_pane_2, -1, "Fecha:")
        self.text_ctrl_fecha = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_6 = wx.StaticText(self.notebook_1_pane_2, -1, "Precio:")
        self.text_ctrl_precio = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_7 = wx.StaticText(self.notebook_1_pane_2, -1, "Portada:\n")
        self.text_ctrl_portada = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.button_buscar_portada = wx.Button(self.notebook_1_pane_2, -1, "Buscar...")
        self.button_1 = wx.Button(self.notebook_1_pane_2, -1, "Insertar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.Conectar, id=1)
        self.Bind(wx.EVT_MENU, self.Salir, id=2)
        self.Bind(wx.EVT_BUTTON, self.Buscar_Libro, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.onOpenFile, self.button_buscar_portada)
        self.Bind(wx.EVT_BUTTON, self.Insertar_Libro, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("Libreria 1.0")
        self.SetSize((686, 457))
        self.label_1.SetMinSize((40, 27))
        self.label_2.SetMinSize((34, 27))
        self.text_ctrl_2.SetMinSize((180, 27))
        self.label_3.SetMinSize((100, 30))
        self.text_ctrl_titulo.SetMinSize((300, 30))
        self.label_4.SetMinSize((100, 30))
        self.text_ctrl_autor.SetMinSize((300, 30))
        self.label_8.SetMinSize((100, 30))
        self.text_ctrl_editorial.SetMinSize((300, 30))
        self.label_5.SetMinSize((100, 30))
        self.text_ctrl_fecha.SetMinSize((100, 30))
        self.label_6.SetMinSize((100, 30))
        self.text_ctrl_precio.SetMinSize((100, 30))
        self.label_7.SetMinSize((100, 30))
        self.text_ctrl_portada.SetMinSize((300, 30))
        # end wxGlade
	self.list_ctrl_1.InsertColumn(0,"Titulo")
	self.list_ctrl_1.SetColumnWidth(0,250)
	self.list_ctrl_1.InsertColumn(1,"Autor")
	self.list_ctrl_1.SetColumnWidth(1,150)
	self.list_ctrl_1.InsertColumn(2,"Precio")
	self.list_ctrl_1.SetColumnWidth(2,100)
	self.list_ctrl_1.InsertColumn(3,"Año")
	self.list_ctrl_1.SetColumnWidth(3,60)
	#lista_autores = [u'Michael', u'Michael Ruphus', u'Tolkien']
	#for l in lista_autores: self.combo_box_1.Append(l)

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_8.Add(self.label_1, 0, 0, 0)
        sizer_8.Add(self.label_2, 0, 0, 0)
        sizer_8.Add(self.button_3, 0, 0, 0)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_9.Add(self.combo_box_1, 0, 0, 0)
        sizer_9.Add(self.text_ctrl_2, 0, 0, 0)
        sizer_7.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_6.Add(self.list_ctrl_1, 3, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_6)
        sizer_2.Add(self.label_3, 0, 0, 0)
        sizer_2.Add(self.text_ctrl_titulo, 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_4, 0, 0, 0)
        sizer_3.Add(self.text_ctrl_autor, 0, 0, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_14.Add(self.label_8, 0, 0, 0)
        sizer_14.Add(self.text_ctrl_editorial, 0, 0, 0)
        sizer_1.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_10.Add(self.label_5, 0, 0, 0)
        sizer_10.Add(self.text_ctrl_fecha, 0, 0, 0)
        sizer_1.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_11.Add(self.label_6, 0, 0, 0)
        sizer_11.Add(self.text_ctrl_precio, 0, 0, 0)
        sizer_1.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_12.Add(self.label_7, 0, 0, 0)
        sizer_12.Add(self.text_ctrl_portada, 0, 0, 0)
        sizer_12.Add(self.button_buscar_portada, 0, 0, 0)
        sizer_1.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_13.Add(self.button_1, 0, 0, 0)
        sizer_1.Add(sizer_13, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_1)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Buscar Libro")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Insertar Libro")
        sizer_5.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

    def Conectar(self, event): # wxGlade: MyFrame1.<event_handler>
        BBDD.conectar_bd()
	record = [u'Michael', u'Michael Ruphus', u'Tolkien', u'Daniel']
	for l in record: self.combo_box_1.Append(l)

    def Salir(self, event): # wxGlade: MyFrame1.<event_handler>
        self.Destroy()

    def Buscar_Libro(self, event): # wxGlade: MyFrame1.<event_handler>
	self.list_ctrl_1.DeleteAllItems()
	autor = self.combo_box_1.GetValue()
	titulo = self.text_ctrl_2.GetValue()        
	record = BBDD.busca_libro(titulo,autor)
	for (autor, libro) in record:
		fila=[libro.titulo, autor.nombre, libro.precio, libro.fecha]
		self.list_ctrl_1.Append([str(x).decode('latin1') for x in fila ])		
		#print 'Titulo: ', libro.titulo, '-->', 'Autor: ', autor.nombre

    def Insertar_Libro(self, event): # wxGlade: MyFrame1.<event_handler>
        claves = ['titulo','autor','editorial','fecha','precio','portada']
	
	titulo = self.text_ctrl_titulo.GetValue()
	autor = self.text_ctrl_autor.GetValue()
	editorial = self.text_ctrl_editorial.GetValue()
	fecha = self.text_ctrl_fecha.GetValue()
	precio = self.text_ctrl_precio.GetValue()
	portada = self.text_ctrl_portada.GetValue()

	valores = [titulo,autor,editorial,fecha,precio,portada]
	diccionario = dict(zip(claves, valores))

	BBDD.insertar_libro(diccionario)

    def onOpenFile(self, event): # wxGlade: MyFrame1.<event_handler>
        """
        Crear y mostar un Open FileDialog
        """
	# Comenzamos un nuevo thread, donde se ejecuta el sleep
        thread.start_new_thread(self.longRunning, ())

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir='./', 
            defaultFile="",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                self.text_ctrl_portada.SetValue(path)
	dlg.Destroy()
	
    def longRunning(self):
	for i in range(0,10):
		self.text_ctrl_titulo.SetValue('Hola mundo')
		time.sleep(2)
		self.text_ctrl_autor.SetValue('Un autor')
		time.sleep(2)
      
# end of class MyFrame1


if __name__ == "__main__":
    BBDD=Database()
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = MyFrame1(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
