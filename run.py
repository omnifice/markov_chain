#!/usr/bin/env python

import sys
from fetch_data import FetchData
from markov_python.cc_markov import MarkovChain

"""
Goofy first attempt at a Python application that uses the Codecademy
  markov_python module to create fun/dumb/whatever responses based on 
  data pulled from various web locations.

Pretty lame, but I didn't want to spend much time on it...

Expects at least one URL on the command line for a source of text to 
pull and search.

Example: run.py http://www.textfiles.com/sf/adams.txt http://www.textfiles.com/sf/alt3.txt
"""

def main(args):
  mc = MarkovChain()
  
  for a in args[1::]:
    fd = FetchData(a)
    mc.add_string(fd.fetch_data())
  
  chain = mc.generate_text()
  out = (" ").join(chain)
  
  print out
  

if __name__ == "__main__":
  main(sys.argv)

