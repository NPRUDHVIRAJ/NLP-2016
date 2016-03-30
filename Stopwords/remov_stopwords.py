import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize 

# defining possible shortened forms of frequent words
def remove_incomplete_forms(line):           
    
    line = re.sub("'m", "am", line)
    line = re.sub("'s", "is", line)
    line = re.sub("'d", "would", line)
    line = re.sub("'ll", "will", line)
    line = re.sub("'ve", "have", line)
    line = re.sub("'re", "are", line)
    line = re.sub("won't", "would not", line)
    line = re.sub("doesn't", "does not", line)        
    line = re.sub("n't", "not", line)
    line = re.sub("would't", "would not", line)
    line = re.sub("'t", "not", line)
    line = re.sub(' [^A-Za-z ]+', '', line)
    
    return line

# this function takes two text files as arguments and creates a new text file after removing the Stopwords_set. 
def remove_Stopwords(data, Stopwords): 

    Stopwords_set = set(stopwords.words("english"))
    #for y in Stopwords_set:
        #print(y)
        
    reviews = open(data, "r")
    output = open("data_without_Stopwords.txt", "w")

    for line in reviews:
        
        line = remove_incomplete_forms(line) # removes the common short forms from the line for consistency

        words_line = line.split();

        for w in words_line:
            if w.lower() not in Stopwords_set:
                if w== '-' or w=='+':
                    output.write(w)
                elif w== '.':
                    output.write(" ")
                else:
                    output.write(" " + w.lower())
                
                
       # converts the word to lower case first, and then writes to the file.
            
        output.write("\n")
        
    reviews.close()
    output.close()
    return
    

remove_Stopwords("data.txt", "Stopwords.txt")  
print("Program Successfully Executed!")
