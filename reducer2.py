#!/usr/bin/env python

from operator import itemgetter
import sys

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def nCr(n,r):
    a = factorial(n)
    b = factorial(r)
    c = factorial(n-r)
    return int(a/(b*c))

current_word = None
current_count = 0
word = None

# import sys untuk baca STDIN dan STDOUT
for line in sys.stdin:    
    # buang spasi
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word, v, status = line.split('\t',2)
    if current_word == word:
        current_count += 1
    else:
        if current_word:
            if(current_count>1):
                # write result to STDOUT
                current_com = nCr(current_count, 2)
                print(current_word+"\t"+str(current_com))
            else:
                print(current_word+"\t"+"X")
        current_count = 1
        current_word = word

if(current_count>1):
    # write result to STDOUT
    current_com = nCr(current_count, 2)
    print(current_word+"\t"+str(current_com))
else:
    print(current_word+"\t"+"X")