#!/usr/bin/env python

import os
import re

def rename_files():
  file_list = os.listdir(r"/Users/duanegabel/work/Nanodegree/LocalServer/prank")

  os.chdir(r"/Users/duanegabel/work/Nanodegree/LocalServer/prank")

  for file in file_list:
    print("Old file: " + file)
#    print(re.sub(r"\d+", "", file))
    print("New file: " + file.translate(None, "0123456789"))
    os.rename(file, file.translate(None, "0123456789"))

rename_files()
