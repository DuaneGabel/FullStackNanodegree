#!/usr/bin/env python

import urllib

def read_text():
  quotes = open('/Users/duanegabel/Work/Nanodegree/01-MovieTrailerWebsite/04-ProfanityAlert/quotxs.txt')
  text = quotes.read()
  quotes.close()
  return text

def check_profanity(text_to_check):
  connection = urllib.urlopen('http://wdylike.appspot.com/?q=' + text_to_check)
  response = connection.read()
  connection.close()
  return response

result = check_profanity(read_text())

if "true" in result:
  print "Profanity Alert!!"
elif "false" in result:
  print "All Clear!!"
else:
  print "No result"
