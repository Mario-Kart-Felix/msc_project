from rouge import Rouge
import glob
import os
import re

summaryFiles = glob.glob(r'../data/processed/textrank/*')
fileNames = []
#goldSummaries = glob.glob(r'..data/raw/OpinosisDataset1.0_0/summaries-gold/*/')
directories = os.walk(r'../data/raw/OpinosisDataset1.0_0/summaries-gold')
directory_list = next(directories)[1]
for h in summaryFiles:
    foldername_search = re.search(r'[^\\/:*?"<>|\r\n]+$', h)
    foldername = (foldername_search.group()).split('.')[0]
    with open(h, 'r') as f:
        hypothesis = f.read()
    f.close()
    if foldername in directory_list:
        files = glob.glob('../data/raw/OpinosisDataset1.0_0/summaries-gold/'+foldername+'/*')
        for r in files:
            with open(r, 'r') as f:
                reference = f.read()
            f.close()
            rouge = Rouge()
            scores = rouge.get_scores(hypothesis, reference)
            print(scores)

 

        
#print(directory_list)

"""for filename in fileNames:
    for _, y, _ in directories:
        print(filename in y)"""




"""for filename in fileNames:
    if filename in directory_list:
        print(filename)"""
#print(directory_list)

"""files_rouge = FilesRouge(hyp_path, ref_path)
scores = files_rouge.get_scores()

scores = files_rouge.get_scores(avg=True)"""

