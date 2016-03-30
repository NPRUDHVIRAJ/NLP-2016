import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

output=open("stopwords.txt","w");
stopwords_set=set(stopwords.words("english"))

for w in stopwords_set:
    output.write(str(w))
    output.write("\n")
output.close()


