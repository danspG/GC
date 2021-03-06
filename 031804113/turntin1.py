import re, sys, datetime
import os
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm
import jieba


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

def readTXT(txtfile):
    print('*' * 80)
    print('文件', '加载中……')
    t1 = datetime.datetime.now()
    texts = open(txtfile,encoding='UTF-8').read()
    ms = msplit(texts)
    t2 = datetime.datetime.now()
    print('加载完成并分词完成，用时: ', t2 - t1)
    showInfo(texts,txtfile)
    return ms

def showInfo(txt, filename = 'filename'):#计算字符个数
    chars = 0
    for p in txt:
            chars = chars + len(p)
    print('字符数: {0:>8d} 个。'.format(chars))
          
def compareParagraph(txt1,txt2): 
    return tf_similarity(txt1,txt2)


def tf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))
    
    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)

    vectorizer = CountVectorizer(tokenizer=lambda s: s.split())

    corpus = [s1, s2]

    vectors = vectorizer.fit_transform(corpus).toarray()

    numerator = np.sum(np.min(vectors, axis=0))

    denominator = np.sum(np.max(vectors, axis=0))

    return 1.0 * numerator / denominator

 
txt1 = "C:/Users/guoch/Desktop/sim_0.8/orig.txt"
txt2 = "C:/Users/guoch/Desktop/sim_0.8/orig_0.8_del.txt"

print('开始比对...'.center(80, '*'))
t1 = datetime.datetime.now()
t = compareParagraph(txt1,txt2)
tt = str(t)
with open("C:/Users/guoch/Desktop/sim_0.8/orig1.txt",'w',encoding='utf-8') as f:
    f.write(tt)
t2 = datetime.datetime.now() 
print('\n比对完成，总用时: ', t2 - t1)    
