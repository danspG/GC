import jieba
import sys
from gensim import corpora, models, similarities
import os
import time
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm

def start_solve(position):
    start = open(position, 'r', encoding='UTF-8')
    start_text = start.read()
    start.close()
    start_items = msplit(start_text)
    return start_items

def test_solve(position):
    test = open(position, 'r', encoding='UTF-8')
    txt_test = test.read()
    test.close()
    test_items = msplit(txt_test)
    return test_items

def write_dir(ans,ans_position):
    str1 = str('0.2f' %ans)
    ans_text = open(ans_position,'w',encoding='UTF-8')
    ans_text.write(str1)
    ans_text.close()

def solveok(start_position,test_position,ans_position):
    start_items = start_solve(start_position)
    test_items = test_solve(test_position)
    ans = jaccard_similarity(start_items,test_items)
    write_dir(ans,ans_position)
    print('%.2f' %ans)


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def msplit(txts):#jieba分词然后去掉符号
    txts_ch = []
    txt_word = jieba.lcut_for_search(txts)
    stop_word=['啊','吧','呀','呢','的','得','她','它','他']
    for i in range(0,len(txt_word)):
        if is_Chinese(txt_word[i]):
            if txts[i] in stop_word:
                continue
            elif txt_word[i]:
                txts_ch += txt_word[i]
    return txts_ch

def jaccard_similarity(txt1, txt2):
    def add_space(txt):
        return ' '.join(list(txt))
    txt1, txt2 = add_space(txt1), add_space(txt2)
    vectorizer = CountVectorizer(tokenizer=lambda txt: txt.split())
    corpus = [txt1, txt2]
    vectors = vectorizer.fit_transform(corpus).toarray()
    numerator = np.sum(np.min(vectors, axis=0))
    denominator = np.sum(np.max(vectors, axis=0))
    return 1.0 * numerator / denominator



    
