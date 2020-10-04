import csv
from collections import Counter

path_train = 'word_tag_freq_train.csv' 
path_test = 'word_tag_freq_test.csv'

word_freq_map_train = {}
word_freq_map_test = {}

csv_file_train = open(path_train, encoding="utf8")
csv_file_test = open(path_test, encoding="utf8")

for row in csv.reader(csv_file_train, delimiter=','):
    if row[1] != 'Frequency': 
        if row[0] not in word_freq_map_train:
            word_freq_map_train[row[0]] = int(row[1])
        word_freq_map_train[row[0]] = word_freq_map_train[row[0]] + int(row[1])

print("\n \nTop 10 frequent used words in train set")
for x, y in Counter(word_freq_map_train).most_common(10):
    print(x, y) 

for row in csv.reader(csv_file_test, delimiter=','):
    if row[1] != 'Frequency': 
        if row[0] not in word_freq_map_test:
            word_freq_map_test[row[0]] = int(row[1])
        word_freq_map_test[row[0]] = word_freq_map_test[row[0]] + int(row[1])

print("\n \nTop 10 frequent used words in test set")
for x, y in Counter(word_freq_map_test).most_common(10):
    print(x, y) 

