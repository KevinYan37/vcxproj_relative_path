# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:37:45 2017

@author: JY
"""
import os.path

def getDirectoryFromPath(in_path):
    if(os.path.isdir(in_path)):
        return in_path
    else:
        return os.path.abspath(os.path.dirname(in_path)+os.path.sep)
        
def getFileName(in_path):
    return os.path.basename(in_path)
        