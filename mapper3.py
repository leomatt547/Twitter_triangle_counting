#!/usr/bin/env python

# import sys untuk baca STDIN dan STDOUT
import sys
  
# baca seluruh line dari STDIN
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # split ke dalam array kata
    u, v = line.split("\t",1)
    if v == "X":
        continue
    else:
        #Format(key, count)
        print(str(u)+"\t"+str(v))