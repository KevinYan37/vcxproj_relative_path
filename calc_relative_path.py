# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:44:04 2017

@author: JY
"""

#calc relative path

import os.path


def calcRelativePath(current_path,other_path):
    # from current path to other path
    if(id(current_path[0])==id(other_path[0])):
        relative_path = os.path.relpath(other_path,current_path)
    else:
        relative_path = other_path
    return relative_path