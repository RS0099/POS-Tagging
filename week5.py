import csv
from collections import Counter

path = 'word_tag_train_freq.csv' ## A CSV file containing frequency of certain word_tag in the train dataset+
word_tag = list(csv.reader(open(path, encoding="utf8")))

word_tag_prob = {} ## 2D Dictionary where word_tag_probability[word][tag] = P(tag|word)
word_freq = {} ## 1D Dictionary where word_freq[word] = total occurences of word over train dataset
tag_freq = {} ## 1D Dictionary where tag_freq[tag] = total occurences of tag over train dataset
all_tags = set() ## A set of all possible tags, excluding ambiguous tags

for row in word_tag[1:]:
	word = row[0].split("_")[0]
	if word not in word_freq: 
		word_freq[word] = int(row[1])
		word_tag_prob[word] = {}
		word_tag_prob[word] = {}
	else :
		word_freq[word] = word_freq[word] + int(row[1])  
	for tag in row[0].split("_")[1].split("-"):	
		if tag not in word_tag_prob[word]:
			all_tags.add(tag)
			word_tag_prob[word][tag] = int(row[1])
		else :
			word_tag_prob[word][tag] = word_tag_prob[word][tag] + int(row[1])

for i in word_tag_prob:
	for j in word_tag_prob[i]:
		word_tag_prob[i][j] = word_tag_prob[i][j] / word_freq[i]

def get_tag(word):
	most_prob = 0
	expected_tag = ""
	if word in word_tag_prob :
		for trial_tag in word_tag_prob[word]:
			if word_tag_prob[word][trial_tag] > most_prob :
				most_prob = word_tag_prob[word][trial_tag]
				expected_tag = trial_tag
	# if(expected_tag==""):
		# return "NN1"
	return expected_tag

hit = 0
miss = 0

confusion_matrix = {}

# print(len(all_tags)) 

cnt = 0

for i in sorted(all_tags):
	confusion_matrix[i] = {}
	for j in sorted(all_tags):
		confusion_matrix[i][j] = 0

with open('word_tag_test.csv','r',encoding="utf8", newline='') as file:
	reader=csv.DictReader(file)
	for row in reader:
		word_tag=row["Word_pos"]
		word = word_tag.split('_')[0]
		tag = word_tag.split('_')[1]
		most_prob = 0
		expected_tag = get_tag(word)
		flag = 0
		expected_tag.replace(" ", "") 
		for acctag in tag.split('-'):
			acctag.replace(" ", "") 
			if(expected_tag==acctag):
				flag = 1	
			cnt = cnt + 1
		for acctag in tag.split('-'):
			if acctag not in confusion_matrix :
				confusion_matrix[acctag] = {}			
			if expected_tag not in confusion_matrix[acctag] :
				confusion_matrix[acctag][expected_tag] = 0
			confusion_matrix[acctag][expected_tag] = confusion_matrix[acctag][expected_tag] + 1
		if(flag==1):
			hit = hit + 1
		else:
			miss = miss + 1

print("accuracy = " , hit/(hit+miss)*100)
print("\n")
print(cnt)
sorted_matrix = {}

wrongtaga = {}
wrongtagb = {}

for i in confusion_matrix:
	for j in confusion_matrix[i]:
		if(i!=j):
			sorted_matrix[confusion_matrix[i][j]] = i + " " + j
			if i not in wrongtaga:
				wrongtaga[i] = 0
			if j not in wrongtagb:
				wrongtagb[j] = 0
				
			wrongtaga[i] = wrongtaga[i] + confusion_matrix[i][j]
			wrongtagb[j] = wrongtagb[j] + confusion_matrix[i][j]

# print(wrongtaga)
# print(wrongtagb)


# for i in sorted(sorted_matrix.keys()):
# 	print(i,sorted_matrix[i])

# for i in sorted(wrongtaga.items(), key=lambda kv: kv[1]):
# 	print(i)


# print("\n\n\n")

# for i in sorted(wrongtagb.items(), key=lambda kv: kv[1]):
# 	print(i)

# print(confusion_matrix)