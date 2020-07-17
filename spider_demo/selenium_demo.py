from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
browser = webdriver.Firefox(firefox_options=firefox_options)
browser.get('http://jycg.hubei.gov.cn/jyxx/zfcg/xqgg/')
browser.get('http://jycg.hubei.gov.cn/jyxx/zfcg/cgxx.shtml?mateid=23644&dataid=1')
print(browser.page_source)
'''


chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=chrome_option)


# 湖北省电子招投标交易平台
'''
browser.get('http://www.hbbidcloud.cn/shengbenji/jyxx/004002/004002004/20200716/63f44e47-030e-4892-99f9-d0a65c278332.html')
ele_string = browser.find_element_by_xpath("//*[@id='infoContentM']/table/tbody/tr[22]/td/table/tbody/tr[1]/td[2]/div").text
print(ele_string)
'''

browser.get('http://jycg.hubei.gov.cn/jyxx/zfcg/cgxx.shtml?mateid=23572&dataid=1')
ele_string = browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div[1]/div/p[23]/span[2]").text
print(ele_string)

browser.close()





