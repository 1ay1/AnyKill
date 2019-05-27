#!/usr/bin/python

#pypiwin32, psutil, admin

import psutil
import subprocess
import os
import  win32api
from time import sleep
import win32com.client
import pythoncom
import ctypes
import win32process
import configparser
from pathlib import Path

sleep_time = 180

my_file = Path("set.cfg")
if not my_file.is_file():
    config = configparser.ConfigParser()
    config.read('set.cfg')
    config['DEFAULT']['sleep_time'] = str(sleep_time)  # update
    with open('set.cfg', 'w') as configfile:  # save
        config.write(configfile)

if my_file.is_file():
    config = configparser.ConfigParser()
    config.read('set.cfg')
    sleep_time = int(config['DEFAULT']['sleep_time'])

#sleep_time is the time to wait for now

# making the program rum without dos pop-up now
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd != 0:
    ctypes.windll.user32.ShowWindow(hwnd, 0)
    ctypes.windll.kernel32.CloseHandle(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    os.system('taskkill /PID ' + str(pid) + ' /f')

old_cur_pos = win32api.GetCursorPos()
sleep(sleep_time)

#the main event loop now
any_count = 0
while(True):
    new_cur_pos = win32api.GetCursorPos()

    if new_cur_pos == old_cur_pos:
        for process in psutil.process_iter():
            if process.name() == 'AnyDesk.exe':
                if(any_count == 0):
                    result = win32api.MessageBox(None, "You been idle for minutes now, Turn off Anydesk?", "ADKiller", 1)
                    any_count = any_count + 1
                if result == 1:
                    process = filter(lambda p: p.name() == "AnyDesk.exe", psutil.process_iter())
                    for i in process:
                        os.system("taskkill /f /im  AnyDesk.exe")
    any_count = 0
    old_cur_pos = new_cur_pos
    sleep(sleep_time)
