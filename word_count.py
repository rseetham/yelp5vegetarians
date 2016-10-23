'''
To use on pyspark shell
upload corpus file to hdfs using something like on ec2 spark
ephemeral-hdfs/bin/hadoop dfs -put "textdata/corpus" /

To launch python spark shell : 
./spark/bin/pyspark
'''

import re

ipfile = sc.textFile("/corpus")
//Test
//ipfile.count()
wordCounts = ipfile.flatMap(lambda line: filter(None, re.split("[, \-!?:.;/]+",line))).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

counts = wordCounts.collect()
f = open("corpus_output.txt","w")
for (word,c) in counts :
  a = word.encode('utf-8') +',' + str(c) + '\n'
  f.write(a)
f.close()


