# vcxproj_relative_path
automate generate relative path in vcxproj file.
The git has been widly used and many people download codes from it.
However after we compiled the code in one directory in VS,it will become impossible for us to move the project to other directory or other computer.
So I create this python project to automate generate relative path in vcxproj file.

Usage:
1.put the vcxproj_relative_path package in the same disk where contains your build path,such as C: or D:
2.If you have Spyder,open the main.py in it
3.change the directory to the path where you build your project(the path in cmake is 'where to build binaries' )
4.run it and everything is okay


Note:
1.I only have tested it by openMVG and openCV, if there were any other problems,please contact me with KevinYan37@163.com
2.You'd better run the py file once. I am not what will happen if you run it many times.