import os
import csv
import xml.etree.ElementTree as ET 	
from fnmatch import fnmatch

root='/home/rs/AI_project/Assignment-files/Train-corups/'
pattern="*.xml"

all_file_paths=list()

row_list=[["Word_pos"]]
#n=1
folders=os.listdir(path=root)
for folder in folders:
	f_path=os.path.join(root,folder)
	
	files=os.listdir(path=f_path)
	for file in files:
		f2_path=os.path.join(f_path,file)
		all_file_paths.append(f2_path)

string = ""
stack = []

def go_deep(x):
	if x.tag== 'w' or x.tag == 'c':
		string = x.text
		string = string.strip()
		string = string + "_"+x.attrib.get('c5')
		row = row=[string]
		row_list.append(row)
		#n=n+1
		string = ""
	else :
		for y in x:
			go_deep(y)


for file_path in all_file_paths:
	tree = ET.parse(file_path)
	root = tree.getroot()

	for a in root.findall('wtext'):
		go_deep(a)


with open('word_tag_train_2.csv','w')as file:
	writer=csv.writer(file)
	writer.writerows(row_list)