from bs4 import BeautifulSoup
import urllib
import json
from datetime import datetime 
# data = []
# dct = {}

class Tripadvisor_Beautiful_Scrapper():

	def __init__(self,restaurant_url):
		self.restaurant_url = restaurant_url
		self.Trip_Scrapper()
	def Trip_Scrapper(self):
		try:
			data = []
			dct = {}
			r = urllib.urlopen(self.restaurant_url).read()
			soup = BeautifulSoup(r,'lxml')
			i=0
			text = soup.find_all("div", class_="entry")
			for element in text:
				data.append({'text':element.p.get_text()})
			rating = soup.find_all("div", class_="rating reviewItemInline")
			# print 'text is success'
			for element in rating:
				complete_rating = element.span.img['alt'][0]
				data[i].update({'rating':complete_rating})
				i = i + 1
			i = 0
			# print 'rating is success'
			title = soup.find_all("span", class_="noQuotes")
			for element in title:
				data[i].update({'title':element.get_text()})
				print 'I am in titles'
				i = i + 1
				if i>len(text):
					break
			i = 0
			url = soup.find_all("div", class_="quote")
			for element in url:
				data[i].update({'url':'https://www.tripadvisor.in'+element.a['href']})
				data[i].update({'id':('https://www.tripadvisor.in'+element.a['href']).split('-')[3]})
				# item['review_id'] = str(item['url'].split('-')[3])
				i = i + 1
			i = 0
			# print 'url is success'
			# print date[0]['title']
			# date = soup.find_all("span", class_="ratingDate relativeDate")
			# for element in date:
			# 	data[i].update({'date':datetime.strptime(element['title'],"%d %B %Y").strftime("%Y-%m-%d")})
			# 	# item['date'] = datetime.strptime(item['date'], "%d %B %Y").strftime("%Y-%m-%d")
			# 	i = i + 1
			date_1 = soup.find_all("span", class_="ratingDate")
			print len(date_1)
			for element in date_1:
				print element.get_text().split(' ')[-1]
				try:
					data[i].update({'date':datetime.strptime(element['title'],"%d %B %Y").strftime("%Y-%m-%d")})
					# i = i + 1
				except:
				# if element['title'] == None:
					print element.get_text()
					data[i].update({'date':datetime.strptime(' '.join(element.get_text().strip().split(' ')[1:]),"%d %B %Y").strftime("%Y-%m-%d")})
					# item['date'] = datetime.strptime(item['date'], "%d %B %Y").strftime("%Y-%m-%d")
						# i = i + 1
				i = i +1
			i = 0

			promotes = soup.find_all("div", class_="helpfulVotesBadge badge no_cpu")
			for element in promotes:
				data[i].update({'promotes': element.span.get_text().strip().split(' ')[0]})
				print 'I am in promotes'
				data[i].update({'comments':None})
				i = i + 1
				if i == 10:
					break
			i = 0
			# print 'promotes is success'
			user_name = soup.find_all("div", class_="username mo")
			# print 'this is lenof user_loc',len(user_name)
			for element in user_name:
				data[i].update({'user':{'name': element.span.get_text()}})
				print 'I am in username'
				i = i + 1
				if i == 10:
					break

			i = 0
			# print 'username is also success'
			user_loc = soup.find_all("div", class_="location")
			# print 'this is lenof user_loc',len(user_loc)
			for element in user_loc:
				if i >= len(user_name):
					break
				data[i]['user'].update({'location': element.get_text().strip()})
				print 'I am in user_loc'
				i = i + 1

				if i == 10:
					break
			# print 'this is i',i
			i = 0
			# print 'username is also success'
			reviews_count = soup.find_all("div", class_="reviewerBadge badge")
			for element in reviews_count:
				data[i]['user'].update({'reviews_count':element.span.get_text().split(' ')[0]})
				print 'I am in reviews_count'
				i = i + 1
				if i == 10:
					break
			dct['url'] = self.restaurant_url		
			dct['reviews'] = data
			dct['source'] = "trip advisor"
			dct['name'] = soup.find('h1',id='HEADING').get_text().strip()
			print 'I am in rest_name'
			rating = soup.find('div',class_= 'rs rating')
			dct['rating'] = rating.span.img['content']
			no_of_reviews = soup.find('div',class_= 'rs rating')
			if no_of_reviews != None:
				dct['votes'] = no_of_reviews.a['content']
			else:
				dct['votes'] = None
			address = soup.find('span',class_='format_address')
			dct['address'] = address.get_text()
			print 'I am in address'
			dct['img_url'] = None
			try:
				cuisine = soup.find('div',class_='detail separator')
				print 'This is in middile of cuisine'
				dct['cuisine'] = cuisine.get_text().strip()
			except:
				dct['cuisine'] = None
					
			# city = soup.find('span',class_='locality')
			# dct['city'] = ' '.join(city.get_text().split(' ')[:-2])
			city = soup.find('div',id='GEO_SCOPE_CONTAINER')
			try:
				dct['city'] = city.input['value'].split(',')[0]
			except:
				dct['city'] = None
			try:
				dct['location'] = soup.find('span',class_='extended-address').get_text()
			except:
				dct['location'] = soup.find('span',class_='street-address').get_text()
				print dct['location']
				print dct['location'].split(',')
				if len(dct['location'].split(',')) > 1:
					print 'Got Inside'
					dct['location'] = str(dct['location'].split(',')[1])
			tmp_string = str(dct['name'] + '.json')
			with open("ta_failed/"+tmp_string,'w') as b:
				json.dump(dct,b)
			print 'this is success',self.restaurant_url
			# with open(tmp_string,'w') as b:
			# 	json.dump(dct,b)
			# print 'this is success',self.restaurant_url
		except Exception,e:
			print e
			print 'this is restaurant failed',self.restaurant_url
