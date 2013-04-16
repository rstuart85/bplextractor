bplextractor
============

Extract BPL table information from SportingPulse. Theoretically could work on any FB league table on SportingPulse and possibly other zones competitions as well.

HowTo
-----

To use this library, you first need to double check the URLs in bpl/spiders/sporting\_pulse\_spider.py. It is configured to use the print view of tables on SportingPulse to extract the information (including team name). However, because the SportingPulse website sucks, you sometimes need to put the round number into the URL.

Once you are happy with the URLs in sporting\_pulse\_spider.py, you can then run the scrape process using:

    scrapy crawl sporting_pulse -o tables.json -t json

This will output each line of all configured tables as a JSON object. That obect will contain the competitin the entry refers to allowing to to re-assemble the tables.

Requirements
------------

You need to have scrapy installed to use this code.

Warning
-------
This code was written in 15 minutes to try and save myself some serious time. It has been used once. I will add to it as the 2013 season progresses (I will use it on average one every 2 weeks).

ToDO
----
The script I use to take the tables and produce the text output I need will follow soon.
