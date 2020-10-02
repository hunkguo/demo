#coding:utf-8
import requests
import random
from lxml import etree
import re
import requests
import sys
import os
from PyPDF2 import PdfFileMerger


class Eeo(object):

	def __init__ (self):
		self.USER_AGENT_LIST = [
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
			"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
			"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
			"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
			"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
			"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
			"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
			"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
			"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
		]
		self.pdfid_url='http://app.eeo.com.cn/?app=mobile&controller=ipad&action=pdfChannel&cid=199&top=0&row=1'
		self.page_list_url = 'http://app.eeo.com.cn/?app=mobile&controller=ipad&action=pdfInfo&cid=199&pdfid='

	def getVersion(self):

		try:
			USER_AGENT = random.choice(self.USER_AGENT_LIST)
			headers = {'user-agent': USER_AGENT}
			resp = requests.get(self.pdfid_url, headers=headers, timeout=20)

			html=etree.HTML(resp.content)
			result=etree.tostring(html)

			result=html.xpath('//item/pdfid/text()') 
			return result[0]
		except Exception as e:
			print('Reason:', e)

	def getPdfList(self,pdfid):

		try:
			USER_AGENT = random.choice(self.USER_AGENT_LIST)
			headers = {'user-agent': USER_AGENT}
			resp = requests.get(self.page_list_url+str(pdfid), headers=headers, timeout=20)
			html=etree.HTML(resp.content)
			result=etree.tostring(html,encoding='utf-8')
			#print(result)

			result=html.xpath('//item/channel/item/url/text()') 

			return result
		except Exception as e:
			print('Reason:', e)

	def download_all_pdf_files(self,pdfid,pdfs):
		for index, pdf in enumerate(pdfs, 1):
			try:
				response = requests.get(pdf , stream=True)
				new_pdf_file = 'eeo_'+str(pdfid)+'_'+str(index)+'.pdf'
				with open(new_pdf_file, 'wb') as handle:
					for block in response.iter_content(1024):
						handle.write(block)
			except Exception as e:
				print('Reason:', e)

	def merge_pdf_files(self,pdfid,pdfs):
		pdf_file_merger = PdfFileMerger()
		merged_pdf = 'eeo_'+str(pdfid)+'.pdf' 

		for index, pdf in enumerate(pdfs, 1):
			if merged_pdf == pdf:
				self.remove_pdf_file(pdf)
			try:
				new_pdf_file = 'eeo_'+str(pdfid)+'_'+str(index)+'.pdf'
				pdf_file_merger.append(open(new_pdf_file, 'rb'))
				self.remove_pdf_file(new_pdf_file)
			except Exception as e:
				print('Reason:', e)

		with open(merged_pdf, 'wb') as fout:
			pdf_file_merger.write(fout)

		return merged_pdf

	def remove_pdf_file(self,file):
		os.remove(file)

	def remove_pdf_files(self, pdfs):
		for file in pdfs:
			self.remove_pdf_file(file)


def main():
	print('-'*20+'开始下载经济观察报'+'-'*20)
	eeo =  Eeo()
	current_pdfid = int(eeo.getVersion())
	print('-'*20+'获取最新版本成功'+'-'*20)
	# 获取当前最新版报纸
	pdfs_url = eeo.getPdfList(current_pdfid)
	print('-'*20+'获取最新报纸'+'-'*20)
	eeo.download_all_pdf_files(current_pdfid,pdfs_url)
	print('-'*20+'下载成功'+'-'*20)
	eeo.merge_pdf_files(current_pdfid,pdfs_url)
	print('-'*20+'合并成功'+'-'*20)
	'''
	# 获取 第900期至今的报纸
	for pdfid in range(900,current_pdfid+1):
		pdfs_url = eeo.getPdfList(pdfid)
		eeo.download_all_pdf_files(pdfid,pdfs_url)
		eeo.merge_pdf_files(pdfid,pdfs_url)
	'''
	


if __name__ == "__main__":
    main()
