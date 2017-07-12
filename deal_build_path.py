# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:38:47 2017

@author: JY
"""

import os
import each_xml



def dealRelativePath(build_path):
    file_list=[]
    vcxproj_list=[]
    for root,dirs,files in os.walk(build_path):
        for name in files:
            file_list.append(os.path.join(root,name))
            

    for file_name_iter in file_list:
        if file_name_iter[-7:]=='vcxproj':
            vcxproj_list.append(file_name_iter)
    
    for vcxproj_iter in vcxproj_list:
        print(vcxproj_iter)
        each_xml.relaEachXmlFile(vcxproj_iter)
        