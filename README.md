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

# 策略简单测试结果

**所有的简单测试结果都并不准确，仅做示例参考。** 因为：

1. 以当日收盘价作为判断依据的同时，以当日作为建仓或清仓标准是不合理的。
2. 没有考虑交易手续费

# 📈策略实际回测

- 默认初始资金10000元。
- 默认测试日期为2014-01-01~2018-12-31。
- 默认仓位为100股。

* [回测布林带穿越上轨买入中轨卖出](#回测布林带穿越上轨买入中轨卖出)
---

## [简单布林带穿越上轨（买入）/中轨（卖出）](%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%95-%E5%B8%83%E6%9E%97%E5%B8%A6.ipynb#%E7%AE%80%E5%8D%95%E5%B8%83%E6%9E%97%E5%B8%A6%E7%A9%BF%E8%B6%8A%E4%B8%8A%E8%BD%A8%EF%BC%88%E4%B9%B0%E5%85%A5%EF%BC%89/%E4%B8%AD%E8%BD%A8%EF%BC%88%E5%8D%96%E5%87%BA%EF%BC%89)

- 收盘价上穿布林带上轨（买入）
- 收盘价下穿布林带中轨（卖出）

默认使用30日线，上下1.5倍标准差

测试了2014~2019年之间的数据。

- 盈利交易平均盈利比率:26.25%
- 最大盈利比率:72.69%
- 亏损交易平均亏损比率:-6.18%
- 最大亏损比率:-12.46%
- 平均盈亏比率:6.90%
- 交易次数:57
- 总天数:1442
- 平均持仓天数:23.40
- R(平均利润/平均损失):1.3201

## 📈[回测布林带穿越上轨（买入）/中轨（卖出）](%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%95-%E5%B8%83%E6%9E%97%E5%B8%A6.ipynb#%E5%B8%83%E6%9E%97%E5%B8%A6%E7%A9%BF%E8%B6%8A%E4%B8%8A%E8%BD%A8%EF%BC%88%E4%B9%B0%E5%85%A5%EF%BC%89/%E4%B8%AD%E8%BD%A8%EF%BC%88%E5%8D%96%E5%87%BA%EF%BC%89)

- 买入策略：收盘价上穿布林带上轨（[BuyStrategy1](#%E4%B9%B0%E5%8D%96%E7%AD%96%E7%95%A5)）
- 卖出策略：收盘价下穿布林带中轨（[SellStrategy1](#%E4%B9%B0%E5%8D%96%E7%AD%96%E7%95%A5)）
- 仓位控制：每次买入100股。（[Position1](#%E4%BB%93%E4%BD%8D%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95)）
- 总资金：10000元
- **使用30日线，上下1.5倍标准差**

|                    |            0 |
|:-------------------|-------------:|
| 盈亏总额           | 12062.4      |
| 最终价值           | 19589.8      |
| 交易次数           |    39        |
| 盈利次数           |    17        |
| 亏损次数           |    22        |
| 盈利比率           |     0.435897 |
| 每笔交易平均盈亏额 |   245.814    |
| 盈利交易平均盈利额 |   709.552    |
| 亏损交易平均亏损额 |  -112.528    |
| R                  |     2.18     |
| 最大回撤           |    -0.232387 |
| 买入平均花费       |  2501.61     |

## [] [布林带开口变化简单测试](%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%95-%E5%B8%83%E6%9E%97%E5%B8%A6.ipynb#%E5%B8%83%E6%9E%97%E5%B8%A6%E5%BC%80%E5%8F%A3%E5%8F%98%E5%8C%96)

现有测试不理想，不知道是哪里有问题。


## [均线百分比突破](%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%95-%E9%80%9A%E9%81%93%E7%AA%81%E7%A0%B4.ipynb#%E5%9D%87%E7%BA%BF%E7%99%BE%E5%88%86%E6%AF%94%E7%AA%81%E7%A0%B4)

- 收盘价上穿20日移动均线*1.05时，买入。
- 20日移动均线*1.05下穿收盘价时，卖出。

测试了2014~2019年之间的数据。

- 盈利交易平均盈利比率:14.94%
- 最大盈利比率:50.57%
- 亏损交易平均亏损比率:-2.89%
- 最大亏损比率:-11.47%
- 平均盈亏比率:0.98%
- 交易次数:69
- 总天数:1442
- 平均持仓天数:5.9420
- R(平均利润/平均损失):0.4322


## [简单通道突破](%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%95-%E9%80%9A%E9%81%93%E7%AA%81%E7%A0%B4.ipynb#%E7%AE%80%E5%8D%95%E9%80%9A%E9%81%93%E7%AA%81%E7%A0%B4)

- 上轨：过去30日最高价
- 下轨：过去10日最低价
- 当日最高价向上突破上轨，买入开仓，当日最低价跌破下轨平仓

测试了2014~2019年之间的数据。

- 盈利交易平均盈利比率:15.21%
- 最大盈利比率:65.14%
- 亏损交易平均亏损比率:-7.38%
- 最大亏损比率:-18.46%
- 平均盈亏比率:1.36%
- 交易次数:62
- 总天数:1442
- 平均持仓天数:16.95
- R(平均利润/平均损失):0.2453
