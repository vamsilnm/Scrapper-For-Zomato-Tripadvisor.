from bs4 import BeautifulSoup
import urllib
import json
import csv

count = 0
not_match = [['url','name_in_sheet','name_in_site']]
with open('TA_lookup.csv','r') as read:
	file = csv.reader(read,delimiter=';')
	for row in file:
		# print row[0]
		print 'Processing is being done...'
		if row[0] != 'None' and row[0] != 'url':
			# print row[0]
			making_https_request = urllib.urlopen(row[0]).read()
			soup = BeautifulSoup(making_https_request,'lxml')
			name = soup.find('h1',id='HEADING').get_text().strip()
			# print name
			if (''.join(name.split(' '))).lower() == (''.join(row[1].split(' '))).lower():
				print 'Matched'
				count += 1
			else:
				not_match.append([row[0],row[1],name])
		print 'Out'
	with open('not_match.csv','w') as myfile:
		print 'I am here'
		write = csv.writer(myfile,delimiter=';') 
		write.writerows(not_match)

