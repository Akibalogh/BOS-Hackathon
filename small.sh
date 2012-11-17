HADOOP_HOME=/usr

OUTPUTFILE=/home/hackreduce/users/trs80/small_output

hadoop fs -rmr -skipTrash $OUTPUTFILE

$HADOOP_HOME/bin/hadoop  jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u5.jar \
    -inputreader "StreamXmlRecordReader,begin=<page>,end=</page>" \
    -mapper 'python aki-mapper.py' \
    -reducer 'python aki-reducer.py' \
    -input /home/hackreduce/users/trs80/wikipedia-sample.xml \
    -file aki-mapper.py \
    -file aki-reducer.py \
    -output $OUTPUTFILE
