from rouge import Rouge
import glob
import os
import re

summaryFiles = glob.glob(r'../data/processed/textrank/*')
fileNames = []
#goldSummaries = glob.glob(r'..data/raw/OpinosisDataset1.0_0/summaries-gold/*/')
gold_summaries = os.walk(r'../data/raw/OpinosisDataset1.0_0/summaries-gold')
gold_list = next(gold_summaries)[1]

for h in summaryFiles:
    foldername_search = re.search(r'[^\\/:*?"<>|\r\n]+$', h)
    foldername = (foldername_search.group()).split('.')[0]
    with open(h, 'r') as f:
        hypothesis = f.read()
    f.close()
    if foldername in gold_list:
        files = glob.glob('../data/raw/OpinosisDataset1.0_0/summaries-gold/'+foldername+'/*')
        for r in files:
            with open(r, 'r') as f:
                reference = f.read()
            f.close()
            rouge = Rouge()
            scores = rouge.get_scores(hypothesis, reference)
            print('TexRank:', scores)

 

summaryFiles = glob.glob(r'../data/processed/lexrank/*')
fileNames = []

for h in summaryFiles:
    foldername_search = re.search(r'[^\\/:*?"<>|\r\n]+$', h)
    foldername = (foldername_search.group()).split('.')[0]
    with open(h, 'r') as f:
        hypothesis = f.read()
    f.close()
    if foldername in gold_list:
        files = glob.glob('../data/raw/OpinosisDataset1.0_0/summaries-gold/'+foldername+'/*')
        for r in files:
            with open(r, 'r') as f:
                reference = f.read()
            f.close()
            rouge = Rouge()
            scores = rouge.get_scores(hypothesis, reference)
            print('Lexrank', scores)


summaryFiles = glob.glob(r'../data/processed/textrank_cosine/*')
fileNames = []

for h in summaryFiles:
    foldername_search = re.search(r'[^\\/:*?"<>|\r\n]+$', h)
    foldername = (foldername_search.group()).split('.')[0]
    with open(h, 'r') as f:
        hypothesis = f.read()
    f.close()
    if foldername in gold_list:
        files = glob.glob('../data/raw/OpinosisDataset1.0_0/summaries-gold/'+foldername+'/*')
        for r in files:
            with open(r, 'r') as f:
                reference = f.read()
            f.close()
            rouge = Rouge()
            scores = rouge.get_scores(hypothesis, reference)
            print('TextRank Cosine', scores)

summaryFiles = glob.glob(r'../data/processed/lsa/*')
fileNames = []

for h in summaryFiles:
    foldername_search = re.search(r'[^\\/:*?"<>|\r\n]+$', h)
    foldername = (foldername_search.group()).split('.')[0]
    with open(h, 'r') as f:
        hypothesis = f.read()
    f.close()
    if foldername in gold_list:
        files = glob.glob('../data/raw/OpinosisDataset1.0_0/summaries-gold/'+foldername+'/*')
        for r in files:
            with open(r, 'r') as f:
                reference = f.read()
            f.close()
            rouge = Rouge()
            scores = rouge.get_scores(hypothesis, reference)
            print('LSA', scores)

