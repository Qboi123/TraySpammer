import os
import sys
import webbrowser
import wx
from wx import adv as wx_adv
from wx.adv import TaskBarIcon as TaskBarIcon

SPAM_AMOUNT = 20

APP: "TraySpammerApp"


class SpammedTaskBarIcon(TaskBarIcon):
    def __init__(self, frame: "HiddenFrame"):
        TaskBarIcon.__init__(self)

        self.frame = frame

        # noinspection PyUnusedLocal
        def click(event):
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

            frame.icon.Destroy()
            frame.Destroy()

        self.SetIcon(wx.Icon('./res/icon.png', wx.BITMAP_TYPE_PNG), 'Never Gonna Give You Up')
        self.Bind(wx_adv.EVT_TASKBAR_LEFT_DOWN, click)
        self.Bind(wx_adv.EVT_TASKBAR_RIGHT_DOWN, lambda event: webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, 'Never gonna give you up')
        menu.Append(2, 'Never gonna let you down')
        menu.Append(3, 'Never gonna run around and desert you')
        menu.Append(4, 'Never gonna make you cry')
        menu.Append(5, 'Never gonna say goodbye')
        menu.Append(6, 'Never gonna tell a lie and hurt you.')

        return menu


class HiddenFrame(wx.Frame):
    def __init__(self, parent, id_, title):
        wx.Frame.__init__(self, parent, id_, title, (-1, -1), (290, 280))

        self.SetSize((350, 250))
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.icon = SpammedTaskBarIcon(self)

        self.Centre()

    # noinspection PyUnusedLocal
    def on_close(self, event):
        self.icon.Destroy()
        self.Destroy()


class TraySpammerApp(wx.App):
    def OnInit(self):
        # Spawn 1000 tray items
        for i in range(0, SPAM_AMOUNT):
            frame = HiddenFrame(None, -1, 'Tray Spammer 3000')
            self.SetTopWindow(frame)

        return True


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    if hasattr(sys, "_MEIPASS"):
        # noinspection PyProtectedMember
        os.chdir(sys._MEIPASS)

    APP = TraySpammerApp(0)
    APP.MainLoop()
