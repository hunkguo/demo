from aip import AipOcr



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def main():

    """ 你的 APPID AK SK """
    APP_ID = '22692118'
    API_KEY = 'UaVDdsMRdASOEL4FEUwDlFyD'
    SECRET_KEY = '17u8kCWAQ4YzTAx7eG2lyxIiFtiO2eRd'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



    image = get_file_content('IMG_3067.png')

    """ 调用通用文字识别, 图片参数为本地图片 """
    client.basicGeneral(image);

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    ocr_result = client.basicGeneral(image)
    #print(msg['words_result'])
    for value in ocr_result['words_result']:
        dy_str = value['words']
        #print(dy_str)
        if '抖音号:' in dy_str:
            douyinID = dy_str.replace('抖音号:','')
            print("抖音号:"+douyinID)
        if '获赞' in dy_str:
            zan_pos = dy_str.find('获赞')
            guanzhu_pos = dy_str.find('关注')
            fans_pos = dy_str.find('粉丝')
            #print(type(end))
            print("获赞:"+dy_str[0:zan_pos])
            print("关注:"+dy_str[(zan_pos+4):guanzhu_pos])
            print("粉丝:"+dy_str[(guanzhu_pos+4):fans_pos])
        if '动态' in dy_str:
            dongtai_pos = dy_str.find('动态')
            print("作品:"+dy_str[2:dongtai_pos])
            print("动态:"+dy_str[(dongtai_pos+2):])


 
 


if __name__ == "__main__":
     main()