# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 15:24:26 2016

@author: DIP
"""

from normalization import normalize_corpus, parse_document
from utils import build_feature_matrix, low_rank_svd
import numpy as np
import glob
import networkx
import re

def lsa_text_summarizer(documents, num_sentences=2,
                        num_topics=1, feature_type='frequency',
                        sv_threshold=0.5):
                            
    vec, dt_matrix = build_feature_matrix(documents, 
                                          feature_type=feature_type)

    td_matrix = dt_matrix.transpose()
    td_matrix = td_matrix.multiply(td_matrix > 0)

    u, s, vt = low_rank_svd(td_matrix, singular_count=num_topics)  
    min_sigma_value = max(s) * sv_threshold
    s[s < min_sigma_value] = 0
    
    salience_scores = np.sqrt(np.dot(np.square(s), np.square(vt)))
    top_sentence_indices = salience_scores.argsort()[-num_sentences:][::-1]
    top_sentence_indices.sort()
    s = ''
    for index in top_sentence_indices:
        s = s + ' ' + sentences[index]
        print(sentences[index])
    return s
    
def textrank_text_summarizer(documents, num_sentences=2,
                             feature_type='frequency'):
    
    vec, dt_matrix = build_feature_matrix(norm_sentences, 
                                      feature_type='tfidf')
    similarity_matrix = (dt_matrix * dt_matrix.T)
        
    similarity_graph = networkx.from_scipy_sparse_matrix(similarity_matrix)
    scores = networkx.pagerank(similarity_graph)   
    
    ranked_sentences = sorted(((score, index) 
                                for index, score 
                                in scores.items()), 
                              reverse=True)

    top_sentence_indices = [ranked_sentences[index][1] 
                            for index in range(num_sentences)]
    top_sentence_indices.sort()
    s = ''
    for index in top_sentence_indices:
        s = s + ' ' + sentences[index]
        print(sentences[index])
    return s

path = r'../../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
reviews = list()
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.read()
        DOCUMENT = review
        sentences = parse_document(DOCUMENT)
        norm_sentences = normalize_corpus(sentences,lemmatize=True) 
        print("Total Sentences:", len(norm_sentences))
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename = filename_search.group()
        myfile = open(r'../../data/processed/lsa/' + filename, 'w')
        myfile.writelines(lsa_text_summarizer(norm_sentences, num_sentences=2,
                    num_topics=1, feature_type='frequency',
                    sv_threshold=0.5))
        myfile = open(r'../../data/processed/textrank_cosine/' + filename, 'w')
        myfile.writelines(textrank_text_summarizer(norm_sentences, num_sentences=2,
                         feature_type='frequency'))
        





"""textrank_text_summarizer(norm_sentences, num_sentences=3,
                         feature_type='tfidf')     """                                   