'''

  _____                 _     _____          _                
  / ____|               | |   |  __ \        | |               
 | |  __ _ __ __ _ _ __ | |__ | |__) |___  __| |_   _  ___ ___ 
 | | |_ | '__/ _` | '_ \| '_ \|  _  // _ \/ _` | | | |/ __/ _ \
 | |__| | | | (_| | |_) | | | | | \ \  __/ (_| | |_| | (_|  __/
  \_____|_|  \__,_| .__/|_| |_|_|  \_\___|\__,_|\__,_|\___\___|
                  | |                                          
                  |_|   

 
 A graph-based text summarizer for easier consumption of product reviews

 Author: Matteo Tomassetti

 Contact: www.matteotomassetti.com

 Based on Opinosis by Kavita Ganesan (http://kavita-ganesan.com/opinosis)

 Main difference with the Opinosis implementation:

 1) Before stitching the sentences to an anchor we use k-means to cluster their sentiment

 2) We use the Oxford Language Model API to evaluate whether a sentence is readable or not

'''

from opinosis import *
import re
import glob
from bs4 import UnicodeDammit
allFiles = glob.glob(r'../../data/raw/OpinosisDataset1.0_0/topics/*.data')
print(allFiles)
reviews = list()
number_of_reviews = 0
for file_ in allFiles:
    with open(file_,errors="surrogateescape") as f:
        review = f.read().splitlines()
        reviews.append(review)
 #       try:
        graph, nodes_PRI = get_graph(review)
        candidates = summarizer(graph,nodes_PRI)
        tmp = remove_duplicates(candidates,parameters["SIGMA_SIM"])
        max_score = Counter(tmp).most_common(1)
        if max_score != []:
            sentence, score = max_score[0]
            clean_sentence = untag(sentence)
            #        JP_score = joint_probability(clean_sentence)
            #        R_score = readability_score(clean_sentence)
            filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
            filename = filename_search.group()
            myfile = open(r'../../data/processed/opinosis/' + filename, 'w')
            myfile.writelines(clean_sentence)
            myfile.close()
        #print(clean_sentence, score)

#, JP_score, R_score"""
#        except:
#                pass





