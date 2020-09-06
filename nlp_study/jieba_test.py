# encoding=utf-8
import jieba
import jieba.analyse

jieba.set_dictionary('data/dict.txt')

content = '''

我国正计划把大力支持发展第三代半导体产业，写入正在制定中的“十四五”规划，并计划在2021～2025年间，在教育、科研、开发、融资、应用等等各个方面，大力支持发展第三代半导体产业，以期实现独立自主。


'''

'''
seg_list = jieba.cut(content)  # 默认是精确模式
print(", ".join(seg_list))

print('-'*50)

seg_list = jieba.cut_for_search(content)  # 搜索引擎模式
print(", ".join(seg_list))
'''
print('-'*40)
print(' 基于 TF-IDF 算法的关键词抽取')
print('-'*40)


tags = jieba.analyse.extract_tags(content, topK=20)
print(",".join(tags))


print('-'*40)
print(' 基于 TextRank 算法的关键词抽取')
print('-'*40)

for x, w in jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v')):
    print('%s %s' % (x, w))