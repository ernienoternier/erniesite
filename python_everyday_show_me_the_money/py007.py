#code count


from os import  listdir
from os.path import isfile, join, splitext

files = [f for f in listdir('.') if isfile(join('.', f))]
print files

print 'line_count', 'comment_count', 'null_count'

for f in files:
	

	line_count = 0 
	comment_count = 0
	null_count = 0
	if not splitext(f)[1] == '.py':
		continue
	print f
	for line in open(f):
		if len(line.strip())==0:
			null_count+=1
		elif line.strip()[0] == '#':
			comment_count +=1
		else:
			line_count+=1

	print line_count, comment_count, null_count
		
