import pandas

from KNNdemo import KNN
# 文件数据格式为 用户名 电影名 评分
# 数据格式为{用户1:{商品1:评分,商品2:评分...},用户2...}
data={}
movielist=[]
with open('userdemo.txt','r',encoding='utf8') as f:
    for line in f:
        username=line.split("\t")[0]
        moviename=line.split("\t")[1]
        score=int(line.split("\t")[2])
        movielist.append((moviename,score))
        data[username]=dict(movielist)
# 根据3个相似用户为用户推荐5个电影
res = KNN(data, 3, 5).recommend('A')
# 保存为csv文件
df=pandas.DataFrame(data=res,columns=['推荐电影','推荐分数'])
df.to_csv('score.csv',index=True)