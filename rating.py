import json




with open('rating.json', 'w') as v:
	with open('/home/vamsi/tripadvisor/tripadvisor/sample_34.json', 'r') as f:
		sample_34 = json.load(f)
		if sample_34[0] == '2' or sample_34[0] == '1':
			json.dump(rating,sample_34)

