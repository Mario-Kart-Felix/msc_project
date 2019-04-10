import glob
import re
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from wordcloud import WordCloud
from collections import defaultdict


def get_common_surface_form(original_corpus, stemmer):
    counts = defaultdict(lambda : defaultdict(int))
    surface_forms = {}

    for document in original_corpus:
        for token in document:
            stemmed = stemmer.stem(token)
            counts[stemmed][token] += 1

    for stemmed, originals in counts.items():
        surface_forms[stemmed] = max(originals, 
                                     key=lambda i: originals[i])

    return surface_forms

stemmer = PorterStemmer() # Stemmer for reducing terms to root form 

stemmed_corpus = []       # For storing the stemmed tokens 

original_corpus = []      # For storing the non-stemmed tokens

path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
for file_ in allFiles:
    with open(file_, "r") as fs:
        review = fs.readlines()
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename_parts = filename_search.group()
        filename = filename_parts.split('.')[0] + '.jpg'
        # Iterate over the files
    stemmer = PorterStemmer() # Stemmer for reducing terms to root form 
    stemmed_corpus = []       # For storing the stemmed tokens 
    original_corpus = []      # For storing the non-stemmed tokens
           
            
    for r in review:
        contents = r.lower().strip() # Load file contents
        tokens = word_tokenize(contents)     # Extract tokens
        stemmed = [stemmer.stem(token) for token in tokens] # Stem tokens
        stemmed_corpus.append(stemmed)    # Store stemmed document
        original_corpus.append(tokens)    # Store original document
    dictionary = Dictionary(stemmed_corpus) # Build the dictionary
    # Get the surface form for each stemmed word
    counts = get_common_surface_form(original_corpus, stemmer)
    # Convert to vector corpus
    vectors = [dictionary.doc2bow(text) for text in stemmed_corpus]
    # Train TF-IDF model
    tfidf = TfidfModel(vectors)
    #Get TF-IDF weights
    weights = tfidf[vectors[0]]
    # Replace term IDs with human consumable strings
    weights = {counts[dictionary[pair[0]]]: pair[1] for pair in weights}

    # Initialize the cloud
    wc = WordCloud(background_color="white",
                    max_words=2000,
                    width=1024,
                    height=720,
                    stopwords=stopwords.words('english'))
    # Generate the cloud
    wc.generate_from_frequencies(weights)
    # Save the cloud to a file
    wc.to_file(r'../data/processed/wordclouds/' + filename)               