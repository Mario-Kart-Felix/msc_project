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
        review = f.read()
        reviews.append(review)


def analyze_sentiment_sentiwordnet_lexicon(review, verbose=False):
    # tokenize and POS tag text tokens
    text_tokens = nltk.word_tokenize(review)
    tagged_text = nltk.pos_tag(text_tokens)
    pos_score = neg_score = token_count = 0
    # get wordnet synsets based on POS tags
    # # get sentiment scores if synsets are found
    for word, tag in tagged_text:
        ss_set = None
        if 'NN' in tag and len(list(swn.senti_synsets(word, 'n'))) != 0:
            ss_sets = list(swn.senti_synsets(word, 'n'))
            ss_set = ss_sets[0]
        elif 'VB' in tag and len(list(swn.senti_synsets(word, 'v'))) != 0:
            ss_sets = list(swn.senti_synsets(word, 'v'))
            ss_set = ss_sets[0]
        elif 'JJ' in tag and len(list(swn.senti_synsets(word, 'a'))) != 0:
            ss_sets = list(swn.senti_synsets(word, 'a'))
            ss_set = ss_sets[0]
        elif 'RB' in tag and len(list(swn.senti_synsets(word, 'r'))) != 0:
            ss_sets = list(swn.senti_synsets(word, 'r'))
            ss_set = ss_sets[0]
        # if senti-synset is found
        if ss_set:
            # add scores for all found synsets
            pos_score += ss_set.pos_score()
            neg_score += ss_set.neg_score()
            token_count += 1
            # aggregate final scores
    final_score = pos_score - neg_score
    norm_final_score = round(float(final_score) / token_count, 2)
    final_sentiment = 'positive' if norm_final_score >= 0 else 'negative'
    if verbose:
        norm_pos_score = round(float(pos_score) / token_count, 2)
        norm_neg_score = round(float(neg_score) / token_count, 2)
        # to display results in a nice table
        sentiment_frame = pd.DataFrame([[final_sentiment,
                                        norm_pos_score, 
                                        norm_neg_score,
                                        norm_final_score]],
                                        columns=pd.MultiIndex(levels=[['SENTIMENT STATS:'],
                                        ['Predicted Sentiment',
                                        'Positive',
                                        'Negative',
                                        'Overall']],
                                        labels=[[0,0,0,0],
                                        [0,1,2,3]]))
        print(sentiment_frame)
        return final_sentiment

print(analyze_sentiment_sentiwordnet_lexicon(reviews[0], verbose=True))