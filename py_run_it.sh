HADOOP_HOME=/usr

OUTPUTFILE=/home/hackreduce/users/trs80/py_output

hadoop fs -rmr -skipTrash $OUTPUTFILE

# export HADOOP_CLASSPATH=`hadoop classpath`:/home/hackreduce/HackReduce-0.3.jar

$HADOOP_HOME/bin/hadoop jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u5.jar \
    -D mapred.reduce.tasks=20
    -mapper 'python aki-mapper.py' \
    -reducer 'python aki-reducer.py' \
    -input /datasets/wikipedia \
    -file aki-mapper.py \
    -file aki-reducer.py \
    -output $OUTPUTFILE

#     -file HackReduce-0.3.jar \
#	-libjars HackReduce-0.3.jar \
#    -inputreader "org.hackreduce.mappers.XMLRecordReader,begin=<page>,end=</page>" \
#    -file HackReduce-0.3.jar \
#    -libjars HackReduce-0.3.jar \
