import csv
from collections import Counter

path_train = 'word_tag_train_freq.csv'
word_tag = list(csv.reader(open(path_train, encoding="utf8")))

word_tag_freq_train = {}
word_freq_train = {}
word_tag_prob_train = {}

for row in word_tag[1:]:
	word = row[0].split("_")[0]
	if word not in word_freq_train: 
		word_freq_train[word] = 0
		word_tag_freq_train[word] = {}
		word_tag_prob_train[word] = {}	  
	word_freq_train[word] = word_freq_train[word] + int(row[1])
	for tag in row[0].split("_")[1].split("-"):			
		if tag not in word_tag_freq_train[word]:
			word_tag_freq_train[word][tag] = int(row[1])
		else :
			word_tag_freq_train[word][tag] = word_tag_freq_train[word][tag] + int(row[1])

for i in word_tag_freq_train:
	for j in word_tag_freq_train[i]:
		word_tag_freq_train[i][j] = word_tag_freq_train[i][j] / word_freq_train[i]

with open('word_tag_train_prob.csv','w',encoding="utf8", newline='') as file:
	writer =csv.writer(file)
	writer.writerow(['Word','Tag','Prob'])
	for word in word_tag_freq_train:
		for tag in word_tag_freq_train[word]:	
			writer.writerow([word,tag,format(word_tag_freq_train[word][tag], '.20f')])

path_test = 'word_tag_test_freq.csv'
word_tag = list(csv.reader(open(path_test, encoding="utf8")))

word_tag_freq_test = {}
word_freq_test = {}
word_tag_prob_test = {}

for row in word_tag[1:]:
	word = row[0].split("_")[0]
	if word not in word_freq_test: 
		word_freq_test[word] = 0
		word_tag_freq_test[word] = {}
		word_tag_prob_test[word] = {}	  
	word_freq_test[word] = word_freq_test[word] + int(row[1])
	for tag in row[0].split("_")[1].split("-"):			
		if tag not in word_tag_freq_test[word]:
			word_tag_freq_test[word][tag] = int(row[1])
		else :
			word_tag_freq_test[word][tag] = word_tag_freq_test[word][tag] + int(row[1])

for i in word_tag_freq_test:
	for j in word_tag_freq_test[i]:
		word_tag_freq_test[i][j] = word_tag_freq_test[i][j] / word_freq_test[i]

with open('word_tag_test_prob.csv','w',encoding="utf8", newline='') as file:
	writer =csv.writer(file)
	writer.writerow(['Word','Tag','Prob'])
	for word in word_tag_freq_test:
		for tag in word_tag_freq_test[word]:	
			writer.writerow([word,tag,format(word_tag_freq_test[word][tag], '.20f')])
