import random
code_list = []
source_list = []
for c in range(97,123):
	source_list.append(chr(c))
for i in range(0,10):
	source_list.append(str(i))

# print source_list, len(source_list)
for cd in range(0,200):
	str_list = [] 
	for r in range(0,31):
		ri = random.randint(0,35)
		# print ri
		# print source_list[ri]
		str_list.append(source_list[ri])
	code_list.append(''.join(str_list))

######
for code in code_list:
	print code

print len(code_list)
