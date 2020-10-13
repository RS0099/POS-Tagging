import csv
from collections import Counter

path_train = 'word_tag_freq_train.csv' 
path_test = 'word_tag_freq_test.csv'

word_freq_map_train = {}
word_freq_map_test = {}
tag_freq_map_train = {}
tag_freq_map_test = {}


csv_file_train = open(path_train, encoding="utf8")
csv_file_test = open(path_test, encoding="utf8")

for row in csv.reader(csv_file_train, delimiter=','):
    if row[1] != 'Frequency': 
        split = row[0].split("_")
        if(len(split)>1):
            word = split[0].lower()
            if word not in word_freq_map_train:
                word_freq_map_train[word] = int(row[1])
            word_freq_map_train[word] = word_freq_map_train[word] + int(row[1])
            tag = split[1]
            if tag not in tag_freq_map_train:
                tag_freq_map_train[tag] = int(row[1])
            tag_freq_map_train[tag] = tag_freq_map_train[tag] + int(row[1])

print("\n \nTop 10 frequent used words in train set")
for x, y in Counter(word_freq_map_train).most_common(10):
    print(x, y) 

print("\n \nTop 10 frequent used tags in train set")
for x, y in Counter(tag_freq_map_train).most_common(10):
    print(x, y) 

for row in csv.reader(csv_file_test, delimiter=','):
    if row[1] != 'Frequency': 
        split = row[0].split("_")
        if(len(split)>1):
            word = split[0].lower()
            if word not in word_freq_map_test:
                word_freq_map_test[word] = int(row[1])
            word_freq_map_test[word] = word_freq_map_test[word] + int(row[1])
            tag = split[1]
            if tag not in tag_freq_map_test:
                tag_freq_map_test[tag] = int(row[1])
            tag_freq_map_test[tag] = tag_freq_map_test[tag] + int(row[1])

print("\n \nTop 10 frequent used words in test set")
for x, y in Counter(word_freq_map_test).most_common(10):
    print(x, y) 


print("\n \nTop 10 frequent used tags in test set")
for x, y in Counter(tag_freq_map_test).most_common(10):
    print(x, y) 
