# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd
import h5py
import datetime
import jieba
import jieba.posseg as pseg
from jieba import analyse
import gensim
from io import StringIO
import os

# 获取上市公司公告
class announcement:
    def __init__(self):
        # 判断h5文件更新日期，超过即更新
        # 股票代码、交易日历、
        # 初始化tushare接口
        self.pro = ts.pro_api('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
        self.hdfsFile = 'common_data.h5'
        # 判断首次运行
        self.firstInit = True
    
    def writeH5(self, h5Key, dfData):
        # 写h5
        store = pd.HDFStore(self.hdfsFile,'a', complevel=4, complib='blosc')
        store[h5Key] = dfData
        store.close()
    
    def readH5(self, h5Key):
        # 读h5
        data=pd.read_hdf(self.hdfsFile,key=h5Key)
        return data

    def getStock(self):
        try:
            data_stock = self.readH5('stock')
        except:
            data_stock = self.pro.stock_basic(exchange='', list_status='L')
            self.writeH5('stock', df_stock)
        return data_stock

    # 未用
    def getAnnouncement(self, ts_code):
        for _ in range(10):
            try:
                data_announcement = self.pro.anns(ts_code=ts_code)
            except:
                time.sleep(5)
            else:
                return data_announcement



    def jiebaFenci(self,content_text,jiebaFenciFile):
        jieba.load_userdict("user_dict.txt")


        #加载停用词表
        stopwords = {}
        fstop = open('baidu_stopwords.txt', 'r',encoding='utf-8',errors='ingnore')
        for eachWord in fstop:
            stopwords[eachWord.strip()] = eachWord.strip()  #停用词典
        fstop.close()


        #分词
        seg_list = jieba.cut(content_text)
        #print("[精确模式]: ", "  ".join(seg_list))        
        #分词并标注词性
        #seg_list = pseg.cut(line)
        seg_final = ''
        for word in seg_list:
            if word not in stopwords:  
                #输出分词
                seg_final +=word+" "
        #print(seg_final)
        with open('dataFenci/'+jiebaFenciFile, 'a', encoding='utf-8') as ff:
            ff.write(''.join(seg_final)) # 词汇用空格分开
        #print("[%s]分词完成"% (jiebaFenciFile))


    def study(self,jiebaFenciFile):
        # 加载语料
        sentences = gensim.models.word2vec.Text8Corpus('dataFenci/'+jiebaFenciFile)

        if(self.firstInit):
            # 训练模型
            model =  gensim.models.Word2Vec(sentences, sg=1, min_count=1, workers=3,batch_words=1000)
            # 保存模型
            model.save('study.model')
            print("[%s]学习完成1"% (jiebaFenciFile))
            self.firstInit = False
        else:
            model = gensim.models.Word2Vec.load('study.model')
            model.train(sentences,total_examples = model.corpus_count, epochs = model.iter)
            # 保存模型
            model.save('study.model')


            print("[%s]学习完成2"% (jiebaFenciFile))

            if os.path.exists(jiebaFenciFile):
                #删除文件，可使用以下两种方法。
                os.remove(my_file)

        

        #with open('分词后的语料.txt', "r+") as f:
        #    f.truncate()   #清空文件

    def run(self, data_stock):


        for stock in data_stock.iterrows():
            ts_code = stock[1]["ts_code"]
            stockName = stock[1]["name"]
            jiebaFenciFile = ts_code+'.txt'

            #获取最新的50条公告数据
            data_announcement = self.getAnnouncement(ts_code)
            print("正在获取股票[%s_%s]公告"%(ts_code,stockName) )

            for anns in data_announcement.iterrows():
                #print(anns[1]["ts_code"])
                #print(anns[1]["ann_date"])
                #print(anns[1]["title"])
                content_text=anns[1]["content"]
                #print(content_text)
                self.jiebaFenci(content_text,jiebaFenciFile)
            self.study(jiebaFenciFile)




        
if __name__ == "__main__":
    
    s = announcement()
    #data_cal = s.getCal()
    data_stock = s.getStock()
    s.run(data_stock)
