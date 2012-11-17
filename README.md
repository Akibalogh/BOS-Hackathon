BOS-Hackathon
=============

Some sample mapper and reducer code. Feel free to fork and modify.

The mapper generates tuples of article:link, where article is the title of the article being looked at and link is every internal Wikipedia link that's referenced.
The reducer takes sorted(!) tuples of article:link, article:link2 and makes them into lists article:link link2.

For example, say the article "Anarchy" links to two Wikipedia pages: Death and Destruction. This would output:
Anarchy:Death
Anarchy:Destruction

There are some small issues w/ the code as documented in the code.


Code to execute on Hadoop:
hadoop jar /usr/lib/hadoop-0.20/contrib/streaming/hadoop-streaming-0.20.2-cdh3u5.jar \
-inputreader "StreamXmlRecordReader,begin=<page>,end=</page>" \
-file ~/users/scorpions/aki-mapper.py -mapper ~/users/scorpions/aki-mapper.py \
-file ~/users/scorpions/aki-reducer.py -reducer ~/users/scorpions/aki-reducer.py \
-output /users/scorpions/aki-output -input /datasets/wikipedia/*