import json
import glob


for filename in glob.glob('*.json'):
	with open(filename,'r') as read:
		reviews = json.load(read)
		if 'source' not in reviews:
			print 'Source is not there'
		if 'name' not in reviews:
			print 'name is not there'
		if 'location' not in reviews:
			print 'location is not there'
		if 'city' not in reviews:
			print 'city is not there'
		if 'address' not in reviews:
			print 'address is not there'
		if 'url' not in reviews:
			print 'url is not there'
		if 'img_url' not in reviews:
			print 'img_url is not there'
		if 'rating' not in reviews:
			print 'rating is not there'
		if 'votes' not in reviews:
			print 'votes is not there'
		for review in reviews['reviews']:
			if 'review_id' not in review:
				print filename,'id is not there'
			if 'review_id' in review:
				if len(review['review_id']) == 0:
					print filename,'id is null'
			if 'date' not in review:
				print filename,'date is not there'
			if 'date' in review:
				if len(review['date']) == 0:
					print filename,'date is null'
			if 'rating' not in review:
				print filename,'rating is not there'
			if 'rating' in review:
				if len(review['rating']) == 0:
					print filename,'rating is null'
			if 'title' not in review:
				print filename,'title is not there'
			if 'title' in review:
				if len(review['title']) == 0:
					print filename,'title is null'
			if 'text' not in review:
				print filename,'text is not there'
			if 'text' in review:
				if len(review['text']) == 0:
					print filename,'text is null'
			if 'url' not in review:
				print filename,'url is not there'
			if 'url' in review:
				if len(review['url']) == 0:
					print filename,'url is null'
			if 'promotes' not in review:
				print filename,'promotes is not there'
			if 'comments' not in review:
				print filename,'comments is not there'

	# with open(filename,'w') as write:
	# 	json.dump(reviews,write)
		# print len(reviews['reviews'])