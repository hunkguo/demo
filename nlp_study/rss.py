import feedparser
import jieba
import jieba.analyse
import stanza
import re

jieba.set_dictionary('data/dict.txt')

pattern = re.compile(r'<[^>]+>',re.S)


d=feedparser.parse('http://hunkhome.asuscomm.com:9200/taoguba/index')
#d=feedparser.parse('http://hunkhome.asuscomm.com:9200/cls/telegraph')

'''
stanza
'''
#zh_nlp = stanza.Pipeline('zh')

for i in range(len(d.entries)):
	print("-"*3+"文章"+str(i)+"---"+d.entries[i].title)
	print("-"*5+"摘要-----"+pattern.sub('',d.entries[i].summary))
	'''
	#stanza
	doc = zh_nlp(pattern.sub('',d.entries[i].summary))
	for sent in doc.sentences:
		#print("Sentence：" + sent.text) # 断句
		#print("Tokenize：" + ' '.join(token.text for token in sent.tokens)) # 中文分词
		#print("UPOS: " + ' '.join(f'{word.text}/{word.upos}' for word in sent.words)) # 词性标注（UPOS）
		#print("XPOS: " + ' '.join(f'{word.text}/{word.xpos}' for word in sent.words)) # 词性标注（XPOS）
		#print("NER: " + ' '.join(f'{ent.text}/{ent.type}' for ent in sent.ents)) # 命名实体识别

		if sent.ents:
			print("***关键词*** " + ' '.join(f'{ent.text}/{ent.type}' for ent in sent.ents))
	'''
	#jieba
	content = pattern.sub('',d.entries[i].summary)
	tags = jieba.analyse.extract_tags(content, topK=20)
	print(",".join(tags))

