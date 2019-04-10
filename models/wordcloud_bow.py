path = r'../data/raw/OpinosisDataset1.0_0/topics/'
allFiles = glob.glob(path + "/*.data")
for file_ in allFiles:
    with open(file_, "r") as fs:
        review = fs.read()
        filename_search = re.search(r'[^\\/:*?"<>|\r\n]+$', file_)
        filename_parts = filename_search.group()
        filename = filename_parts.split('.')[0] + '.jpg'