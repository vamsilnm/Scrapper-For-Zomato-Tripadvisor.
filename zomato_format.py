import json
from bs4 import BeautifulSoup
import urllib

class Zomato_Reviews_Format():
	def __init__(self,filenmae):
		self.filenmae = filenmae
		self.Format()
	def Format(self):
		with open(self.filenmae,'r') as k:
			l = json.load(k)
			for i in l['reviews']:
				if not 'rating' in i:
					i.update({'rating':None})
				if not 'title' in i:
					i.update({'title':None})
				if not 'url' in i:
					i.update({'url':None})
				if not 'date' in i:
					i.update({'date':None})
				if not 'promotes' in i:
					i.update({'promotes':None})
				if not 'comments' in i:
					i.update({'comments':None})
				if not 'user' in i:
					i.update({'user':None})
				if not 'name' in i['user']:
					i['user'].update({'name':None})	
				if not 'reviews_count' in i['user']:
					i['user'].update({'reviews_count':None})
				if not 'followers_count' in i['user']:
					i['user'].update({'followers_count':None})
				if not 'url' in i['user']:
					i['user'].update({'url':None})
				if not 'level' in i['user']:
					i['user'].update({'level':None})
				if not 'is_verified' in i['user']:
					i['user'].update({'is_verified':None})
					

			# for v in l['reviews']:
			# 	if v['user']['url'] != None:
			# 		f = urllib.urlopen(v['user']['url']).read()
			# 		soup = BeautifulSoup(f,'lxml')
			# 		loc_element = soup.find("div", class_="meta ")
			# 		v['user'].update({'location':loc_element.get_text().strip()})

		with open(self.filenmae,'w+') as p:
			json.dump(l,p)








