HADOOP_HOME=/usr

$HADOOP_HOME/bin/hadoop  jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u5.jar \
    -inputreader "StreamXmlRecordReader,begin=<page>,end=</page>" \
    -mapper 'python aki-mapper.py' \
    -reducer 'python empty-reducer.py' \
    -input /home/hackreduce/users/trs80/wikipedia-sample.xml \
    -file aki-mapper.py \
    -file empty-reducer.py \
    -output /home/hackreduce/users/trs80/empty_output
