from bs4 import BeautifulSoup
import urllib
import json
# data = []
# dct = {}

class Zomato_Beautiful_Scrapper():

	def __init__(self,restaurant_url,rest_reviews,rest_name):
		self.restaurant_url = restaurant_url
		self.rest_reviews = rest_reviews
		self.rest_name = rest_name
		self.Trip_Scrapper()
	def Trip_Scrapper(self):
		try :
			data = []
			dct = {}
			r = urllib.urlopen(self.restaurant_url).read()
			soup = BeautifulSoup(r,'lxml')
			i=0
			text = soup.find_all("div", class_="rev-text mbot0 ")
			for element in text:
				data.append({'text':element.get_text().split('\n')[2].strip()})

				# print element.get_text().split('\n')[2].strip()
			rating = soup.find_all("div", class_="rev-text mbot0 ")
			for element in rating:
				complete_rating = str(element.div['aria-label'].split(' ')[1])
				data[i].update({'rating':complete_rating})
				data[i].update({'title':None})
				i = i + 1
			i = 0
			url = soup.find_all("div", class_="fs12px pbot0 clearfix")
			for element in url:
				data[i].update({'url':element.a['href']})
				data[i].update({'id':element.a['href'].split('/')[-1]})
				data[i].update({'date':str(element.a.time['datetime'].split(' ')[0])})
				data[i].update({'promotes': None})
				i = i + 1
			user_name = soup.find_all("div", itemprop="name")
			for element in user_name:
				data[i].update({'user':{'name': element.a.get_text().strip()}})
				i = i + 1
			reviews_count = soup.find_all("span", class_="grey-text fontsize5 nowrap")
			for element in reviews_count:
				data[i]['user'].update({'reviews_count':(element.get_text().strip().split(',')[0]).split(' ')[0]})
				data[i]['user'].update({'location':None})
				i = i + 1
			dct['url'] = self.restaurant_url		
			dct['reviews'] = data
			dct['source'] = "zomato"
			dct['name'] = soup.find('h1',itemprop='name').a.get_text().strip()
			dct['location'] = soup.find('div',class_='resinfo-icon').span.span.get_text()
			dct['city']  = soup.find('span',id='location_input_sp').get_text()
			dct['address'] = soup.find('div',class_='resinfo-icon').span.get_text()
			dct['img_url'] = None
			dct['rating'] = soup.find('div',itemprop="ratingValue").get_text().split('/')[0].strip()
			dct['votes'] = soup.find('span',itemprop='ratingCount').get_text()
			dct['cusinies'] = soup.find('div',class_='res-info-cuisines clearfix').a.get_text().strip()
			# tmp_string = str(dct['name'] + '.json')
			# with open("url_not_found/"+tmp_string,'w') as b:
			# 	json.dump(dct,b)
			self.rest_reviews = dct
			self.rest_name = dct['name']
			print 'This url',self.restaurant_url,'is Success'
		except Exception,e:
			print e
			print 'This is the url which is not scrapped',self.restaurant_url
