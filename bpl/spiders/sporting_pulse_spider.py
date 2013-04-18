from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from bpl.items import BplItem


class SPSpider(BaseSpider):
        name = "sporting_pulse"
        allowed_domains = ["sportingpulse.com"]
        start_urls = [
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-244757-0",  # Seniors
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-244758-0",  # Reserves
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-244744-0",  # U18s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-245247-0&pool=1&round=4",  # U16s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-245245-0&pool=1&round=4",  # U15s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-245250-0&pool=1&round=4",  # U14s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-245249-0&pool=1&round=4",  # U13s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-245251-0&pool=1&round=4",  # U12s
        ]

        def parse(self, response):
            hxs = HtmlXPathSelector(response)
            ladder_row = hxs.select('//table/tr')[1:]
            league = hxs.select('//p[@class="heading5"]/text()').extract()[0]
            items = []
            for club in ladder_row:
                item = BplItem()
                item['league'] = league
                item['position'] = club.select('td[1]/text()').extract()[0]
                item['club'] = club.select('td[2]/a/text()').extract()[0]
                item['played'] = club.select('td[3]/text()').extract()[0]
                item['won'] = club.select('td[4]/text()').extract()[0]
                item['drawn'] = club.select('td[5]/text()').extract()[0]
                item['lost'] = club.select('td[6]/text()').extract()[0]
                item['goals_for'] = club.select('td[7]/text()').extract()[0]
                item['goals_against'] = club.select('td[8]/text()').extract()[0]
                item['goals_diff'] = club.select('td[9]/text()').extract()[0]
                item['points'] = club.select('td[10]/text()').extract()[0]
                items.append(item)
                print item['club']
            return items
