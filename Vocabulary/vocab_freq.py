import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


complete_text_file= open("data_without_Stopwords.txt", "r")
complete_text=complete_text_file.read();

all_words=word_tokenize(complete_text,'english')

freq_dist=FreqDist(all_words)

#print(freq_dist)


output1=open("vocabulary.txt","w")
output2=open("vocab_freq.txt","w")

for word,frequency in freq_dist.most_common(5000):
    if frequency >= 2:
        output1.write(word + "\n")
        output2.write(word + " : " + str(frequency) + "\n")
 

output1.close()
output2.close()

print("voc_freq file created successfully")




    
