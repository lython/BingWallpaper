# -*- coding: cp936 -*-  
from distutils.core import setup  
import py2exe  
  
includes = ["encodings", "encodings.*","sip","PyQt4.QtSvg"]  
  
options = {"py2exe":    
            {"compressed": 1, #ѹ��    
             "optimize": 2,    
             "ascii": 1,    
             "includes":includes,    
             "bundle_files": 1 #�����ļ������һ��exe�ļ�  
            }}  
setup(  
    options=options,
    zipfile=None,  
    description = u"��Ӧ��ֽ",
    version = "1.0.0.0",
    name = "Bing Wallpage",
    windows=[{"script": "BingWallpage.py", "icon_resources": [(1, "icon/icon.ico")] }],
)
