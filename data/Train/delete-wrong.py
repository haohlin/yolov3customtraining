import os

a = 0
f = open('wrong.txt', 'r')
lines = list(filter(None, f.read().split('\n')))
for line in lines:
	os.remove('Images/'+line)
	os.remove('Labels/'+line.replace('jpg','txt'))
	a+=1
	print(a)
