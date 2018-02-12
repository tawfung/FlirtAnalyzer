import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def most_common(lst):
    return max(set(lst), key=lst.count)

var_input = open("read.txt").read()

var_input = re.sub(r'[\W\s\d]',' ', var_input)
input_tokenized = word_tokenize(var_input, 'english')
filtered_words = [word for word in input_tokenized if word not in stopwords.words('english')]

print(filtered_words)

emotion_count = []

for i in range(0, len(filtered_words)):
    with open('em.txt') as f:
        for line in f:
            finaline = line.strip()
            keym = re.search("'" + filtered_words[i] + "':\s'", finaline)
            if keym:
                valuem = re.findall(":\s'.*", finaline)
                newstr = str(valuem)
                finalvalue = re.sub(r'[\W\s]',' ', newstr)
                emotion_count.append(finalvalue.strip())

print("The most comman mood is: "+ most_common(emotion_count))