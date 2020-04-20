# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd
import h5py
import datetime

# 以股票找信息
class stock:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        
        # 获取所属行业,最后一个
        df_stock_in_index_member = pro.index_member(ts_code='600000.SH').tail(1)
        #print(df_stock_in_index_member.values[0][0])
        
        #获取分类的成份股
        df_index_member = pro.index_member(index_code=df_stock_in_index_member.values[0][0], fields='index_code, con_code, in_date')
        #print(df_index_member)
        
        for index_member_stock in df_index_member.iterrows():
            #balancesheet
            print(index_member_stock[1]['con_code'])
            stock_code = index_member_stock[1]['con_code']
            stock_balancesheet = pro.balancesheet(ts_code=stock_code)
            # 资产总计
            print(stock_balancesheet.head(1)['total_assets'])
            break
        
class index:
    def init(self):
        pass
    
    def run(self):
        # 初始化
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        

        # 指数
        # df_index = pro.index_basic(market='CSI', category='主题指数')
        df_index = pro.index_dailybasic(trade_date='20191213', fields='ts_code,trade_date,turnover_rate,pe')
        print(df_index)


# 根据股票所属行业筛选同行业其他股票
class same_industry_stock:
    def init(self):
        pass
    def run(self):
        # 初始化tushare接口
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')

        # 查询当前所有正常上市交易的股票列表
        all_stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

        #print(all_stocks)
        # 查询股票所属行业
        stock_industry = all_stocks[all_stocks['ts_code']=='600519.SH']
        
        # 筛选同行业股票
        same_industry_stock = all_stocks[all_stocks['industry']==stock_industry['industry'].values[0]]
        #print(same_industry_stock)
        #print(type(stock_industry['industry'].values[0]))
        
        
        # 筛选ROE>10的股票
        same_industry_stock_roe = pd.DataFrame()
        for stock in same_industry_stock.iterrows():
            #print(type(stock[1]["ts_code"]))
            # ROE>10%
            fina_indicator = pro.fina_indicator(ts_code=stock[1]["ts_code"]).head(1)
            
            ts_code = fina_indicator["ts_code"].values[0]
            roe = fina_indicator["roe"].values[0]
            if roe > 10:
                stock = [[ts_code, roe]]
                same_industry_stock_roe = same_industry_stock_roe.append(stock)
        print(same_industry_stock_roe)


# 获取上市公司公告
class announcement:
    def __init__(self):
        # 判断h5文件更新日期，超过即更新
        # 股票代码、交易日历、
        # 初始化tushare接口
        self.pro = ts.pro_api('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
        self.hdfsFile = 'common_data.h5'
        # 判断首次运行
        self.firstInit = True

    def writeH5(self, h5Key, dfData):
        # 写h5
        store = pd.HDFStore(self.hdfsFile,'a', complevel=4, complib='blosc')
        store[h5Key] = dfData
        store.close()

    def readH5(self, h5Key):
        # 读h5
        data=pd.read_hdf(self.hdfsFile,key=h5Key)
        return data

    def getCal(self):
        try:
            data_cal = self.readH5('cal')
        except:
            data_cal = self.pro.trade_cal(exchange='')
            self.writeH5('cal', df_cal)
        return data_cal

    def getStock(self):
        try:
            data_stock = self.readH5('stock')
        except:
            data_stock = self.pro.stock_basic(exchange='', list_status='L')
            self.writeH5('stock', df_stock)
        return data_stock

    def getAnnouncement(self, ts_code, last_month, curr_month):
        try:
            data_announcement = self.readH5('announcement')
        except:
            #获取最新的50条公告数据
            data_announcement = self.pro.anns(ts_code=ts_code, start_date=last_month ,end_date=curr_month )
            self.writeH5('announcement', data_announcement)
        return df_stock



    def run(self,data_month, data_stock):


        for stock in data_stock.iterrows():
            ts_code = stock[1]["ts_code"]

            last_month = data_month[0]
            for curr_month in data_month:
                if(last_month == curr_month):
                    continue
                self.getAnnouncement(ts_code, last_month, curr_month)


                last_month = curr_month

            '''
        

            for anns in df_announcement.iterrows():
                print(anns[1]["ts_code"])
                print(anns[1]["ann_date"])
                print(anns[1]["ann_type"])
                print(anns[1]["title"])
                print(anns[1]["pub_time"])
                
                #print(anns[1]["content"])
            '''

    def test(self):
        today = datetime.datetime.today().date() 
        data_month = pd.date_range('2000-01-01',today,freq='MS').strftime("%Y%m%d").tolist()
        return(data_month)

        
if __name__ == "__main__":
    
    s = announcement()
    #data_cal = s.getCal()
    data_stock = s.getStock()
    data_month = s.test()
    s.run(data_month, data_stock)
