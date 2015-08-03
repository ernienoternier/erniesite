#find the most import word in 1Q84

txtfile = open('1Q84.txt')

count_dict ={}

for line in txtfile:
	newline = ''.join(c for c in line if c.isalpha() or c ==' ')
	word_list = newline.split()
	for word in word_list:
		if word.upper() in count_dict:
			count_dict[word.upper()]+=1
		else:
			count_dict[word.upper()]=1

# print count_dict
sorted_dict = sorted(count_dict, key=count_dict.get, reverse=True)
for word in sorted_dict:
	print word, count_dict[word]
