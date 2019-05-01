from pandas import read_csv

filename='holdin/20190222.csv'
# names={'code','hold'}
data=read_csv(filename)  #,names)

print(data.head(20))
