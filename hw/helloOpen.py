f = open ('hello.txt')
content = f.readlines()
for line in content:
	print line
f.close()


#def catfile('hello.txt'):
 # with open('hello.txt') as f:
  #  for line in f:
   #   print line