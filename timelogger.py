import csv

# user, book, date, start_time, end_time, bookmark_page, bookmark_line, next_step, comment

with open('example.csv') as csvfile:
	tlreader = csv.reader(csvfile)
	for row in tlreader:
		print ','.join(row)
