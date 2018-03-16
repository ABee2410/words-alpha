# Abby Woolley Words Quiz


#total words
with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()
print (words [:10])

print (len(words))


#num of words with 5 letters
five_letter= 0
for w in words:
    if (len(w))==5:
        five_letter+=1

print(five_letter)


#number words over 7 letters
long= 0
for w in words:
    if (len(w))>7:
        long+=1

print(long)


#number of characters
characters= 0
for w in words:
    characters+=len(w)

print(characters)


#number of words with no e
no_e= 0
for w in words:
    if "e" not in w:
        no_e+=1
    
print(no_e)


#number of words that begin and end with the same letter
first_last=0
for w in words:
    if w[0]==w[-1]:
        first_last+=1
        
print(first_last)


#number of words with exactly 3 A's

aez=0
for w in words:
    count=0
    for i in range(len(w)):
        if i=="a":
           count+=1
    if count==3:
        aez+=1
    
print(count)


#number of words with q not followed by u

qwords=0
for w in words:
    count=0
    for i in range(len(w)-1):
        if w[i]== "q" and w[i+1] != "u":
            count+=1
    if w[-1]=="q":
        count+=1
    if count>0:
        qwords+=1
        
print(qwords)
    
            


    
