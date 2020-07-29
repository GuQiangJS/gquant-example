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

- 👍[ATR波幅通道策略](https://github.com/GuQiangJS/gquant-example/wiki/ATR波幅通道策略) [代码](策略测试-通道策略-ATR波幅通道.ipynb)

- 👍[布林带通道宽度策略](https://github.com/GuQiangJS/gquant-example/wiki/布林带通道宽度) [代码](策略测试-通道策略-布林带通道宽度.ipynb)

