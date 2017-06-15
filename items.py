# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field,Item 

class TripadvisorItem(Item):
	rest_name = Field()
	rest_location = Field()
	rest_city = Field()
	rest_address = Field()
	rest_url = Field()
	rest_imgUrl = Field()
	rest_rating = Field()
	rest_votes = Field()
	review = Field()
	title = Field()
	date = Field()
	url = Field()
	rating =Field()
	promotes = Field()
	place =Field()
	value = Field()
	service = Field()
	food = Field()
	atmosphere = Field()
	user = Field() 
	review_id = Field()
	comments = Field()
    
    
