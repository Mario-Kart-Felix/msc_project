# Import glob
import glob
# Import string
import string
# Import NLTK Tokenize Library
from nltk.tokenize import sent_tokenize, word_tokenize
#Import NLTK Stopwords
from nltk.corpus import stopwords
#Import NLTK Lemmatize
from nltk.stem import WordNetLemmatizer
# Import regular expressions
import re
# Import Counter
from collections import Counter
#Import Wordcloud
from wordcloud import WordCloud

english_stops = set(stopwords.words('english'))
#reviews = []
path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
for file_ in allFiles:
    with open(file_, "r") as fs:
        review = fs.read()
 #       reviews.append(review)
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename_parts = filename_search.group()
        filename = filename_parts.split('.')[0] + '.jpg'
        # Tokenize the article: tokens
        tokens = word_tokenize(review)

        # Convert the tokens into lowercase: lower_tokens
        lower_tokens = [t.lower() for t in tokens]

        # Retain alphabetic words: alpha_only
        alpha_only = [t for t in lower_tokens if t.isalpha()]

        # Remove all stop words: no_stops
        no_stops = [t for t in alpha_only if t not in english_stops]

        # Instantiate the WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        # Lemmatize all tokens into a new list: lemmatized
        lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

        # Create the bag-of-words: bow
        bow = Counter(lemmatized)
        
        # Initialize the cloud
        wc = WordCloud(background_color="white",
                    max_words=2000,
                    width=1024,
                    height=720,
                    stopwords=stopwords.words('english'))
        # Generate the cloud
        wc.generate_from_frequencies(bow)
        # Save the cloud to a file
        wc.to_file(r'../data/processed/wordclouds_bow/' + filename)