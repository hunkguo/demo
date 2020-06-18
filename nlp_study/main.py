import feedparser
import stanza

d=feedparser.parse('http://hunkhome.asuscomm.com:9200/xueqiu/user/5124430882')



print("-"*20+"标题"+"-"*20)
print(d.feed.title)

print("-"*20+"链接"+"-"*20)
print(d.feed.link)


zh_nlp = stanza.Pipeline('zh')

for i in range(len(d.entries)):
	print("-"*20+"文章"+str(i)+"-"*20)
	print(d.entries[i].summary)
	doc = zh_nlp(d.entries[i].summary)
	for sent in doc.sentences:
		#print("Sentence：" + sent.text) # 断句
		#print("Tokenize：" + ' '.join(token.text for token in sent.tokens)) # 中文分词
		#print("UPOS: " + ' '.join(f'{word.text}/{word.upos}' for word in sent.words)) # 词性标注（UPOS）
		#print("XPOS: " + ' '.join(f'{word.text}/{word.xpos}' for word in sent.words)) # 词性标注（XPOS）
		#print("NER: " + ' '.join(f'{ent.text}/{ent.type}' for ent in sent.ents)) # 命名实体识别

		if sent.ents:
			print("***关键词*** " + ' '.join(f'{ent.text}/{ent.type}' for ent in sent.ents))