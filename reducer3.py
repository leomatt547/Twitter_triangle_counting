#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
current_word = None
sum = 0
word = None
  
# read the entire line from STDIN
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # split ke dalam array kata
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    sum += count
  
# keluarkan output trianglenya
print("triangle" + "\t" + str(sum))

