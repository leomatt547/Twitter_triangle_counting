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
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if v > u:
        #pastikan node terurut dari terkecil ke terbesar
        print(u+"\t"+v+"\t"+"X")