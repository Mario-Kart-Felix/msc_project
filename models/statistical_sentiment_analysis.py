import nltk
import pandas as pd
import glob
from nltk.corpus import sentiwordnet as swn

# Import the data set 
path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
reviews = list()
summaries = list()
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.readlines()
        reviews.append(review)


# initialize afinn sentiment analyzer
from afinn import Afinn
af = Afinn()

# compute sentiment scores (polarity) and labels
sentiment_scores = [af.score(r) for r in reviews[0]]
sentiment_category = ['positive' if score > 0 
                          else 'negative' if score < 0 
                              else 'neutral' 
                                  for score in sentiment_scores]
    
    
# sentiment statistics per news category
df = pd.DataFrame([sentiment_scores, sentiment_category]).T
df.columns = ['sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.describe()