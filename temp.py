import pandas as pd
import QUANTAXIS as QA
import numpy as np

hs300 = QA.QA_fetch_index_day_adv(
    '510310', start='2012-01-01', end='2021-07-11').data.reset_index(level=1, drop=True)
hs300.index.rename('datetime', inplace=True)

df = pd.read_csv('bxzj_20210711.csv', encoding='utf-8')
df.fillna(0, inplace=True)
df.set_index('datetime', inplace=True)
df['total_net_in'] = df['total_net_in_sh']+df['total_net_in_sz']


def app(row, data):
    print(row.name)
    # cate = pd.cut(data.loc[:row.name]['total_net_in'], cut,
    #               retbins=True, labels=['sell', 'keep', 'buy'])
    sp = np.array_split(
        np.array(data.loc[:row.name]['total_net_in'].sort_values()), 3)
    if len(sp) < 3 or len(sp[0]) < 1 or len(sp[1]) < 1 or len(sp[2]) < 1:
        return
    data.loc[row.name, 'cate0'] = sp[0][0]
    data.loc[row.name, 'cate1'] = sp[0][-1]
    data.loc[row.name, 'cate2'] = sp[1][0]
    data.loc[row.name, 'cate3'] = sp[1][-1]
    data.loc[row.name, 'cate4'] = sp[2][0]
    data.loc[row.name, 'cate5'] = sp[2][-1]
    # data.loc[row.name, 'cate']=sp
    if data.loc[row.name, 'total_net_in'] <= data.loc[row.name, 'cate1']:
        data.loc[row.name, 'order'] = 'sell'
    elif data.loc[row.name, 'total_net_in'] >= data.loc[row.name, 'cate4']:
        data.loc[row.name, 'order'] = 'buy'
    else:
        data.loc[row.name, 'order'] = 'keep'


df = df.join(hs300['open'])
df['next_open'] = df['open'].shift(-1)

df.apply(app, axis=1, args=[df])
print(df)
