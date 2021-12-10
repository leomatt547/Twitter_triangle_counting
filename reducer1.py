from operator import itemgetter
import sys
import os

# os.environ['HADOOP_HOME'] = "D:\Hadoop\hadoop-3.3.1"
# sys.path.append("D:\Hadoop\hadoop-3.3.1/bin")

# os.system.setProperty("HADOOP_HOME", "D:\Hadoop\hadoop-3.3.1")
# os.system.setProperty("hadoop.home.dir", "D:\Hadoop\hadoop-3.3.1")
  
current_v = None
v = None
  
# import sys untuk baca STDIN dan STDOUT
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    u, v = line.split('\t', 1)
  
    if current_v == v:
        continue
    else:
        if current_v:
            # write result to STDOUT
            print(u+"\t"+v)
        current_v = v