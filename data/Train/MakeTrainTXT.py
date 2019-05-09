import os

f = open('MavicTrain.txt', 'w')

for file_name in os.listdir('Images'):
    f.write('data/Train/Images/'+ file_name + '\n')

'''for file_name in sorted(os.listdir('Labels')):
    if os.path.getsize("Labels/"+file_name) == 0:
        os.remove("Labels/"+file_name)'''

f.close()
