BOS-Hackathon
=============

Some sample mapper and reducer code. Feel free to fork and modify.

aki-mapper and aki-reducer
==========

The mapper generates tuples of article:link, where article is the title of the article being looked at and link is every internal Wikipedia link that's referenced.
The reducer takes sorted(!) tuples of article:link, article:link2 and makes them into lists article:link link2.

For example, say the article "Anarchy" links to two Wikipedia pages: Death and Destruction. The mapper would output:
anarchy:death
anarchy:destruction

The reducer outputs: anarchy death destruction


yellow-maper and yellow-reducer
==========

These scripts list the number of times that an article is cited in Wikipedia.

For example, the reducer outputs:
8813 anarchy