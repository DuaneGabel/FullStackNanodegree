#!/usr/bin/env python
import time
import webbrowser

counter = 0

print("This program started at " + time.ctime())
while (counter < 3):
  time.sleep(10)
  webbrowser.open("https://www.youtube.com/watch?v=JoxuZFYofkk")
  counter += 1
