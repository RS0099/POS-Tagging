def dfs(x):
	flag = 0
	if x.tag== 'w' or x.tag == 'c':
		if(x.text!=None):
			string = x.text.strip() + "_" + x.attrib.get('c5')
			row = row = [string]
			row_list_test.append(row)
	else :
		for y in x:
			dfs(y)

#############################################################################

import os
import csv
import xml.etree.ElementTree as ET 	
from fnmatch import fnmatch

root_train = 'Train-corups/'
root_test = 'Test-corpus/'
pattern = "*.xml"

file_paths_train = list()
file_paths_test = list()
row_list_train = [["Word_pos"]]
row_list_test = [["Word_pos"]]

# folders = os.listdir(path = root_train)
# stack = []

# for folder in folders:
# 	for file in os.listdir(path = os.path.join(root_train,folder)):	
# 		file_paths_train.append(os.path.join(os.path.join(root_train,folder),file))

# for file_path in file_paths_train:
# 	for a in ET.parse(file_path).getroot().findall('wtext'):
# 		dfs(a)

# with open('word_tag_train.csv','w') as file:
# 	writer=csv.writer(file)
# 	writer.writerows(row_list_train)


folders = os.listdir(path = root_test)

for folder in folders:
	for file in os.listdir(path = os.path.join(root_test,folder)):	
		file_paths_test.append(os.path.join(os.path.join(root_test,folder),file))

for file_path in file_paths_test:
	for a in ET.parse(file_path).getroot().findall('wtext'):
		dfs(a)

with open('word_tag_test.csv','w') as file:
	writer=csv.writer(file)
	writer.writerows(row_list_test)