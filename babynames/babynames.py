#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename, summary):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  with open(filename) as f:
    text = f.read()

  yr = re.search(r'Popularity in ((?:19|20)\d{2})</', text).group(1)
  names = re.findall(r'right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)', text)

  d = {}
  for n in names:
    d[n[1]] = n[0]
    d[n[2]] = n[0]

  raw_list = []
  for name, rank in sorted(d.items()):
    raw_list.append(' '.join([name, rank]))

  for i in range(len(raw_list)):
    raw_list[i] = f'{raw_list[i]:<17}'

  if summary:
    with open(f'{filename}.summary.txt', 'w') as nf:
      nf.write(f'{yr:^50}\n {"=" *50}\n')
      nf.write('\n'.join(["| ".join(raw_list[i:i+5]) for i in range(1, len(raw_list),5)]))

  else:
    print(f'{yr:^50}\n', '=' *50)
    print('\n'.join(["| ".join(raw_list[i:i+5]) for i in range(1, len(raw_list),5)]), '\n')
  
  return

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)
  
  print(f'main is running given the following argument list: {args}.')

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for i in range(len(args)):
    extract_names(args[i], summary)


if __name__ == '__main__':
  main()
