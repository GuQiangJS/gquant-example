数据文件 `300378_daily.csv` 为300378日线数据（不复权）

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

# 策略测试结果

## [简单布林带穿越上轨（买入）/中轨（卖出）](%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%95-%E5%B8%83%E6%9E%97%E5%B8%A6.ipynb#%E7%AE%80%E5%8D%95%E5%B8%83%E6%9E%97%E5%B8%A6%E7%A9%BF%E8%B6%8A%E4%B8%8A%E8%BD%A8%EF%BC%88%E4%B9%B0%E5%85%A5%EF%BC%89/%E4%B8%AD%E8%BD%A8%EF%BC%88%E5%8D%96%E5%87%BA%EF%BC%89)

- 收盘价上穿布林带上轨（买入）
- 收盘价下穿布林带中轨（卖出）

默认使用30日线，上下1.5倍标准差

测试了2014~2019年之间的数据。

- 盈利交易平均盈利比率:26.25%
- 最大盈利比率:72.69%
- 亏损交易平均亏损比率:-6.18%
- 最大亏损比率:-12.46%
- 平均:6.90%
- 交易次数:57

**问题**： 此计算方式并不准确，仅做示例参考。因为：

1. 以当日收盘价作为判断依据的同时，以当日作为建仓或清仓标准是不合理的。
2. 没有考虑交易手续费