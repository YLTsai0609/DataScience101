'''
input list[str]
output dict[keyword : list]
check the fomular from wiki
https://zh.wikipedia.org/wiki/Tf-idf
'''
from math import log



documents = ['terrible service this time','terrible terrible service',
'most terrible service','terrible service and experience',
'what a terrible service','so terrible service experience',
'what a terrible disappointment','what a terrible place',
'this time it was so horrible','the staff was horrible']
all_terms = []
for content in documents:
    for term in content.split():
        all_terms.append(term)

n_cotent = float(len(documents))


def idf(w):
    w = w.lower()
    return log( n_cotent / sum([float(w in cont) for cont in documents]), 10)


def tf(w, cont):
    w = w.lower()
    terms_of_content = cont.split()
    n_terms = len(terms_of_content)
    return sum([float(w == x) / n_terms for x in terms_of_content]) 

def tf_idf(w, cont):
    return tf(w, cont) * idf(w)

def run():
    word_tfidf = {}
    for w in set(all_terms):
        word_tfidf[w] = []
        word_idf = idf(w)
        for content in documents:
            word_tfidf[w].append(tf(w, content)*word_idf)
    return word_tfidf



# Test case, 'terrible' tf, idf in 'terrible terrible service'
print(tf('terrible', documents[1]))
print(n_cotent)
print(idf('terrible'))
df = run()
import pandas as pd
df = pd.DataFrame(df)
col = ['this','terrible','service','staff','disappointment','the','place','what','horrible','most','so','experience','was','time','a','it','and']
df = df[col]
df.to_csv('tfidf_demo.csv')
print('*')

# def computTFIDF(documents):
#     '''
#     {keyword_1 : [0.174743, 0,0, ...], keyword_2 : [...], keyword_k }
#     '''
#   return 


#   this	terrible	service	staff	disappointment	the	place	what	horrible	most	so	experience	was	time	a	it	and
# 0	0.174743	0.024228	0.055462	0.00	0.00	0.00	0.00	0.00000	0.000000	0.000000	0.000000	0.000000	0.000000	0.174743	0.00000	0.000000	0.00
# 1	0.000000	0.064607	0.073950	0.00	0.00	0.00	0.00	0.00000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.00000	0.000000	0.00
# 2	0.000000	0.032303	0.073950	0.00	0.00	0.00	0.00	0.00000	0.000000	0.333333	0.000000	0.000000	0.000000	0.000000	0.00000	0.000000	0.00
# 3	0.000000	0.024228	0.055462	0.00	0.00	0.00	0.00	0.00000	0.000000	0.000000	0.000000	0.174743	0.000000	0.000000	0.00000	0.000000	0.25
# 4	0.000000	0.024228	0.055462	0.00	0.00	0.00	0.00	0.13072	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.13072	0.000000	0.00
# 5	0.000000	0.024228	0.055462	0.00	0.00	0.00	0.00	0.00000	0.000000	0.000000	0.174743	0.174743	0.000000	0.000000	0.00000	0.000000	0.00
# 6	0.000000	0.024228	0.000000	0.00	0.25	0.00	0.00	0.13072	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.13072	0.000000	0.00
# 7	0.000000	0.024228	0.000000	0.00	0.00	0.00	0.25	0.13072	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.13072	0.000000	0.00
# 8	0.116495	0.000000	0.000000	0.00	0.00	0.00	0.00	0.00000	0.116495	0.000000	0.116495	0.000000	0.116495	0.116495	0.00000	0.166667	0.00
# 9	0.000000	0.000000	0.000000	0.25	0.00	0.25	0.00	0.00000	0.174743	0.000000	0.000000	0.000000	0.174743	0.000000	0.00000	0.000000	0.00