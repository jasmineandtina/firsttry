from pandas import read_csv
from pandas import set_option
filename='holdin/20190222.csv'
# names={'code','hold'}
data=read_csv(filename)  #,names)
set_option('display.width',50)
print(data.head(200))
print(data.describe())
print(data.skew())