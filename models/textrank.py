import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences
import glob
import re

# Import the data set 
path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.read()
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename = filename_search.group()
        myfile = open(r'../data/processed/textrank/' + filename, 'w')
        myfile.writelines(summarize(review, ratio=0.1))
        myfile.close()