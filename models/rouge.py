from sumeval.metrics.rouge import RougeCalculator
import glob

rouge = RougeCalculator(stopwords=True, lang="en")



allFiles = glob.glob(r'../data/raw/OpinosisDataset1.0_0/topics/'+ "/*.data")
summaryFiles = glob.glob(r'..data/raw/OpinosisDataset1.0_0/summaries-gold')
reviews = list()
for file_ in allFiles:
    with open(file_, "r") as f:
        review = f.readlines()
        reviews.append(review)

rouge_1 = rouge.rouge_n(
            summary="I went to the Mars from my living town.",
            references="I went to Mars",
            n=1)

rouge_2 = rouge.rouge_n(
            summary="I went to the Mars from my living town.",
            references=["I went to Mars", "It's my living town"],
            n=2)

rouge_l = rouge.rouge_l(
            summary="I went to the Mars from my living town.",
            references=["I went to Mars", "It's my living town"])


print("ROUGE-1: {}, ROUGE-2: {}, ROUGE-L: {}".format(
    rouge_1, rouge_2, rouge_l
).replace(", ", "\n"))