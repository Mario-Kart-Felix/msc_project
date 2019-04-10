#Python-Script for LexRank Calculation Example
#Author: Franziska Weng
#Implemented by Obiamaka Agbaneje
#License: Attribution 4.0 International (CC BY 4.0)
#License-URL: https://creativecommons.org/licenses/by/4.0/


#PACKAGES

import re
import numpy as np
import glob


#FUNCTIONS

#calculate idf-modified-cosine
def idf_modified_cosine(x, y, idf):
    """Calculate term frequencies for inputs x and y. Finally, apply formula to calculate
    idf-modified cosine similarity of x and y.
    """
    result = 0
    try:
        tf_x = [dict([word, int(tf)] for word, tf in dict(
            np.array(np.unique(x, return_counts=True)).T).items())][0]
        tf_y = [dict([word, int(tf)] for word, tf in dict(
            np.array(np.unique(y, return_counts=True)).T).items())][0]
        result = sum([tf_x[w] * tf_y[w] * (idf[w]**2)
		        for w in tf_x.keys() & tf_y.keys()]) / ((
            sum([(tf_x[w] * idf[w])**2
                for w in tf_x.keys()])**0.5) * (
            sum([(tf_y[w] * idf[w])**2
                for w in tf_y.keys()])**0.5))
    except:
        print(r'x:', x, r'y:', y)
        pass
    return result

#calculate binary value
def idf_modified_cosine_binary(x, y, t, idf):
    """Return 1 if idf-modified-cosine value is greater than threshold, else return 0.
    """
    idf_modified_cosine_value_binary = 0
    if idf_modified_cosine(x, y, idf) > t:
        idf_modified_cosine_value_binary = 1
    return idf_modified_cosine_value_binary

#calculate pagerank
def calculate_pagerank(binary_cosine_matrix, d):
    """Calculate left stochastic matrix A with all row sums equal to 1, random surfer
    model matrix B, left stochastic matrix M with all row sums equal to 1 and including
    random surfer model. Next, calculate eigenvector v for eigenvalue 1 from transposed
    matrix M and finally, return pagerank vector as normalized eigenvector v.
    """
    pr = 0
    try:
        A = (binary_cosine_matrix.T / binary_cosine_matrix.sum(axis=1)).T
        B = np.zeros((len(A), len(A))) + 1/len(A)
        M = (1-d)*A + d*B
        v = np.linalg.eig(M.T)[1][:, 0].astype(float) #throws complex warning
        pr = v / sum(v)
    except:
        pass
    return pr


def lexrank(documents, t=0.1, d=0.5):
    #input text
    documents = np.array(documents)
    #PROCESS
    #set number of documents N
    N = len(documents)
    #split documents into words
    words_in_documents = np.array([np.array([word 
            for word in re.split(r'[^A-Za-z]+', str(document).lower()) if len(word) > 0])
        for document in documents])

    #extract all unique words
    words = np.unique([word_in_document
            for words_in_document in words_in_documents
        for word_in_document in words_in_document])

    #create dictionary of inverse document frequencies (idf)
    dict_idf = [dict([w, float(df)]
                for w, df in dict(np.array([words, [np.log(N / sum([word in words_in_document
            for words_in_document in words_in_documents]))
        for word in words]]).T).items())][0]
#    print(r'Inverse document frequencies:', dict_idf)

    #split documents into sentences
    sentences_in_documents = [re.split(r'[.!?;]\s{0,5}', str(document).lower())[:-1]
        for document in documents]

    #extract words in sentences
    words_in_sentences_in_documents = [[[word
                for word in re.split(r'[^A-Za-z]+', sentence_in_document) if len(word) > 0]
            for sentence_in_document in sentences_in_document]
        for sentences_in_document in sentences_in_documents]

    #calculate overall summary applying lexrank
    sentences = [sentences
        for words_in_sentences_in_document in words_in_sentences_in_documents
            for sentences in words_in_sentences_in_document]
    overall_summary = r' '.join(sentences[np.argmax(calculate_pagerank(
                np.array([[idf_modified_cosine_binary(sentence_x, sentence_y, t, dict_idf)
            for sentence_y in sentences]
        for sentence_x in sentences]), d))])
    return overall_summary

#cosine threshold t = 0.1

#damping factor d = 0.5

path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
reviews = list()
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.readlines()
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename = filename_search.group()
        myfile = open(r'../data/processed/lexrank/' + filename, 'w')
        myfile.writelines(lexrank(review))
        myfile.close()
        







