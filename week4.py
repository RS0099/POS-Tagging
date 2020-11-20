import csv
from collections import Counter

path = 'word_tag_test_freq.csv'
word_tag = list(csv.reader(open(path, encoding="utf8")))

word_tag_freq = {}
word_freq = {}
tag_freq = {}
word_tag_prob = {}

for row in word_tag[1:]:
	word = row[0].split("_")[0]
	if word not in word_freq: 
		word_freq[word] = 0
		word_tag_freq[word] = {}
		word_tag_prob[word] = {}	  
	word_freq[word] = word_freq[word] + int(row[1])
	for tag in row[0].split("_")[1].split("-"):			
		if tag not in word_tag_freq[word]:
			word_tag_freq[word][tag] = int(row[1])
		else :
			word_tag_freq[word][tag] = word_tag_freq[word][tag] + int(row[1])

for i in word_tag_freq:
	for j in word_tag_freq[i]:
		word_tag_freq[i][j] = word_tag_freq[i][j] / word_freq[i]

with open('word_tag_test_prob.csv','w',encoding="utf8", newline='') as file:
	writer =csv.writer(file)
	writer.writerow(['Word','Tag','Prob'])
	for word in word_tag_freq:
		for tag in word_tag_freq[word]:	
			writer.writerow([word,tag,format(word_tag_freq[word][tag], '.20f')])

