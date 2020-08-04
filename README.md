读取复权数据代码：

```python
# 原始未复权数据
ori_data_df = gquant.pd.read_csv('300378_daily.csv', 
                                 encoding='utf-8', 
                                 parse_dates=[0], 
                                 dtype={'code': str}).set_index(['date', 'code'])
ori_data = QA.QAData.QA_DataStruct_Stock_day(ori_data_df)
# 前复权数据
ori_data_df_qfq = ori_data.to_qfq().data
```

**代码修正记录**：
```python
# LocalDataAPI.kline方法中遗失对start,end的处理。造成数据读取有误。参考：策略测试-通道策略-ATR波幅通道.ipynb
# 增加以下代码：
if start and end:
    return df[start:end]
elif start:
    return df[start:]
elif end:
    return df[:end]
# KLManager._fetch_pick_time_kl_pd方法中遗失对start,end的处理。造成数据读取有误。参考：策略测试-通道策略-ATR波幅通道.ipynb
# 调用abupy.MarketBu.ABuSymbolPd.make_kl_df时增加传入start和end：
data = abupy.MarketBu.ABuSymbolPd.make_kl_df(target_symbol,start=self.benchmark.start,end=self.benchmark.end)
```
以上修正需要在其他策略测试时注意。否则可能会造成使用非起始日开始的数据回测时无法回测到数据。

**数据来源**：[gquant-data](https://github.com/GuQiangJS/gquant-data)

**策略说明**:

|                                                              | 盈亏总额 | 最终价值 | 交易次数 | 盈利次数 | 亏损次数 | 盈利比率 | 每笔交易平均盈亏额 | 盈利交易平均盈利额 | 亏损交易平均亏损额 |    R | 最大回撤 | 买入平均花费 | 平均获利期望 | 平均亏损期望 | 盈亏比 | 策略年化收益 | 基准年化收益 | 赢利交易平均持股天数 | 亏损交易平均持股天数 |
| :----------------------------------------------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -----------------: | -----------------: | -----------------: | ---: | -------: | -----------: | -----------: | -----------: | -----: | -----------: | -----------: | -------------------: | -------------------: |
| [抛物线SAR+双均线交叉](策略测试-趋向策略-抛物线SAR+双均线交叉.ipynb) |  9065.55 |    16315 |       38 |       15 |       23 |     0.39 |             166.13 |             604.37 |            -119.68 | 1.39 |    -0.16 |      2436.23 |         0.19 |        -0.06 |   1.97 |         0.13 |        -0.05 |                37.88 |                14.43 |
| [布林带开口](策略测试-通道策略-布林带通道宽度.ipynb) |    21999.2 |    26921.7 |        118 |         54 |         64 |       0.46 |               143.36 |               407.39 |               -79.42 | 1.81 |      -0.23 |        2363.48 |           0.13 |          -0.03 |     6.34 |           0.36 |          -0.05 |                  20.82 |                    6.2 |
| [ATR波幅通道](策略测试-通道策略-ATR波幅通道.ipynb) |    16323.2 |    24499.1 |         52 |         28 |         24 |       0.54 |               278.74 |               582.97 |               -76.19 | 3.66 |      -0.22 |        2194.26 |           0.19 |          -0.04 |     7.63 |           0.31 |          -0.05 |                  50.59 |                  20.67 |





- 👍[ATR波幅通道策略](https://github.com/GuQiangJS/gquant-example/wiki/ATR波幅通道策略) [代码](策略测试-通道策略-ATR波幅通道.ipynb)

- 👍[布林带通道宽度策略](https://github.com/GuQiangJS/gquant-example/wiki/布林带通道宽度) [代码](策略测试-通道策略-布林带通道宽度.ipynb)

