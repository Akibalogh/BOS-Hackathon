HADOOP_HOME=/usr

$HADOOP_HOME/bin/hadoop  jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u5.jar \
    -D mapred.reduce.tasks=20
    -mapper 'perl map.pl' \
    -reducer 'perl reduce.pl' \
    -input /datasets/msd \
    -file map.pl \
    -file reduce.pl \
    -output /home/hackreduce/users/trs80/output
