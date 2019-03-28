# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:04:50 2019

@author: 1714116
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import networkx
def build_feature_matrix(documents, feature_type='frequency'):
    feature_type = feature_type.lower().strip()
    if feature_type == 'binary':
        vectorizer = CountVectorizer(binary=True, min_df=1,
                                     ngram_range=(1, 1))
    elif feature_type == 'frequency':
        vectorizer = CountVectorizer(binary=False, min_df=1,
                                     ngram_range=(1, 1))
    elif feature_type == 'tfidf':
        vectorizer = TfidfVectorizer(min_df=1,
                                     ngram_range=(1, 1))
    else:
        raise Exception("Wrong feature type entered. Possible values:
'binary', 'frequency', 'tfidf'")
    feature_matrix = vectorizer.fit_transform(documents).astype(float)
    
    return vectorizer, feature_matrix

def textrank_text_summarizer(documents, num_sentences=2, feature_type='frequency'):
    vec, dt_matrix = build_feature_matrix(norm_sentences, feature_type='tfidf')
    similarity_matrix = (dt_matrix * dt_matrix.T)
    similarity_graph = networkx.from_scipy_sparse_matrix(similarity_matrix)
    scores = networkx.pagerank(similarity_graph)
    ranked_sentences = sorted(((score, index) for index, score in scores.items()),reverse=True)