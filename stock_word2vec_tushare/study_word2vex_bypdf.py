
# -*- coding:utf-8 -*-
import jieba
import jieba.posseg as pseg
from jieba import analyse
from gensim.models import word2vec
from urllib.request import urlopen
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import process_pdf, PDFResourceManager
from io import StringIO


class studyAndJieba():
    #此函数用于读取和返回pdf文件的内容
    def getPdfText(self,pdf_url):
        pdf_file_obj = urlopen(pdf_url)
        pdf_rm = PDFResourceManager()
        ret_str = StringIO()
        lap = LAParams()
        tc = TextConverter(pdf_rm, ret_str, laparams=lap)

        process_pdf(pdf_rm, tc, pdf_file_obj)
        tc.close()
        pdf_text = ret_str.getvalue()
        ret_str.close()
        return pdf_text
    
    def study(self,pdf_url):
        pdf_text = self.getPdfText(pdf_url)

        jieba.load_userdict("user_dict.txt")
        jieba_cut_seq = jieba.cut(pdf_text)
        pdf_cut_text = " ".join(jieba_cut_seq)


        #加载停用词表
        stopwords = {}
        fstop = open('cn_stopwords.txt', 'r',encoding='utf-8',errors='ingnore')
        for eachWord in fstop:
            stopwords[eachWord.strip()] = eachWord.strip()  #停用词典
        fstop.close()


        #分词
        seg_list = jieba.cut(pdf_cut_text, cut_all=False)
        #print("[精确模式]: ", "  ".join(seg_list))        
        #分词并标注词性
        #seg_list = pseg.cut(line)
        seg_final = ''
        for word in seg_list:
            if word not in stopwords:  
                #输出分词
                seg_final +=word+" "
        #print(seg_final)
        with open('分词后的语料.txt', 'a', encoding='utf-8') as ff:
            ff.write(''.join(seg_final)) # 词汇用空格分开
                # 加载语料




if __name__ == '__main__':
    with open('pdf_url.txt', errors='ignore', encoding='utf-8') as fp:
        lines = fp.readlines()
        for line in lines:
            pdf_url = line
            mwc = studyAndJieba()
            mwc.study(pdf_url)

    
    sentences = word2vec.Text8Corpus('分词后的语料.txt')
    # 训练模型
    model = word2vec.Word2Vec(sentences, sg=1, workers=3,batch_words=1000)
    # 保存模型
    model.save('study.model')


