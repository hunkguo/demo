# -*- coding:utf-8 -*-
import jieba
import jieba.posseg as pseg
from jieba import analyse
from gensim.models import word2vec

#加载停用词表
stopwords = {}
fstop = open('cn_stopwords.txt', 'r',encoding='utf-8',errors='ingnore')
for eachWord in fstop:
    stopwords[eachWord.strip()] = eachWord.strip()  #停用词典
fstop.close()


with open('语料.txt', errors='ignore', encoding='utf-8') as fp:
    lines = fp.readlines()
    for line in lines:
        #分词
        seg_list = jieba.cut(line, cut_all=False)
        #print("[精确模式]: ", "  ".join(seg_list))        
        #分词并标注词性
        #seg_list = pseg.cut(line)
        seg_final = ''
        for word in seg_list:
            if word not in stopwords:  
                #输出分词
                seg_final +=word+" "
        #print(seg_final)


        with open('分词后的语料.txt', 'w', encoding='utf-8') as ff:
            ff.write(''.join(seg_final)) # 词汇用空格分开

# 加载语料
sentences = word2vec.Text8Corpus('分词后的语料.txt')
# 训练模型
model = word2vec.Word2Vec(sentences)
# 保存模型
model.save('study.model')
