import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences
import glob
import pdb
import re

# Import the data set 
path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
reviews = list()
summaries = list()
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.read()
        reviews.append(review)
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename = filename_search.group()
        myfile = open(r'../data/processed/' + filename, 'w')
        myfile.writelines(summarize(review, word_count = 20))
        myfile.close()
#print(allFiles)


"""for review in reviews:
    summary = summarize(review)
    print(review)
    summaries.append(review)"""

#print(summaries)