import os
import csv
import xml.etree.ElementTree as ET 	
from fnmatch import fnmatch

root='/home/aditya/Downloads/Train-corups/'
pattern="*.xml"

all_file_paths=list()

folders=os.listdir(path=root)
for folder in folders:
	f_path=os.path.join(root,folder)
	
	files=os.listdir(path=f_path)
	for file in files:
		f2_path=os.path.join(f_path,file)
		all_file_paths.append(f2_path)

string = ""

for file_path in all_file_paths:
	tree = ET.parse(file_path)
	root = tree.getroot()
	for c in root.findall('wtext'):
		for d in c.findall('div'):
			for e in d:
				for f in e.findall('s'):
					for g in f:
						tag = g.tag
						if tag == 'w':
							string = " " + g.attrib.get('hw')+"_"+g.attrib.get('pos')
							with open('word_tag_test.txt','a')as file:
								file.write(string)
						elif tag == 'c':
							string = " " + g.text.replace(" ", "")
							with open('word_tag_test.txt','a')as file:
								file.write(string)
				if e.tag == 'head':
					string = '\n'
					with open('word_tag_test.txt','a')as file:
								file.write(string)

	string = '\n'
	with open('word_tag_test.txt','a')as file:
				file.write(string)
