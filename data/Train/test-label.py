import os

a = 0
for i, label in enumerate(os.listdir('Labels')):
    #os.rename('labels/'+label, 'labels/%d.txt' % (i+1))
    #if label.replace('txt','jpg') not in os.listdir('images'):
    #    os.remove('labels/' + labels)
     #   a += 1
    f = open('Labels/' + label, 'r')
    lines = list(filter(None, f.read().split('\n')))
    for line in lines:
        box = [float(a) for a in line.split(' ')]
        for x in box[1:]:
	        if x > 1.0:
		        a += 1
    f.close()
print(a)
