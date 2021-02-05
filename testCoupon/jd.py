import random
import time
import json
from untils.jd_api import JdApiClient
from untils.suo_im import Suo_mi
from untils.common import save_pic, del_pic
import jieba
import jieba.analyse


jieba.set_dictionary('./dict.txt')

def jingfen_query(group_material_id:str, app_key:str, secret_key:str, site_id:str, suo_mi_token:str):
    ''' 方法效率不咋地，不管了
    https://union.jd.com/openplatform/api/10421
    :return:
    '''
    info = []
    try:
        page_no = str(random.randint(1, 25))
        page_size = str(random.randint(3, 5))  # 不建议发很多，图片接口会跪

        client = JdApiClient(app_key=app_key, secret_key=secret_key)
        resp = client.call("jd.union.open.goods.jingfen.query",
                           {"goodsReq":
                                {"sort": "desc",
                                 "pageSize": page_size,
                                 "pageIndex": page_no,
                                 "eliteId": group_material_id
                                 }})
    except Exception as e:
        print(e)
        set_system_notice(f'''page_no: {page_no},\npage_size:{page_size}\n, eliteId:{group_material_id}\n发现问题''')
        jingfen_query(group_material_id, app_key, secret_key, site_id, suo_mi_token)

    # pprint.pprint(json.loads(resp.json()['jd_union_open_goods_jingfen_query_response']['result']))
    for data in json.loads(resp.json()['jd_union_open_goods_jingfen_query_response']['result'])['data']:
        #print(data)
        sku_name = data['skuName']   ## 商品全名
        print('商品名称： %s' % sku_name)

        tags = jieba.analyse.extract_tags(sku_name, topK=200, allowPOS=('ns', 'n', 'nr', 'nt', 'nz'))
        print('商品名称分词结果： %s' % tags)


        sku_id = data['skuId']     ## 商品 sku
        print('商品SKU： %s' % sku_id)
        material_url = f'''http://{(data['materialUrl'])}''' ## 商品url
        print('商品链接： %s' % material_url)

        couponInfos = data['couponInfo'] ## 优惠券列表
        # 查找最优优惠券
        coupon_link = ""
        discount = 0
        share_text = ""
        lowest_price_type = data['priceInfo']['lowestPriceType']  ## 什么类型
        is_coupon = False
        for couponInfo in couponInfos['couponList']:
            if 'isBest' in couponInfo:
                if int(couponInfo['isBest']) == 1:
                    discount = couponInfo['discount']  ## 优惠券额度
                    coupon_link = couponInfo['link']  ## 优惠券领取地址
                    is_coupon = True
            else:
                discount = couponInfo['discount']  ## 优惠券额度
                coupon_link = couponInfo['link']  ## 优惠券领取地址
                is_coupon = True
                
        if is_coupon: # 如果有券
            if lowest_price_type == 3:  # 秒杀
                price = data['seckillInfo']['seckillOriPrice'] # 原价
                lowest_price = data['priceInfo']['lowestCouponPrice'] # 秒杀价
                #duanzhi = tb_share_text(app_key, secret_key, material_url, coupon_link, site_id, suo_mi_token)
                #share_text = f'''【秒杀】{sku_name}\n——————————\n  【原价】¥{price}\n 【券后秒杀价】¥{lowest_price}\n抢购地址：{duanzhi}'''
            elif lowest_price_type == 2: # 拼购
                price = data['priceInfo']['price']  # 原价
                lowest_price = data['priceInfo']['lowestCouponPrice']  # 用券拼购
                #duanzhi = tb_share_text(app_key, secret_key, material_url, coupon_link, site_id, suo_mi_token)
                #share_text = f'''【拼购】{sku_name}\n——————————\n  【原价】¥{price}\n 【券后拼购价】¥{lowest_price}\n抢购地址：{duanzhi}'''
            else:
                price = data['priceInfo']['price'] ## 商品价格
                lowest_price = data['priceInfo']['lowestCouponPrice']
                #duanzhi = tb_share_text(app_key, secret_key, material_url, coupon_link, site_id, suo_mi_token)
                #share_text = f'''【京东】{sku_name}\n——————————\n  【爆款价】¥{price}\n 【用卷价】¥{lowest_price}\n抢购地址：{duanzhi}'''

                print()


        else: ## 如果没有券
            if lowest_price_type == 3:  # 秒杀
                price = data['seckillInfo']['seckillOriPrice']  # 原价
                lowest_price = data['seckillInfo']['seckillPrice']  # 秒杀价
                #duanzhi = tb_share_text(app_key, secret_key, material_url, coupon_link, site_id, suo_mi_token)
                #share_text = f'''【秒杀】{sku_name}\n——————————\n  【原价】¥{price}\n 【秒杀价】¥{lowest_price}\n抢购地址：{duanzhi}'''

            elif lowest_price_type == 2:  # 拼购
                price = data['priceInfo']['price']  # 原价
                lowest_price = data['priceInfo']['lowestPrice']  # 用券拼购
                #duanzhi = tb_share_text(app_key, secret_key, material_url, coupon_link, site_id, suo_mi_token)
                #share_text = f'''【拼购】{sku_name}\n——————————\n  【原价】¥{price}\n 【拼购价】¥{lowest_price}\n抢购地址：{duanzhi}'''
            else:
                lowest_price = data['priceInfo']['price']
                # 得到短址
                #duanzhi = tb_share_text(app_key, secret_key, material_url, coupon_link, site_id, suo_mi_token)
                #share_text = f'''【京东】{sku_name}\n——————————\n 【爆款价】¥{lowest_price}\n抢购地址：{duanzhi}'''

        ## 获取 images
        image_list = []
        images_count = 0
        for image in data['imageInfo']['imageList']:
            images_count += 1
            if images_count > 3: ## 3个以上图片就不发了
                pass
            else:
                image_url = image['url']
                #filename = save_pic(image_url, sku_id)
                #del_pic(filename)
                print(image_url)


def tb_share_text(app_key, secret_key, material_url, coupon_url, site_id, suo_mi_token):
    '''
    :param material_url: 物料的url
    :param coupon_url:  优惠券的url
    :param site_id:  网站id
    :param suo_mi_token: suo_mi网站的token
    :return: string ，返回一个suo_mi的短址
    '''
    print(f'''{app_key}''')
    print(f'''{secret_key}''')
    print(f'''{material_url}''')
    print(f'''{coupon_url}''')
    print(f'''{site_id}''')
    print(f'''{suo_mi_token}''')
    client = JdApiClient(app_key=app_key, secret_key=secret_key)
    if coupon_url == "":
        resp = client.call("jd.union.open.promotion.common.get",
                           {"promotionCodeReq":
                                {
                                 "siteId": site_id,
                                 "materialId": material_url
                                 }})
    else:
        resp = client.call("jd.union.open.promotion.common.get",
                           {"promotionCodeReq":
                                {
                                 "siteId": site_id,
                                 "materialId": material_url,
                                 "couponUrl": coupon_url
                                 }})
    try:
        x = json.loads(resp.json()['jd_union_open_promotion_common_get_response']['result'])['data']['clickURL']
    except Exception as e:
        print(f'''转码异常：{resp.json()}\n material_url: {material_url} \n coupon_url: {coupon_url}''')
        x = material_url
    # 直接返回短址
    url = x
    c = Suo_mi(app_key=suo_mi_token).get_short_url(url)
    return c

if __name__ == '__main__':
    #pass

    # 好券商品
    group_material_id = '1'
    app_key = 'b91b8182e5f38a47765d994e15ebf29b'
    secret_key = '33adf9a49b434ce685048bbfe0e1a8ee'
    site_id = '4100315068'
    suo_mi_token = '601d123ddac4437a6d6ab122@310d33d3c9141dc51f2703b3f4c1357d'
    jingfen_query(group_material_id, app_key, secret_key, site_id, suo_mi_token)




'''
eliteId
资源位名称
排序规则描述文案
1
好券商品
联盟运营配置的精选优惠券商品
2
精选卖场
基于推客搜索历史进行个性化推荐排序
10
9.9包邮
到手价9.9左右的低价爆品，佣金比例>5%，默认按商品综合评分排序
15
京东配送
京东配送商品，评价>100，佣金比例>10%，默认按商品综合评分排序
22
实时热销榜
近2小时全联盟热销商品排行榜
23
为你推荐
根据推客购买记录进行个性化推荐排序
24
数码家电
数码家电类商品，默认按商品综合评分排序
25
超市
超市类商品，默认按商品综合评分排序
26
母婴玩具
母婴类商品，默认按商品综合评分排序
27
家具日用
家居日用类商品，默认按商品综合评分排序
28
美妆穿搭
美妆穿搭类商品，默认按商品综合评分排序
29
医药保健
医药保健类商品，默认按商品综合评分排序
30
图书文具
图书文具类商品，默认按商品综合评分排序
31
今日必推
联盟运营配置的高佣爆品
32
京东好物
佣金比例>20%，好评率>80%，评论数>100，价格<200元的优惠券商品，默认按商品综合评分排序
33
京东秒杀
京东秒杀商品池，当前正在秒杀的商品排在前面，再以商品综合评分排序
34
拼购商品
拼购商品，默认按商品综合评分排序
40
高收益榜
佣金比例>30%，好评率>85%的销量TOP 200商品，默认按销量排序。
41
自营热卖榜
自营商品，佣金比例>3%，评论数>200的销量TOP 200商品，默认按销量排序。
109
新品首发
最近3个月新上架商品，默认按商品综合评分排序
110
自营
京东自营商品，默认按商品综合评分排序
112
京东爆品
联盟精选有券商品，价格<10000元，默认按商品综合评分排序
125
首购商品
联盟运营配置的拉新商品池
129
高佣榜单
近3天联盟支出佣金较高的商品排行榜
130
视频商品
有视频物料的商品池，可入参videoInfo获取视频物料，默认按商品综合评分排序
153
历史最低价商品榜
历史低价商品排行榜，根据历史低价优惠力度、商品综合评分排序
'''