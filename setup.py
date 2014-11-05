# -*- coding: cp936 -*-  
from distutils.core import setup  
import py2exe  
  
includes = ["encodings", "encodings.*","sip","PyQt4.QtSvg"]  
  
options = {"py2exe":    
            {"compressed": 1, #压缩    
             "optimize": 2,    
             "ascii": 1,    
             "includes":includes,    
             "bundle_files": 1 #所有文件打包成一个exe文件  
            }}  
setup(  
    options=options,
    zipfile=None,  
    description = u"必应壁纸",
    version = "1.0.0.0",
    name = "Bing Wallpage",
    windows=[{"script": "BingWallpage.py", "icon_resources": [(1, "icon/icon.ico")] }],
)
