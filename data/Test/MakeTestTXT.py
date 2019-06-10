import os

f = open('MavicTest.txt', 'w')

for file_name in os.listdir('Images'):
    f.write('data/Test/Images/'+ file_name + '\n')

'''for file_name in sorted(os.listdir('Labels')):
    if os.path.getsize("Labels/"+file_name) == 0:
        os.remove("Labels/"+file_name)'''

f.close()
