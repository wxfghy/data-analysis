# 将本地文件传入HDFS存储
from pyhdfs import HdfsClient
client = HdfsClient(hosts='ghym:50070', user_name='hadoop')
client.copy_from_local('D:/programs/workspace/pythonworks/doubanuser/doubanuser/userdemo.txt', '/score.txt')
