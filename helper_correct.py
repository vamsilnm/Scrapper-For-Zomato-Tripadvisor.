
from correct_format import Correct_Format
import json

if __name__ == "__main__":
	dct = {}
	msg = ''
	a = Correct_Format('https://www.tripadvisor.in/Attraction_Review-g297654-d2178303-Reviews-Mayur_Baug-Pune_Maharashtra.html',dct,'vamsi',msg)
	# with open('a.json','w') as write:
	# 	json.dump(a.remainig_data,write)
	print a.remainig_data