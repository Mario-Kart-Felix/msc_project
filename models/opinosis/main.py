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
allFiles = glob.glob(r'../../data/raw/OpinosisDataset1.0_0/topics/*.data')

reviews = list()
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.read().splitlines()
        reviews.append(review)

# try with simple reviews
graph, nodes_PRI = get_graph(reviews[50])




candidates = summarizer(graph,nodes_PRI)
print candidates

tmp = remove_duplicates(candidates,parameters["SIGMA_SIM"])

# use the JP and R scores to discriminate which candidate sentences should be thrown out

for sentence, score in Counter(tmp).most_common():
	clean_sentence = untag(sentence)
#	JP_score = joint_probability(clean_sentence)
#	R_score = readability_score(clean_sentence)
	print clean_sentence, score
#, JP_score, R_score"""



