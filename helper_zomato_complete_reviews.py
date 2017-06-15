from zomato_complete_reviews import Zomato_Complete_Scrapper
import csv

if __name__ == '__main__':
	i = 0
	none = 0
	Zomato_Complete_Scrapper('https://www.zomato.com/jaipur/kebabs-curries-company-malviya-nagar/reviews','sample_1')
	# with open('ZT_lookup.csv','rb') as csvfile:
	# 		spamreader = csv.reader(csvfile, delimiter=';',)
	# 		for row in spamreader:
	# 			if row[0] != "None" and  row[0] != "url" and i >= 244:
	# 				# print row[0],row[1]
	# 				Zomato_Complete_Scrapper(row[0],str(i)+'_'+row[1])
	# 			else :
	# 				none += 1
	# 			i += 1
