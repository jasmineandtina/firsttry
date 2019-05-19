from pandas import read_csv
from pandas import set_option
filename='holdin/20190222.csv'
# names={'code','hold'}
data=read_csv(filename)  #,names)
set_option('display.width',50)

filecitihold='holdin/citihold.csv'


print(data.head(200))
print(data.describe())
print(data.skew())
print(data.skew())

import numpy as np
import pandas as pd ####生成9000,0000条数据，9千万条
a = np.random.standard_normal((90000000,4))
b = pd.DataFrame(a) ####普通格式存储：
h5 = pd.HDFStore('holdin/citiholdh5.h5','w')
h5['data'] = b
h5.close() ####压缩格式存储
h5 = pd.HDFStore('holdin/citiholdh5.h5','w', complevel=4, complib='blosc')
h5['data'] = b
h5.close()
