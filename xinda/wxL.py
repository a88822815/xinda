# -*- coding: utf-8 -*-
import wx
import wx.grid
import logging
import os


# 第3步，实现wx.FileDropTarget子类
class FileDrop(wx.FileDropTarget):
    def __init__(self, m_text):
        wx.FileDropTarget.__init__(self)
        self.m_text = m_text

    def OnDropFiles(self, x, y, filePath):  # 当文件被拖入grid后，会调用此方法
        # cellCoords = self.grid.XYToCell(x, y)  # 根据坐标轴换算被拖入grid网格的行号和列号
        dirname = os.path.dirname(filePath[0])
        filename = os.path.basename(filePath[0])
        self.m_text.SetValue(dirname+'\\'+filename)


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_text1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_text1, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"执行", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.button1_click)

        self.fileDrop = FileDrop(self.m_text1)  # 第1步，创建FileDrop对象，并把grid传给初始化函数
        self.m_text1.SetDropTarget(self.fileDrop)
        # self.grid.SetDropTarget(self.fileDrop)  # 第2步，调用grid的SetDropTarget函数，并把FileDrop对象传给它

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button1_click(self, event):
        event.Skip()


class MainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show()
        self.frame.Center()
        return True


app = MainApp()
app.MainLoop()