# -*- coding:utf-8 -*-
from gensim.models import word2vec

# 加载模型
model = word2vec.Word2Vec.load('study.model')

# 选出最相似的10个词
for e in model.most_similar(positive=['基建'], topn=10):
   print(e[0], e[1])