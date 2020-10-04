#!/usr/bin/env python3

import xml.dom.minidom as xd
import os
import csv
from xml.dom.minidom import parse
from fnmatch import fnmatch

root='/home/rs/AI_project/Assignment-files/Train-corups/'
pattern="*.xml"

all_file_paths=list()
row_list=[["S.No","Word_pos"]]
n=1

folders=os.listdir(path=root)
for folder in folders:
	f_path=os.path.join(root,folder)
	
	files=os.listdir(path=f_path)
	for file in files:
		f2_path=os.path.join(f_path,file)
		all_file_paths.append(f2_path)


for file_path in all_file_paths:
	
	DOMTREE =xd.parse(file_path)
	w_tags=DOMTREE.getElementsByTagName("w")

	for w in w_tags:
		word=w.getAttribute("hw")
		tag=w.getAttribute("pos")
		row=[str(n),word+"_"+tag]
		row_list.append(row)
		n=n+1

with open('word_tag.csv','w')as file:
	writer=csv.writer(file)
	writer.writerows(row_list)
