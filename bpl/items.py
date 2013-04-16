# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BplItem(Item):
    league = Field()
    position = Field()
    club = Field()
    played = Field()
    won = Field()
    drawn = Field()
    lost = Field()
    goals_for = Field()
    goals_against = Field()
    goals_diff = Field()
    points = Field()
