
**策略说明**:

|                                                              | 盈亏总额 | 最终价值 | 交易次数 | 盈利次数 | 亏损次数 | 盈利比率 | 每笔交易平均盈亏额 | 盈利交易平均盈利额 | 亏损交易平均亏损额 |    R | 最大回撤 | 买入平均花费 | 平均获利期望 | 平均亏损期望 | 盈亏比 | 策略年化收益 | 基准年化收益 | 赢利交易平均持股天数 | 亏损交易平均持股天数 |
| :----------------------------------------------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -----------------: | -----------------: | -----------------: | ---: | -------: | -----------: | -----------: | -----------: | -----: | -----------: | -----------: | -------------------: | -------------------: |
| [抛物线SAR+双均线交叉](策略测试-趋向策略-抛物线SAR+双均线交叉.ipynb) |  9065.55 |    16315 |       38 |       15 |       23 |     0.39 |             166.13 |             604.37 |            -119.68 | 1.39 |    -0.16 |      2436.23 |         0.19 |        -0.06 |   1.97 |         0.13 |        -0.05 |                37.88 |                14.43 |
| [布林带开口](策略测试-通道策略-布林带通道宽度.ipynb) |    12493.4 |    22368.3 |         15 |         14 |          1 |       0.93 |                824.3 |               892.39 |              -128.83 | 6.4 |      -0.26 |        3054.88 |           0.26 |          -0.07 |    11.73 |           0.26 |          -0.05 |                  58.74 |                     22 |
| [ATR波幅通道](策略测试-通道策略-ATR波幅通道.ipynb) |    16323.2 |    24499.1 |         52 |         28 |         24 |       0.54 |               278.74 |               582.97 |               -76.19 | 3.66 |      -0.22 |        2194.26 |           0.19 |          -0.04 |     7.63 |           0.31 |          -0.05 |                  50.59 |                  20.67 |
| [CTA-收盘价交叉移动均线+趋势判断](策略测试-交叉策略-CTA-收盘价交叉移动均线+趋势判断.ipynb) |  5420.13 |    14180.8 |         19 |          8 |         11 |       0.42 |               219.97 |               677.52 |              -112.79 | 1.95 |      -0.11 |        2516.46 |           0.19 |          -0.04 |     4.94 |           0.09 |          -0.05 |                  28.25 |                   6.55 |

---

* [ETF穿越120日均线](ETF穿越120日均线.ipynb)

|        |   基准收益 |   策略收益 |   基准年化收益 |   策略年化收益 |   基准最大回撤 |   策略最大回撤 |
|-------:|-----------:|-----------:|---------------:|---------------:|---------------:|---------------:|
| 510300 |   0.583337 |   0.629848 |      0.0787442 |      0.0850226 |      -0.461035 |      -0.176836 |
| 510310 |   0.794892 |   0.905159 |      0.120365  |      0.137062  |      -0.456236 |      -0.192224 |

* [ETF周内效应(510310)](ETF周内效应-沪深300-510310.ipynb)

|                       |   基准浮动盈亏(基准最后收盘/基准最先开盘)cumsum |   浮动盈亏(结算价值/初始资金)cumsum |   基准浮动盈亏(基准最后收盘/基准最先开盘) |   浮动盈亏(结算价值/初始资金) |   基准最大回撤 |   策略最大回撤 |
|:----------------------|------------------------------------------------:|------------------------------------:|------------------------------------------:|------------------------------:|---------------:|---------------:|
| 2016-01-01~2016-12-31 |                                        0.908197 |                             1.11078 |                                  0.908197 |                      1.11078  |     -0.186782  |     -0.0649591 |
| 2017-01-01~2017-12-31 |                                        2.14141  |                             2.18985 |                                  1.23321  |                      1.07907  |     -0.0617413 |     -0.023934  |
| 2018-01-01~2018-12-31 |                                        2.90237  |                             3.14234 |                                  0.760959 |                      0.952491 |     -0.306485  |     -0.142651  |
| 2019-01-01~2019-12-31 |                                        4.29028  |                             4.48582 |                                  1.38791  |                      1.34348  |     -0.132188  |     -0.100598  |
| 2020-01-01~2020-12-31 |                                        5.58639  |                             5.70247 |                                  1.29611  |                      1.21665  |     -0.156608  |     -0.128704  |

* [ETF周内效应(159915)](ETF周内效应-创业板159915.ipynb)

|                       |   基准浮动盈亏(基准最后收盘/基准最先开盘)cumsum |   浮动盈亏(结算价值/初始资金)cumsum |   基准浮动盈亏(基准最后收盘/基准最先开盘) |   浮动盈亏(结算价值/初始资金) |   基准最大回撤 |   策略最大回撤 |
|:----------------------|------------------------------------------------:|------------------------------------:|------------------------------------------:|------------------------------:|---------------:|---------------:|
| 2016-01-01~2016-12-31 |                                        0.743185 |                             1.04292 |                                  0.743185 |                      1.04292  |      -0.235353 |      -0.138827 |
| 2017-01-01~2017-12-31 |                                        1.61672  |                             1.96406 |                                  0.873539 |                      0.921143 |      -0.177495 |      -0.142027 |
| 2018-01-01~2018-12-31 |                                        2.34036  |                             2.84984 |                                  0.723636 |                      0.885771 |      -0.356348 |      -0.217943 |
| 2019-01-01~2019-12-31 |                                        3.78443  |                             4.10578 |                                  1.44407  |                      1.25594  |      -0.198336 |      -0.115312 |
| 2020-01-01~2020-12-31 |                                        5.42872  |                             5.70559 |                                  1.64429  |                      1.59982  |      -0.197064 |      -0.109    |

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
