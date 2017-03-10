#!/usr/bin/env python

import os
import re
import shutil

def rename_files():
#   src = os.listdir(r"/Users/duanegabel/work/Nanodegree/LocalServer/prankFrom/")
  src = "/Users/duanegabel/work/Nanodegree/LocalServer/prankFrom/"
  dest = "/Users/duanegabel/work/Nanodegree/LocalServer/prankTo/"
  
  try:
    shutil.rmtree(dest)
    print("Destination directory removed")
  except:
    print("Destination directory not found")
  shutil.copytree(src, dest)
  
  os.chdir(r"/Users/duanegabel/work/Nanodegree/LocalServer/prankTo")
  
  destFiles = os.listdir(r"/Users/duanegabel/work/Nanodegree/LocalServer/prankTo/")
  
  for file in destFiles:
    print("Old file: " + file)
#    print(re.sub(r"\d+", "", file))
    print("New file: " + file.translate(None, "0123456789"))
    os.rename(file, file.translate(None, "0123456789"))

rename_files()
