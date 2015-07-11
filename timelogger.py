import csv
from datetime import datetime

# user, book, date, start_time, end_time, bookmark_page, bookmark_line, next_step, comment

with open('example.csv') as csvfile:
	tlreader = csv.reader(csvfile)
	for row in tlreader:
		print ','.join(row)



def time_duration():
	h1 = '17:05'
	h2='18:15'
	FMT = '%H:%M'
	t1=datetime.strptime(h1, FMT)
	t2=datetime.strptime(h2, FMT)
	df =  (t2-t1).seconds/60
	print (t2-t1)
	print df


time_duration()


