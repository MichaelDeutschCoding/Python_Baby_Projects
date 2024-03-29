#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  f = open(filename, 'r')
  words = f.read().lower().split()
  f.close()
  md = dict()
  md[''] = [words[0]]
  md[words[-1]] = [words[0]]
  for i in range(len(words)-1):
    if words[i] not in md:
      md[words[i]] = [words[i+1]]
    else:
      md[words[i]].append(words[i+1])
  
  return md

def print_mimic(mimic_dict, start_word):
  """Given mimic dict and start word, prints 200 random words."""
  fake = [start_word]
  while len(fake) < 200:
    old = fake[-1]
    if old in mimic_dict:
      new = random.choice(mimic_dict[old])
      fake.append(new)
    else:
      new = random.choice(mimic_dict[''])
  print(' '.join(fake))
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  print('just checking that main is getting called')
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  md = mimic_dict(sys.argv[1])
  print_mimic(md, '')


if __name__ == '__main__':
  main()
