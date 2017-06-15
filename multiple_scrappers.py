


from correct_format import Correct_Format 
# from tripadvisor_spider.spiders import TripadvisorSpider
import os
import sys
import json
import csv

# if __name__ == "__main__":
# 	dct = {}
	# a = Correct_Format('https://www.tripadvisor.in/Restaurant_Review-g304555-d2142625-Reviews-Peacock_Roof_Top_Restaurant-Jaipur_Jaipur_District_Rajasthan.html',dct)
# 	print a.remainig_data
	                                 
if __name__ == "__main__":
	option = sys.argv[1]
	i = 0
	msg = ''
	if option=="one":
		#Below code is for calling only once for a specified url
		dct = {}
		a = Correct_Format('https://www.tripadvisor.in/Attraction_Review-g297654-d2178303-Reviews-Mayur_Baug-Pune_Maharashtra.html',dct,'Vamsi',msg)
		if a.message == None :
			os.system('scrapy crawl tripadvisor_spider -o data_1/new.json -t json -a start_url="https://www.tripadvisor.in/Attraction_Review-g297654-d2178303-Reviews-Mayur_Baug-Pune_Maharashtra.html" -s LOG_LEVEL=INFO')
		
			print 'In if'
			with open('data_1/new.json','r') as read:
				reviews_3 = json.load(read)
				a.remainig_data['reviews'] = reviews_3
			with open('data_1/new.json','w') as write:
				json.dump(a.remainig_data,write)
		else:
			print "In else"
			print "Not a valid Hotel"
	elif option=="all":
	# Below code is for calling from csv file
		
		with open('TA_lookup_modified.csv','r') as read:
			data = csv.reader(read,delimiter=';')
			for row in data:
				# print row
				i += 1
				if row[0] != "None" and row[0] != "url":
					dct = {}
					a = Correct_Format(row[0],dct,row[1],msg)
					if a.message == None:
						try :
							json_file_name = '_'.join(row[1].split(' ')) + '_'+str(i)+ '.json'
							cmd = 'scrapy crawl tripadvisor_spider -o data/"'+json_file_name+'" -t json -a start_url="'+row[0]+'" -s LOG_LEVEL=INFO'
							print 'RUNNING: '+cmd
							os.system(cmd)
							with open("data/"+json_file_name,'r') as read:
								reviews = json.load(read)
								a.remainig_data['reviews'] = reviews
							with open("data/"+json_file_name,'w') as write:
								json.dump(a.remainig_data,write)
						except Exception,e:
							print e
					else:
						# print e
						continue
				print "The row processing is -"+str(i)


