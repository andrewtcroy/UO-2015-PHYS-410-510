f = open ('hello.txt')
content = f.readlines()
for line in content:
	print line
f.close()