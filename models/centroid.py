from os import listdir
import string
import math

"""Method to calculate Inverse Document Frequency Score"""
def calculate_idf(word):
    files = [f for f in listdir("E:\Works\Products\doc") ]  #Specify the directory where the documents located
    count,wcount=2,1    
    for file1 in files:
        file=open("E:\Works\Products\doc\\" +file1,'r')     #Specify the directory where the documents located
        page=file.read()
        if(word in page):
            wcount+=1
        count+=1
    idf=count/wcount
    
    return math.log(idf,10)

"""Method to calculate Centroid Score of sentences"""
def calculate_centroid(sentences):
    
    """"Compute tf X idf score for each word"""
    tfidf=dict()
    for sentence in sentences:
        words=sentence.split()
        for word in words:
            if word in tfidf:
                tfidf[word]+=calculate_idf(word)
            else:
                tfidf[word]=calculate_idf(word)

    """Construct the centroid of Cluster
    By taking the words that are above the threshold"""

    centroid=dict()
    threshold=0.7
    for word in tfidf:
        if(tfidf[word]>threshold):
            centroid[word]=tfidf[word]
        else:
            centroid[word]=0

    """Compute the Score for Sentences"""
    senctence_score=list()
    counter=0
    for sentence in sentences:
        senctence_score.append(0)
        words=sentence.split()
        for word in words:
            senctence_score[counter]+=centroid[word]
        
        counter=counter+1
    return senctence_score


"""Splitting Documents as sentences"""
files = [f for f in listdir("E:\Works\Products\doc") ]
page=""
for file1 in files:
    file=open("E:\Works\Products\doc\\" +file1,'r')
    page+=file.read()
    file.close()
sentences=page.split(".")
senctence_score=calculate_centroid(sentences)
    

"""Printing Sentences which has more central words"""
for i in range(len(sentences)):
    if(senctence_score[i]>15):
        print(sentences[i])