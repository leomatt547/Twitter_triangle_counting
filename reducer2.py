from operator import itemgetter
import sys

current_u = None
list_v = []
u = None

# import sys untuk baca STDIN dan STDOUT
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    u, v, status = line.split('\t',2)
    try:
        u = int(u)
        v = int(v)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if current_u == u:
        list_v.append(v)
    else:
        if len(list_v)>1:
            # Kombinasi pasangan
            for i in range(len(list_v)):
                for j in range(i+1, len(list_v)-1):
                    print(u+"\t"+str(list_v[i])+"\t"+str(list_v[j]))
        else:
            print(u+"\t"+v+"\t"+"X")
        current_u = u
        list_v = []
    
#Operasi terakhir
if len(list_v)>1:
    # Kombinasi pasangan
    for i in range(len(list_v)):
        for j in range(i+1, len(list_v)-1):
            print(u+"\t"+str(list_v[i])+"\t"+str(list_v[j]))
else:
    print(u+"\t"+v+"\t"+"X")