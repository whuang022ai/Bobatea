#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyautogui import typewrite, press, hotkey
import time
import json

import os
current_path = os.path.dirname(os.path.realpath(__file__))

cmds = ['pca',
        'log',
        'take',
        'drop',
        'csvf',
        'scatter',
        't',
        'pair',
        'hcluster',
        'kmean',
        'index',
        'header',
        'merge',
        'mergebyix',
        'tsne',
        'curve',
        'mean',
        'kat',
        'group',
        'search']


def show_cmd(cmd):
    current_cmd = cmd
    typewrite(cmd)


def del_cmd():
    hotkey('ctrl', 'u')


del_cmd()
jsonFile = open(current_path+"/f.json", "r")
data = json.load(jsonFile)
jsonFile.close()
ix = int(data["cmd"])
show_cmd(cmds[ix])
ix = ix+1
if ix > len(cmds)-1:
    ix = 0
data["cmd"] = ix
jsonFile = open(current_path+"/f.json", "w+")
jsonFile.write(json.dumps(data))
jsonFile.close()
