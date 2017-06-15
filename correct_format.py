from bs4 import BeautifulSoup
import urllib
import json

dct = {}
dct['source'] = "trip advisor"
class Correct_Format():
	def __init__(self,restaurant_url,remainig_data,restaurant_name,message):
		self.restaurant_url = restaurant_url
		self.remainig_data = remainig_data
		self.restaurant_name = restaurant_name
		self.message = message
		self.Fields()
	def Fields(self):
		try :
			making_https_request = urllib.urlopen(self.restaurant_url).read()
			soup = BeautifulSoup(making_https_request,'lxml')
			# name = soup.find('h1',id='HEADING').get_text().strip()
			dct['name'] = soup.find('h1',id='HEADING').get_text().strip()
			dct['url'] = self.restaurant_url
			#for restaurant name
			# rest_name = soup.find('div',class_= 'heading_name_wrapper')
			# dct['name'] = rest_name.h1.get_text().strip()
			#For rating of restaurant
			rating = soup.find('div',class_= 'rs rating')
			dct['rating'] = rating.span.img['content']
			#For Number of reviews
			no_of_reviews = soup.find('div',class_= 'rs rating')
			if no_of_reviews != None:
				dct['votes'] = no_of_reviews.a['content']
			else:
				dct['votes'] = None
			#For Address
			address = soup.find('span',class_='format_address')
			dct['address'] = address.get_text()
			location = soup.find('ul',class_='detailsContent')
			#For Image_Url
			# photo = soup.find('div',class_='flexible_photo_wrap restaurant')
			dct['img_url'] = None
			#For Location
			location = soup.find_all('span',itemprop='title')
			location_string = ''
			for loc in range(0,len(location)-1):
				location_string += location[loc].get_text() + ' '
			dct['location'] = location_string
			#For Cuisine
			cuisine = soup.find('div',class_='detail separator')
			dct['cuisine'] = cuisine.get_text().strip()
			if len(dct['cuisine']) == 0:
				dct['cuisine'] = None
			#For city
			city = soup.find('span',class_='locality')
			dct['city'] = ' '.join(city.get_text().split(' ')[:-2])
			self.remainig_data = dct
			self.message = None
		except Exception,e:
			print e
			print "Not valid hotel"
			self.message = "Not a valid hotel"
			