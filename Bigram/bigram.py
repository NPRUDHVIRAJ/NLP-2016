a=open("vocabularywithbigrams.txt","r+")
a.seek(0,2)
f = file("data_without_stopwords.txt")
bigram1=open("bigrams.txt","w")
for line in f.readlines():
    i=1
    words=line.split()
    for p in range(len(words)):
        
        if (i+1)<len(words):
            
            x1=words[i]
            x2=words[i+1]
            y=x1+" "+x2
            i=i+1
            #print(y +"\n")
            bigram1.write(y +"\n")
        continue
    continue
bigram1.close()
g=open("bigrams.txt")
open("countedbigrams.txt","w").close()
b=open("bigram_freq.txt","w")
lines=g.readlines()

for i in range(0,len(lines)):
    flag=0
    h=open("countedbigrams.txt","r+")
    coun_lines=h.readlines()  
    count=0
    x=lines[i]
    #print x
    for j in range(0,len(coun_lines)):
        y=coun_lines[j]
        #print y
        if x == y:
            flag=1
            break
    if flag!=1:
        for k in range(0,len(lines)):
            if x == lines[k]:
               count=count+1

        b.write(x.replace("\n"," ") + ":" + str(count) + "\n")
        h.write(x + "\n")
        if count>=2:
             a.write(x)
        
        
    
b.close()
h.close()
g.close()


    
