bplextractor
============

Extract BPL table information from SportingPulse. Theoretically could work on any FB league table on SportingPulse and possibly other zones competitions as well.

HowTo
-----

To use this library, you first need to double check the URLs in bpl/spiders/sporting\_pulse\_spider.py. It is configured to use the print view of tables on SportingPulse to extract the information (including team name). However, because the SportingPulse website sucks, you sometimes need to put the round number into the URL.

Once you are happy with the URLs in sporting\_pulse\_spider.py, you can then run the scrape process using:

    scrapy crawl sporting_pulse -o tables.json -t json

This will output each line of all configured tables as a JSON object. That obect will contain the competitin the entry refers to allowing to to re-assemble the tables.

The `logan_mdp_builder.py` script under the BPL folder takes the tables.json generated above and colates a table for each league plus he BPL Relegation table based on the 5,3,2,1 model. It is formated in such a way that I can copy and paste the output into Scribus for the Logan Lightning Match Day Program.

Requirements
------------

You need to have scrapy installed to use this code.

Warning
-------
Use this code at your own risk. It is scraping a live website!

