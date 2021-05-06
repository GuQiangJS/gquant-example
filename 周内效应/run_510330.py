import logging
logging.disable(logging.INFO)

import numpy as np
import talib
import pandas as pd
import gquant
import abupy
import QUANTAXIS as QA
import gquant.jupyter_helper
gquant.jupyter_helper.init()
from gquant.backtest import backtest
from gquant.week_effect import *


CODE='510330' #计算数据
BENCHMARK_CODE='399300' #基准代码(沪深300)
START='2012-12-25'#510300成立日期
END=QA.QAUtil.QADate.QA_util_today_str()#数据截止到今天。后面会根据不同的测试时间段对数据分段
INIT_CASH=10000#验证时的模拟初始资金
DEFAULT_MA=20#判断上涨/下跌市的SMA取值

def get_data(code=CODE,start=START,end=END,ma=DEFAULT_MA,dropna=True):
    """获取指数数据
    
    Args:
        code: 指数代码
        start: 数据开始时间
        end: 数据截止时间
        ma: 计算SMA时的时间段
    """
    data = QA.QA_fetch_index_day_adv(code,start=start,end=end).data.reset_index(level=1, drop=True)
    # 收盘价变化率
    data['收盘价变化率'] = data['close'].pct_change()
    data['date'] = data.index.get_level_values(0)
    data['date'] = pd.to_datetime(data['date'])
    # 星期一为0，星期天为6
    data['weekday'] = data['date'].dt.weekday
    # 明天星期
    data['nextday']=data['weekday'].shift(-1)
    # 昨天星期
    data['prevday']=data['weekday'].shift()
    # 简单移动均线
    data["MA"] = QA.QA_indicator_MA(data, ma)
    # 每日成交均价
    data['avg_price']=(data['close']+data['open']+data['high']+data['low'])/4
    # 每日价格变化幅度（收盘价/开盘价）
    data['日价格变化幅度']=data['close']/data['open']-1
    # TR:输出TR:(最高价-最低价)和昨收-最高价的绝对值的较大值和昨收-最低价的绝对值的较大值
    data['TR'] = TR(data)
    # 每日成交均价变化率
    data['日成交均价变化率'] = data['avg_price'].pct_change()
    # 上涨市
    data['market']=np.NaN
    data.loc[data['close']>data["MA"],'market']=1
    # 下跌市
    data['down']=False
    data.loc[data['close']<data["MA"],'market']=-1
    # 昨天是上涨市/下跌市
    data['prev_market']=data['market'].shift()

    if dropna:
        data.dropna(inplace=True)
    return data

full_data = get_data(CODE, START, END)
full_benchmark_data = get_data(BENCHMARK_CODE, START, END)

i=1
TIMES=100000
MAXTIMES=20
while i<=MAXTIMES:
    report = MonteCarloTest(full_data, full_benchmark_data,times=TIMES,multiprocessing=True)
    report.to_csv('/amount_volume_jupyter/Result_{}_{}_{}.csv'.format(CODE,TIMES*MAXTIMES,i))
    i=i+1