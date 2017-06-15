import glob
import os
import json
from bs4 import BeautifulSoup
import urllib

# for filename in glob.glob('*.json'):
# 	statinfo = os.stat(filename)
# 	if statinfo.st_size == 1:
# 		os.remove(filename)
# 	else:
# 		with open(filename,'r') as read:
# 			reviews = json.load(read)
# 			if len(reviews['city']) == 0:
# 				making_https_request = urllib.urlopen(reviews['url']).read()
# 				soup = BeautifulSoup(making_https_request,'lxml')
# 				city_new = soup.find('a',class_='breadcrumb_link')
# 				reviews['city'] = city_new.span.get_text().strip()

# 				# print reviews['url']
# 				with open(filename,'w') as write:
# 					json.dump(reviews,write)
for filename in glob.glob('*.json'):
	statinfo = os.stat(filename)
	if statinfo.st_size == 1:
		print 'Sorry there is dicrepency in'
		with open(filename,'r') as read:
			reviews = json.load(read)
			print reviews['url']
	with open(filename,'r') as read:
		reviews = json.load(read)
		if len(reviews['city']) == 0:
			print 'Sorry there is discrepency in'
			print reviews['url']
