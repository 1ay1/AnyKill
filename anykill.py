#!/usr/bin/python

#pypiwin32, psutil, admin

import psutil
import subprocess
import os
import  win32api
from time import sleep
import win32com.client
import pythoncom



savedpos = win32api.GetCursorPos()
any_count = 0
while(True):

    curpos = win32api.GetCursorPos()
    if savedpos == curpos:
        for process in psutil.process_iter():
            if process.name() == 'AnyDesk.exe' and any_count != 0:
                result = win32api.MessageBox(None, "You been idle for minutes now, Turn off Anydesk?", "ADKiller", 1)
                if result == 1:
                    process = filter(lambda p: p.name() == "AnyDesk.exe", psutil.process_iter())
                    for i in process:
                        os.system("taskkill /f /im  AnyDesk.exe")


    any_count = 1
    savedpos = curpos
    sleep(2)