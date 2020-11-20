import csv
from collections import Counter

path = 'word_tag_train_freq.csv'
word_tag = list(csv.reader(open(path, encoding="utf8")))

word_freq_map = {}
tag_freq_map = {}
word_tag_map = {}

for row in word_tag[1:]:
    word = row[0].split("_")[0].lower()
    if word not in word_freq_map: 
        word_freq_map[word] = int(row[1])
    else :
        word_freq_map[word] = word_freq_map[word] + int(row[1])    
    for tag in row[0].split("_")[1].split("-"):
        if tag not in tag_freq_map:
            tag_freq_map[tag] = int(row[1])
        else :
            tag_freq_map[tag] = tag_freq_map[tag] + int(row[1])

for x, y in Counter(word_freq_map).most_common(12):
    if(x[0]>='a' and x[0]<='z'):
        print(x, y)

print()

for x, y in Counter(tag_freq_map).most_common(10):
    print(x, y) 

print()

path = 'word_tag_test_freq.csv'
word_tag = list(csv.reader(open(path, encoding="utf8")))

word_freq_map = {}
tag_freq_map = {}
word_tag_map = {}

for row in word_tag[1:]:
    word = row[0].split("_")[0].lower()
    if(len(word) > 4 and word[0]=='t' and word[1]=='h' and word[2] == 'a' and word[3] == 't' and word[4] == ' '):
        print(row)
    if word not in word_freq_map: 
        word_freq_map[word] = int(row[1])
    else :
        word_freq_map[word] = word_freq_map[word] + int(row[1])    
    for tag in row[0].split("_")[1].split("-"):
        if tag not in tag_freq_map:
            tag_freq_map[tag] = int(row[1])
        else :
            tag_freq_map[tag] = tag_freq_map[tag] + int(row[1])

for x, y in Counter(word_freq_map).most_common(12):
    if(x[0]>='a' and x[0]<='z'):
        print(x, y)

print()

for x, y in Counter(tag_freq_map).most_common(10):
    print(x, y) 
