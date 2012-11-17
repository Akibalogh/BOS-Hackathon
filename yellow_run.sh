HADOOP_HOME=/usr

OUTPUTFILE=/home/hackreduce/users/trs80/yellow_output

hadoop fs -rmr -skipTrash $OUTPUTFILE

# export HADOOP_CLASSPATH=`hadoop classpath`:/home/hackreduce/HackReduce-0.3.jar

$HADOOP_HOME/bin/hadoop jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u5.jar \
    -D mapred.reduce.tasks=10 \
    -mapper 'python yellow-mapper.py' \
    -reducer 'python yellow-reducer.py' \
    -input /datasets/wikipedia/* \
    -file yellow-mapper.py \
    -file yellow-reducer.py \
    -output $OUTPUTFILE
    

#     -file HackReduce-0.3.jar \
#	-libjars HackReduce-0.3.jar \
#    -inputreader "org.hackreduce.mappers.XMLRecordReader,begin=<page>,end=</page>" \
#    -file HackReduce-0.3.jar \
#    -libjars HackReduce-0.3.jar \
