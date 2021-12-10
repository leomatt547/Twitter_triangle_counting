#!/usr/bin/env python

# import sys untuk baca STDIN dan STDOUT
import sys
  
# baca seluruh line dari STDIN
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # split ke dalam array kata
    inputnya = line.split()
    
    #  print pasangan, nanti Intermediate Output akan mengurutkan otomatis
    print(inputnya[0]+"\t"+inputnya[1])
    print(inputnya[1]+"\t"+inputnya[0])