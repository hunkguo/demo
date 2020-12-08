#!/user/bin/env python
# -*- coding:utf-8 -*-
"""
@file_name: get_data_from_tushare.py
@author:
@email:
@datetime:2019/12/24 19:21
@software: PyCharm
@disc: 
@hint:
"""
# Factor_0、规模因子（总市值）
# Factor_1、市盈率
# Factor_2、成长因子（营业利润同比增长）
# Factor_3、ROE
# Factor_4、动量（过去20天涨幅值）
# Factor_5、波动因子（过去20天波动率）
import os
import time
import tushare as ts
import pandas as pd
import numpy as np
from config import *    #在这里导入tushare的key

class GetDatafromTushare():

    def __init__(self):
        pass

    def get_all_stocks(self):
        """
        得到所有股票的行情
        :return:
        """
        pro = ts.pro_api(key)
        data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        # 选出上市时间在2019-03-31之前的股票
        stocks_data = data[data.list_date<'20190331']
        # stocks_data = stocks_data.loc[0:200]   # 这句只是为了测试，后面需要删掉
        return stocks_data

    def get_market_trading_days(self,startdate,enddate):
        """
        取交易所交易的日期
        :param startdate: 开始日期
        :param enddate: 结束日期
        :return:
        """
        pro = ts.pro_api(key)
        tradedate_df = pro.trade_cal(exchange='', start_date=startdate, end_date=enddate, is_open=1)
        trading_days = tradedate_df.cal_date.tolist()
        return trading_days

    def get_index_weight(self):

        # 指数的权重
        if os.path.exists('./data/zz500_weight.csv'):
            pass
        else:
            stock_list = self.get_all_stocks().ts_code.tolist()
            trading_days = self.get_market_trading_days(begD,endD)
            index_weight_df = pd.DataFrame([],index=trading_days,columns=stock_list)
            pro = ts.pro_api(key)
            # 这里注意：取少量没问题，取多的话只出最近一年的数据，最好是分时间段去取
            df = pro.index_weight(index_code=benchmark, start_date=begD, end_date=endD)
            for i,stock in enumerate(stock_list):
                print(i,stock)
                stock_df = df[df.con_code==stock]
                if len(stock_df)>0:
                    stock_df = stock_df.sort_values(by=['trade_date'], axis=0, ascending=True)
                    # stock_df.reset_index(drop='index',inplace=True)
                    # # 后一个交易日
                    # for j in range(len(stock_df)):
                    #     datelist = [date for date in trading_days if date >= stock_df.loc[j, 'trade_date']]
                    #     if datelist:
                    #         next_tradedate = datelist[0]
                    #     else:
                    #         next_tradedate = stock_df.loc[j, 'trade_date']
                    #     stock_df.loc[j, 'next_date'] = next_tradedate
                    # stock_df.set_index('next_date', inplace=True)
                    stock_df.set_index('trade_date', inplace=True)
                    index_weight_df[stock] = stock_df.weight/100
                else:
                    index_weight_df[stock] = 0
            index_weight_df = index_weight_df.fillna(method='pad')
            index_weight_df = index_weight_df.fillna(0)
            index_weight_df.to_csv('./data/zz500_weight.csv')
        return 0

    def get_all_stocks_history_kline_qfq(self):
        """
        得到所有股票的2008年到现在的所有日线close的行情
        :return:
        """
        if os.path.exists('./data/twap_stock.csv'):
            all_stock_twap_df = pd.read_csv('./data/twap_stock.csv',index_col=0)
        else:
            all_stocks_list = self.get_all_stocks().ts_code.tolist()
            trading_days = self.get_market_trading_days(data_begD,data_endD)
            api = ts.pro_api(key)

            all_stock_twap_df = pd.DataFrame([],index=trading_days,columns=all_stocks_list)
            for i, stock in enumerate(all_stocks_list):
                print(i, stock)
                df = ts.pro_bar(api=api, ts_code=stock, adj='qfq', start_date=data_begD, end_date=data_endD)
                df = df.sort_values(by=['trade_date'], axis=0, ascending=True)
                df.set_index('trade_date', inplace=True)
                all_stock_twap_df[stock] = df.close

            all_stock_twap_df.to_csv('./data/twap_stock.csv')

        return all_stock_twap_df

    def get_factors_raw_data(self):

        """
        得到每个股票的原始因子数据
        # Factor_0、规模因子（总市值）
        # Factor_1、市盈率
        # Factor_2、成长因子（营业利润同比增长）
        # Factor_3、ROE
        # Factor_4、动量（过去20天涨幅值）
        # Factor_5、波动因子（过去20天波动率）
        :return:
        """
        pro = ts.pro_api(key)
        all_stocks_list = self.get_all_stocks().ts_code.tolist()
        trading_days = self.get_market_trading_days(data_begD, data_endD)
        market_cap_df = pd.DataFrame([], index=trading_days, columns=all_stocks_list)   # 市值
        pe_df = pd.DataFrame([], index=trading_days, columns=all_stocks_list)   # pe——ttm
        roe_df = pd.DataFrame([], index=trading_days, columns=all_stocks_list)  #q_roe 净资产收益率(单季度)
        op_df = pd.DataFrame([], index=trading_days, columns=all_stocks_list)   #op_yoy 营业利润同比增长率(%)
        momentum_df = pd.DataFrame([], index=trading_days, columns=all_stocks_list)  #动量（过去20天涨幅值）
        volatility_df = pd.DataFrame([], index=trading_days, columns=all_stocks_list)  #波动因子（过去20天波动率）

        # Factor_0、规模因子（总市值）
        # Factor_1、市盈率
        if os.path.exists('./data/Factor_0.csv'):
            pass
        else:
            all_df = pd.DataFrame()
            for i,datestr in enumerate(trading_days):
                print(i,datestr)
                df = pro.daily_basic(ts_code='', trade_date=datestr,fields='ts_code,trade_date,total_mv,pe')
                all_df = pd.concat([all_df,df],axis=0,ignore_index=True)

            stocks_of_df = list(set(all_df.ts_code.tolist()))
            for i,stock in enumerate(all_stocks_list):
                print(i,stock)
                stock_df = all_df[all_df.ts_code==stock]
                if isinstance(stock_df,pd.DataFrame):
                    stock_df = stock_df.sort_values(by=['trade_date'], axis=0, ascending=True)
                    stock_df.set_index('trade_date',inplace=True)
                    # market_cap_df[stock] = stock_df.total_mv
                    # pe_df[stock] = stock_df.pe
                    market_cap_df.loc[stock_df.index, stock] = stock_df.total_mv.values
                    pe_df.loc[stock_df.index, stock] = stock_df.pe.values
                else:
                    market_cap_df[stock] = np.nan
                    pe_df[stock] = np.nan
            # market_cap_df = market_cap_df.fillna(method='pad')
            # pe_df = pe_df.fillna(method='pad')
            market_cap_df.to_csv('./data/Factor_0.csv')
            pe_df.to_csv('./data/Factor_1.csv')
        print('=======完成Factor0、1取数据===========')
        # =======完成Factor0、1取数据===========

        # Factor_2、成长因子（营业利润同比增长）
        # Factor_3、ROE
        rpt_datelist = ['20121231', '20130331', '20130630', '20130930', '20131231'
            , '20140331', '20140630', '20140930', '20141231'
            , '20150331', '20150630', '20150930', '20151231'
            , '20160331', '20160630', '20160930', '20161231'
            , '20170331', '20170630', '20170930', '20171231'
            , '20180331', '20180630', '20180930', '20181231'
            , '20190331']
        block_date_list = [[date for date in trading_days if date >= rpt_datelist[i] and date < rpt_datelist[i + 1]] for
                           i in range(len(rpt_datelist) - 1)]
        block_len_list = [len(ls) for ls in block_date_list]
        roe_rpt_data_df = pd.DataFrame([], index=rpt_datelist[:-1])
        op_rpt_data_df = pd.DataFrame([], index=rpt_datelist[:-1])
        if os.path.exists('./data/Factor_2.csv'):
            pass
        else:
            for i, stock in enumerate(all_stocks_list):
                print(i, stock)
                stock_df = pro.query('fina_indicator', ts_code=stock, fields='ts_code,ann_date,end_date,q_roe,op_yoy',
                                     start_date='20121231', end_date='20190329')
                if isinstance(stock_df, pd.DataFrame):
                    stock_df = stock_df.sort_values(by=['end_date'], axis=0, ascending=True)
                    stock_df.set_index('end_date', inplace=True)
                    roe_stock_df = stock_df[['q_roe']]
                    op_stock_df = stock_df[['op_yoy']]
                    roe_rpt_data_df = pd.concat([roe_rpt_data_df, roe_stock_df], axis=1, join='outer')
                    op_rpt_data_df = pd.concat([op_rpt_data_df, op_stock_df], axis=1, join='outer')

                    # roe_rpt_data_df.loc[stock_df.index, stock] = stock_df.q_roe.values
                    # op_rpt_data_df.loc[stock_df.index, stock] = stock_df.op_yoy.values
                else:
                    roe_df[stock] = np.nan
                    op_df[stock] = np.nan
                roe_rpt_data_df.rename(columns={'q_roe': stock}, inplace=True)
                op_rpt_data_df.rename(columns={'op_yoy': stock}, inplace=True)
                time.sleep(0.5)
            roe_rpt_data_df.to_csv('./data/roe_rpt_data_df.csv')
            op_rpt_data_df.to_csv('./data/op_rpt_data_df.csv')
            # end_date_list = stock_df.end_date.tolist()
            # ind_list = [rpt_datelist.index(end_date) for end_date in end_date_list]
            # len_list = [block_len_list[l] for l in ind_list]
            roe_all_block_data_list = []
            op_all_block_data_list = []
            for i in range(len(roe_rpt_data_df)):
                roe_block_data_list = [roe_rpt_data_df.iloc[i, :].tolist()] * block_len_list[i]
                roe_all_block_data_list = roe_all_block_data_list + roe_block_data_list
            for i in range(len(op_rpt_data_df)):
                op_block_data_list = [op_rpt_data_df.iloc[i, :].tolist()] * block_len_list[i]
                op_all_block_data_list = op_all_block_data_list + op_block_data_list
            roe_df = pd.DataFrame(roe_all_block_data_list, index=trading_days, columns=all_stocks_list)
            op_df = pd.DataFrame(op_all_block_data_list, index=trading_days, columns=all_stocks_list)
            roe_df = roe_df.fillna(method='pad')
            op_df = op_df.fillna(method='pad')
            roe_df.to_csv('./data/Factor_2.csv')
            op_df.to_csv('./data/Factor_3.csv')
        print('=======完成Factor2、3取数据===========')
        # =======完成Factor2、3取数据===========

        # Factor_4、动量（过去20天涨幅值）
        # Factor_5、波动因子（过去20天波动率）
        if os.path.exists('./data/Factor_4.csv'):
            pass
        else:
            all_stock_twap_df = self.get_all_stocks_history_kline_qfq()
            momentum_df = all_stock_twap_df.pct_change(20)  # 动量（过去20天涨幅值）
            pct_change_df = all_stock_twap_df.pct_change(1)
            volatility_df = pct_change_df.rolling(20).std()  # 波动率（过去20天波动率）
            momentum_df.index = all_stock_twap_df.index
            volatility_df.index = all_stock_twap_df.index
            momentum_df.to_csv('./data/Factor_4.csv')
            volatility_df.to_csv('./data/Factor_5.csv')
        print('=======完成Factor4、5取数据===========')
        # =======完成Factor4、5取数据===========

        return 0

    def get_index_history_kline(self):
        """
        得到指数历史行情
        :return:
        """
        pro = ts.pro_api(key)
        df = pro.index_daily(ts_code=benchmark, start_date=data_begD, end_date=data_endD)
        df = df.sort_values(by=['trade_date'], axis=0, ascending=True)
        df.set_index('trade_date', inplace=True)
        index_df = df[['close']]
        index_df.rename(columns = {'close':benchmark},inplace=True)
        index_df.to_csv('./data/twap_index.csv')
        return index_df

    def get_industry_classified(self):
        df = ts.get_industry_classified()
        for i in range(len(df)):
            if df.loc[i,'code'].startswith('6'):
                df.loc[i, 'ts_code'] = df.loc[i, 'code'] + '.SH'
            else:
                df.loc[i, 'ts_code'] = df.loc[i, 'code'] + '.SZ'
        ind_df = df[['ts_code','c_name']]
        ind_df.to_csv('./data/industry.csv',encoding='GBK')
        return ind_df

if __name__=="__main__":

    obj = GetDatafromTushare()
    pro = ts.pro_api(key)
    # obj.get_industry_classified()   # 放弃，这里的行业分类有问题，后面是从wind里面导出的行业
    # obj.get_index_history_kline()
    obj.get_index_weight()
    # obj.get_all_stocks_history_kline_qfq()
    # obj.get_factors_raw_data()