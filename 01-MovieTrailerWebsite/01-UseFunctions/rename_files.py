#!/usr/bin/env python

import os
import re
import shutil

def rename_files():
#   src = os.listdir(r"/Users/duanegabel/work/Nanodegree/LocalServer/prankFrom/")
  src = "/Users/duanegabel/Work/Nanodegree/LocalServer/prankFrom/"
  dest = "/Users/duanegabel/Work/Nanodegree/LocalServer/prankTo/"
  
  try:
    shutil.rmtree(dest)
    print("Destination directory removed")
  except:
    print("Destination directory not found")
  shutil.copytree(src, dest)
  
  os.chdir(dest)
  
  destFiles = os.listdir(dest)
  
  for file in destFiles:
    print("Old file: " + file)
#    print(re.sub(r"\d+", "", file))

    newFile = file.translate(None, "0123456789")
    
    print("New file: " + newFile)
    os.rename(file, newFile)

rename_files()
