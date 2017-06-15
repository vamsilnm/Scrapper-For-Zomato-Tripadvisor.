from datetime import datetime 
import glob
import json
from dateutil.parser import parse
# dt = parse('Mon Feb 15 2010')
# print(dt)
# # datetime.datetime(2010, 2, 15, 0, 0)
# print(dt.strftime('%d/%m/%Y'))
# # 15/02/2010
for file_name in glob.glob('*.json'):
	with open(file_name,'r') as read:
		reviews = json.load(read)
		for review in reviews['reviews']:
			if 'date' in review:
				if type(review['date']) == list:
					# date = parse(''.join(review['date'])
					# review.update({'date':parse(''.join(review['date']))})
					# review.update({'date':date.strftime('%Y-%m-%d')})
					review.update({'date':datetime.strptime((''.join(review['date']).strip()), "%d %B %Y").strftime("%Y %m %d")})
				else:
					review.update({'date':datetime.strptime(review['date'], "%d %B %Y").strftime("%Y %m %d")})
			if 'url' in review:
				review.update({'review_id': str(review['url'].split('-')[3])})
