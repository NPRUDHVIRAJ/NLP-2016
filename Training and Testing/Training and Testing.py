import math
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


i=0
j=25
avg_accuracy=[]
while i<=250 and j<=250:     

        input_data=open("data_without_stopwords.txt","r")
        count_positive=0
        count_negative=0
        count_positive_train=0
        count_negative_train=0
        count_positive_words_train=0
        count_negative_words_train=0

        positive=""
        negative=""
        train=""
        train_positive=""
        train_negative=""
        test=[]
        theoritical=[]
        experimental=[]
        counts=0

        for line in input_data:
            words=line.split()
            counts =counts + 1
            
            if words[0]=='+':
                positive += line
                count_positive +=1
            elif words[0]=='-':
                negative += line
                count_negative +=1
            if words[0]=='+' and count_positive > i and count_positive <= j:
                test += words
                theoritical.append(1)
            elif words[0]=='-' and count_negative > i and count_negative <= j:
                test += words
                theoritical.append(0)
                
            else:
                train += line
                if words[0]=='+':
                    count_positive_train += 1
                    count_positive_words_train += (len(words)-1)
                    train_positive += line
                elif words[0]=='-':
                    count_negative_train += 1
                    count_negative_words_train += (len(words)-1)
                    train_negative += line

        
        words_train=train.split()
        words_train.sort()

        words_train_positive= train_positive.split()
        words_train_positive.sort()

        words_train_negative= train_negative.split()
        words_train_negative.sort()


        vocab=[]
        freq=[]
        vocabulary=[]
        frequency=[]

        count=0

        for k in range(0,len(words_train)):
            if count==0:
                temp=words_train[k]
                vocab.append(str(temp))
                count +=1
            else:
                if temp==words_train[k]:
                    count+=1
                else:
                    freq.append(str(count))
                    count=1;
                    temp=words_train[k]
                    vocab.append(str(temp))
        freq.append(str(count))

        for k in range(len(freq)):
                if int(freq[k]) > 1 :
                       vocabulary.append(vocab[k])
                       frequency.append(freq[k])


        vocab_positive=[]
        freq_positive=[]

        count=0

        for k in range(0,len(words_train_positive)):
            if count==0:
                temp=words_train_positive[k]
                vocab_positive.append(str(temp))
                count +=1
            else:
                if temp==words_train_positive[k]:
                    count+=1
                else:
                    freq_positive.append(str(count))
                    count=1;
                    temp=words_train_positive[k]
                    vocab_positive.append(str(temp))
        freq_positive.append(str(count))


        vocab_negative=[]
        freq_negative=[]

        count=0

        for k in range(0,len(words_train_negative)):
            if count==0:
                temp=words_train_negative[k]
                vocab_negative.append(str(temp))
                count +=1
            else:
                if temp==words_train_negative[k]:
                    count+=1
                else:
                    freq_negative.append(str(count))
                    count=1;
                    temp=words_train_negative[k]
                    vocab_negative.append(str(temp))
        freq_negative.append(str(count))



        prob_positive= count_positive_train/ (count_positive_train + count_negative_train)
        prob_negative= count_negative_train/ (count_positive_train + count_negative_train)



        for k in range(0,len(test)):
            if test[k]== '+' or test[k]== '-':
                p=k+1
                sum_positive= 0
                sum_negative=0
                prob_word_negative= 0
                prob_word_positive=0
                while test[p]!= '+' and test[p] != '-':
                    if test[p] not in vocabulary:
                        prob_word_positive= math.log2(1/ (count_positive_words_train+len(vocabulary)))
                        prob_word_negative= math.log2(1/ (count_negative_words_train+len(vocabulary)))
                    elif test[p]in vocabulary and test[p] not in vocab_positive:
                        prob_word_positive= math.log2(1/ (count_positive_words_train+len(vocabulary)))
                    elif test[p]in vocabulary and test[p] not in vocab_negative:
                        prob_word_negative= math.log2(1/(count_negative_words_train+len(vocabulary)))
                    elif test[p]in vocabulary and test[p] in vocab_positive:
                        prob_word_positive=  math.log2(int(frequency[vocabulary.index(test[p])])/count_positive_words_train)
                    elif test[p]in vocabulary and test[p] in vocab_negative:
                        prob_word_negative=  math.log2(int(frequency[vocabulary.index(test[p])])/count_negative_words_train)    
                    sum_positive += prob_word_positive
                    sum_negative += prob_word_negative
                    p += 1
                    if p==len(test):
                        break
                sum_positive += math.log2(prob_positive)
                sum_negative -= math.log2(prob_negative)
                if sum_positive > sum_negative:
                    experimental.append(1)
                else:
                    experimental.append(0)
                    
        tp=0
        tn=0
        fp=0
        fn=0
        for k in range(0,len(theoritical)):
            if theoritical[k]==1 and experimental[k]==1:
                tp+=1
            elif theoritical[k]==0 and experimental[k]==0:
                tn+=1
            elif theoritical[k]==1 and experimental[k]==0:
                fn+=1
            elif theoritical[k]==0 and experimental[k]==1:
                fp+=1
        accuracy= ( tp+tn )/ (tp+tn+fp+fn)
        print(accuracy)
        avg_accuracy.append(accuracy)
        i=i+25
        j=j+25
tem=sum(avg_accuracy)/len(avg_accuracy)
print(tem)
output=open("accuracy.txt","w")
output.write("Accuracies of 10 fold cases:" + "\n")
l=0
for h in avg_accuracy:
        l+=1
        tmp=int(h*100)
        if l<10:
                output.write("\n" + "case:" + str(l) + "    " + str(tmp) + " % " )
        else:
                output.write("\n" + "case:" + str(l) + "   " + str(tmp) + " % " )
                
output.write("\n" + "\n")
l=int(tem*100)
output.write("Average Accuracy for 10 cases: " + str(l) + " %")
output.close()


