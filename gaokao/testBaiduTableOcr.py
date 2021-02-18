import sys, fitz, os, datetime
import requests,base64
import json,time

def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()#开始时间

    print("imagePath="+imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):#判断存放图片的文件夹是否存在
            os.makedirs(imagePath) # 若图片文件夹不存在就创建
        (pdfFile, pdfExt) = os.path.splitext(pdfPath)
        pix.writePNG(imagePath+'/'+pdfFile+'_%s.png' % pg)#将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()#结束时间
    # print('pdf2img时间=',(endTime_pdf2img - startTime_pdf2img).seconds)


def baiduOcr(filepath):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UaVDdsMRdASOEL4FEUwDlFyD&client_secret=17u8kCWAQ4YzTAx7eG2lyxIiFtiO2eRd'
    response = requests.get(host)
    if response:
        access_token = (response.json())['access_token']
        # print(access_token)

        '''
        表格文字识别(同步接口)
        '''

        # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/form"
        request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
        # 二进制方式打开图片文件
        # print(filepath)
        f = open(filepath, 'rb')
        img = base64.b64encode(f.read())

        params = {"image":img}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            result = response.json()
            request_id = result['result'][0]['request_id']

        time.sleep(5)
        request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result"
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        params = {"request_id":request_id, "result_type":"excel"}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            result = (response.json())['result']['result_data']
            
            print(result)
        

if __name__ == "__main__":
    pdfPath = '2020年河南省普通高招分数段统计表(理科).pdf'
    # pdfPath = '2020年河南省普通高招分数段统计表(文科).pdf'
    imagePath = 'images'
    pyMuPDF_fitz(pdfPath, imagePath)


    g = os.walk(r"images")  

    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            # print(os.path.join(path, file_name) )
            baiduOcr(os.path.join(path, file_name))
        break


