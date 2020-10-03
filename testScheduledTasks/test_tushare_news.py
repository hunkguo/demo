# -*- coding:utf-8 -*-
import tushare as ts
from pandas import DataFrame

ts.set_token('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
pro = ts.pro_api()

def main():
    df = pro.news(src='sina', start_date='2018-11-21 09:00:00', end_date='2018-11-22 10:10:00')
    print(df)

if __name__ == "__main__":
    main()