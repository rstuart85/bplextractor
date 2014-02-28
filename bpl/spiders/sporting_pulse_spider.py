from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from bpl.items import BplItem


class SPSpider(BaseSpider):
        name = "sporting_pulse"
        allowed_domains = ["sportingpulse.com"]
        match_round = 1
        start_urls = [
            "http://www.foxsportspulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-279778-0&pool=1&round={}".format(match_round),  # Seniors
            "http://www.foxsportspulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-279776-0&pool=1&round={}".format(match_round),  # Reserves
            "http://www.foxsportspulse.com/rpt_ladder.cgi?results=N&r&client=1-9386-0-279775-0&pool=1&round={}".format(match_round),  # U18s
            "http://www.foxsportspulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-282296-0&pool=1&round={}".format(match_round),  # U16s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-282580-0&pool=1&round={}".format(match_round),  # U15s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-282583-0&pool=1&round={}".format(match_round),  # U14s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-282582-0&pool=1&round={}".format(match_round),  # U13s
            "http://www.sportingpulse.com/rpt_ladder.cgi?results=N&client=1-9386-0-282503-0&pool=1&round={}".format(match_round),  # U12s
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
