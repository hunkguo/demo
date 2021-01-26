# encoding:utf-8

import requests
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UaVDdsMRdASOEL4FEUwDlFyD&client_secret=17u8kCWAQ4YzTAx7eG2lyxIiFtiO2eRd'
response = requests.get(host)
if response:
    #print(response.json())
    access_token = (response.json())['access_token']


    '''
    身份证识别
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    #f = open('24-1305301G146.jpg', 'rb')
    f = open('IMG_0704.jpeg', 'rb')
    img = base64.b64encode(f.read())

    params = {"id_card_side":"front","image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())