# import sys untuk baca STDIN dan STDOUT
import sys
import os

# os.environ['HADOOP_HOME'] = "D:\Hadoop\hadoop-3.3.1"
# sys.path.append("D:\Hadoop\hadoop-3.3.1/bin")

# os.system.setProperty("HADOOP_HOME", "D:\Hadoop\hadoop-3.3.1")
# os.system.setProperty("hadoop.home.dir", "D:\Hadoop\hadoop-3.3.1")
  
# baca seluruh line dari STDIN
for line in sys.stdin:
    # buang spasi
    line = line.strip()
    # split ke dalam array kata
    inputnya = line.split()
    
    #  print pasangan, nanti Intermediate Output akan mengurutkan otomatis
    print(inputnya[0]+"\t"+inputnya[1])
    print(inputnya[1]+"\t"+inputnya[0])