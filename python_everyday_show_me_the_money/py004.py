txtfile = open('1Q84.txt')

word_count = 0

for line in txtfile:
	newline =  ''.join(c for c in line if c.isalpha() or c ==' ')
	word_list = newline.split()
	word_count += len(word_list)

print 'Word count:', word_count
	
