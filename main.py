import pandas as pd
import nltk
import statistics
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# benepar.download('benepar_en3')
import spacy
# from spacy.tokens import Token
# Token.set_extension('context', default=True, force=True)
nlp = spacy.load("en_core_web_sm")

def clean(data):
    for i in range(0,data.shape[0]-1):
        title = data.iloc[i,1]

        #print(len(title))
        for j in range(0,len(title)-1):
            if title[j] == '|' or title[j] =='[':
                new_title = title.split(title[j])
                data.iloc[i,1] = new_title[0]

def count(data):
    word_counts=[]
    for i in range(0,data.shape[0]):
        title = data.iloc[i,1]
        word_list = title.split()
        number_of_words = len(word_list)
        word_counts.append(number_of_words)
    data.insert(4, 'WordCount', word_counts)

def tokenise(data):
    all_tokens=[]
    for i in range(0,data.shape[0]):
        title = data.iloc[i,1]
        tokens = nltk.word_tokenize(title)
        all_tokens.append(tokens)
    data.insert(5, 'TokenTitle', all_tokens)

def tag(data):
    tags_tokens = []
    for i in range(0, data.shape[0]):
        tokens = data.iloc[i, 5]
        tokens = nltk.pos_tag(tokens)
        tags_tokens.append(tokens)
    data.insert(6, 'TagTitle', tags_tokens)

def word_length(data):
    all_wl=[]
    for i in range(0,data.shape[0]):
        clauses=0
        word_lengths = []
        words = data.iloc[i,5]
        for w in words:
            word_lengths.append(len(w))
        all_wl.append(statistics.mean(word_lengths))
    data.insert(7, 'WordLength', all_wl)

def ttr(data):
    token_tag_ratio = []
    for i in range(0,data.shape[0]):
        pos_tokens = data.iloc[i, 5]
        num_tokens = len(pos_tokens)
        types = sorted(set(data.iloc[i, 6]))
        num_types = len(types)
        token_tag_ratio.append(float(num_types) / num_tokens)
    data.insert(8, 'TTR', token_tag_ratio)

def ratios(data):
    nounRatios = []
    verbRatios = []
    adjRatios = []
    advRatios = []
    for i in range(0, data.shape[0]):
        nouns = 0
        verbs = 0
        advs = 0
        adjs = 0
        total = len(data.iloc[i,5])
        for t in data.iloc[i, 6]:
            if t[1] in ["NN", "NNS", "NNP", "NNPS"]:
                nouns += 1
            elif t[1] in ["VB", "VBD", "VBN", "VBP"]:
                verbs += 1
            elif t[1] in ["RB", "RBR", "RBS"]:
                advs += 1
            elif t[1] in ["JJ", "JJR", "JJS"]:
                adjs += 1

        nounRatios.append(nouns / total)
        verbRatios.append(verbs / total)
        adjRatios.append(adjs / total)
        advRatios.append(advs / total)
    data.insert(9, 'nounRatio', nounRatios)
    data.insert(10, 'verbRatio', verbRatios)
    data.insert(11, 'adjectiveRatio', adjRatios)
    data.insert(12, 'adverbRatio', advRatios)

def clause(data):
    all_clauses = []

    for i in range(0,data.shape[0]):
        clause=False
        title = data.iloc[i,1]
        doc = nlp(title)
        for token in doc:
            if token.dep_ == 'relcl':
                clause=True
        all_clauses.append(clause)
    data.insert(13, 'Clause',all_clauses)

if __name__ == '__main__':
    arts = pd.read_csv('scopus.csv', header=0)
    stem = pd.read_csv('scopus(1).csv', header=0)
    for i in range(0,arts.shape[0]):
        arts.iloc[i,2] = 'arts'
    for i in range(0,stem.shape[0]):
        stem.iloc[i,2] = 'stem'
    d = [arts,stem]
    data = pd.concat(d,axis=0)

    #clean up, preprocessing
    clean(data)
    count(data)
    tokenise(data)
    tag(data)

    word_length(data)
    ttr(data)
    ratios(data)
    clause(data)
    print(data.iloc[1,:])
    print('done')
    data.to_csv('new_data.csv')
