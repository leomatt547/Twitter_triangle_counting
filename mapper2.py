#!/usr/bin/env python

# import sys untuk baca STDIN dan STDOUT
import sys
  
# baca seluruh line dari STDIN
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # split ke dalam array kata
    u, v = line.split("\t",1)
    try:
        u = int(u)
        v = int(v)
    except ValueError:
        continue
    if v > u:
        #pastikan node terurut dari terkecil ke terbesar
        print(str(u)+"\t"+str(v)+"\t"+"X")