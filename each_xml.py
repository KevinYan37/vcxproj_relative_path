# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xml.dom.minidom
import calc_relative_path
import get_dir_path

#set it 0 for no log information
LOG_MODE = 0

def relaEachXmlFile(vcxproj_file_path):

    #xml file path
    xml_path = vcxproj_file_path
    xml_path_no_file = get_dir_path.getDirectoryFromPath(vcxproj_file_path)
    
    #get root project
    dom = xml.dom.minidom.parse(xml_path)
    root = dom.documentElement
    
    #get nodes that contain the path information
    property_group_root = root.getElementsByTagName('PropertyGroup')
    item_definition_root = root.getElementsByTagName('ItemDefinitionGroup')
    item_group_root = root.getElementsByTagName('ItemGroup')
    
    if LOG_MODE:
        print('node information')
        for iter in item_definition_root:
            print(iter)
        for iter in item_group_root:
            print(iter)
    

    if property_group_root.length>0:
        for property_iter in property_group_root:
            out_dir_node = property_iter.getElementsByTagName('OutDir')
            if out_dir_node.length>0:
                for out_dir_iter in out_dir_node:
                    out_dir_path = out_dir_iter.firstChild.data
                    if ( id(out_dir_path[0])!=id('$') ):
                        out_dir_rela_path = calc_relative_path.calcRelativePath(xml_path_no_file,out_dir_path)
                        out_dir_iter.firstChild.nodeValue = out_dir_rela_path 
            
            
    #loop to deal with the path
    node_name_list = ['ClCompile','ResourceCompile','Midl','Link']
    if item_definition_root.length>0:
        for definition_iter in item_definition_root:
            for node_iter in node_name_list:
                node = definition_iter.getElementsByTagName(node_iter)
                if node.length>0:
                    if(node_iter=='Link'):
                        importLibrary_node = node[0].getElementsByTagName('ImportLibrary')
                        programdata_node = node[0].getElementsByTagName('ProgramDataBaseFile')
                        
                        if importLibrary_node.length>0:
                            importLibarry_relative_path = calc_relative_path.calcRelativePath(xml_path_no_file,get_dir_path.getDirectoryFromPath(importLibrary_node[0].firstChild.data))
                            importLibrary_node[0].firstChild.nodeValue = importLibarry_relative_path+'/'+get_dir_path.getFileName(importLibrary_node[0].firstChild.data)
                        
                        if programdata_node.length>0:
                            programdata_relative_path = calc_relative_path.calcRelativePath(xml_path_no_file,get_dir_path.getDirectoryFromPath(programdata_node[0].firstChild.data))
                            programdata_node[0].firstChild.nodeValue = programdata_relative_path+'/'+get_dir_path.getFileName(programdata_node[0].firstChild.data)
            
                    else:      
                        
                        additional_path_node = node[0].getElementsByTagName('AdditionalIncludeDirectories')
                        
                        if additional_path_node.length>0:
                            if LOG_MODE:
                                print(additional_path_node[0].firstChild.data)
                            
                            relative_path='';
                            path_list = str(additional_path_node[0].firstChild.data).split(';')
                            for path_iter in path_list:
                                if(id(path_iter[0])!=id('%')):
                                    relative_path_definition = calc_relative_path.calcRelativePath(xml_path_no_file,get_dir_path.getDirectoryFromPath(path_iter))
                                    relative_path = relative_path + relative_path_definition+';'
                                else:
                                    relative_path = relative_path + path_iter
                            additional_path_node[0].firstChild.nodeValue = relative_path
            
    #only deal with the item contains ProjectReference   
    item_node_list =  ['CustomBuild','ClCompile','ProjectReference']  
    if item_group_root.length>0:     
        for group_iter in item_group_root:
            for item_iter in item_node_list:
                project_reference_node = group_iter.getElementsByTagName(item_iter)
                
                if project_reference_node.length>0:
                    if LOG_MODE:
                        for iter in project_reference_node:
                            print(iter.getAttribute('Include'))
                            
                    if item_iter=='CustomBuild': 
                            group_iter.removeChild(project_reference_node[0])
                    else:
                        for iter in project_reference_node:
                            file_path = iter.getAttribute('Include')
                            relative_path_group = calc_relative_path.calcRelativePath(xml_path_no_file,get_dir_path.getDirectoryFromPath(file_path))
                            iter.setAttribute('Include',relative_path_group+'/'+get_dir_path.getFileName(file_path))
        
            
    #save new file
    new_xml_file = open(vcxproj_file_path,'w',encoding='utf-8')
    dom.writexml(new_xml_file,encoding='utf-8')
    new_xml_file.close()    