import random
import MySQLdb
code_list = []
source_list = []
def make_code():
	str_list = [] 
	for r in range(0,30):
		ri = random.randint(0,35)
		# print ri
		# print source_list[ri]
		str_list.append(source_list[ri])
	return ''.join(str_list)

def get_next_code():
	next_code = make_code()
	if next_code in code_list:
		print "duplicated"
		return get_next_code()
	else:
		return next_code

for c in range(97,123):
	source_list.append(chr(c))
for i in range(0,10):
	source_list.append(str(i))

# print source_list, len(source_list)
for cd in range(0,200):
	code = get_next_code()
	code_list.append(code)
	print code


######
print '*'*8
for code in code_list:
	print code

print len(code_list)

print len(list(set(code_list)))



######

conn = MySQLdb.connect(host='localhost', user='root', passwd='888888', db='test')
cs = conn.cursor();
for code in code_list:
	cs.execute("insert into code values('%s')" % code)
#cs.execute("insert into code values('test')")
conn.commit()

