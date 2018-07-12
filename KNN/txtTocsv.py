# 打开存储在HDFS上的文件
from pyhdfs import HdfsClient
client = HdfsClient(hosts='ghym:50070', user_name='hadoop')
inputfile=client.open('/score.txt')
# 转化为csv格式
import pandas as pd
df=pd.read_table(inputfile,encoding='gbk',sep=',')
df.to_csv('demo.csv',encoding='gbk',index=None,columns=['用户名','电影名','评分'])

