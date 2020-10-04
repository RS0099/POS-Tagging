import csv

word_tag_dict={}

with open('word_tag.csv','r') as file:
	reader=csv.DictReader(file)
	for row in reader:
		word_tag=row["Word_pos"]
		if word_tag not in word_tag_dict.keys():
			word_tag_dict[word_tag]=0
		word_tag_dict[word_tag]=word_tag_dict[word_tag] + 1	

with open('word_tag_freq.csv','w') as file:
	writer =csv.writer(file)
	writer.writerow(['Word_tag','Frequency'])
	for word,freq in word_tag_dict.items():
		writer.writerow([word,freq])
