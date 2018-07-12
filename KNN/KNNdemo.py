
# 距离公式使用欧氏距离
def euclid(a1, a2):
    # a1,a2表示两个向量,每个向量有多个维度
    distance = 0  # 欧氏距离
    for item in a1:  # item表示被评分物品
        if item in a2:  # 判断item是否同时被两个用户评价过
            score1 = a1[item]  # score代表分数
            score2 = a2[item]
            distance += pow((score1 - score2), 2)
            distance = pow(distance, 0.5)
    return distance


def itemAll(users):
    # 返回users中所有的物品item
    itemSet = set()  # set集合去重
    for user in users:
        for item in users[user]:
            itemSet.add(item)
    itemList = list(itemSet)  # 去重后转换为列表便于操作
    itemList.sort()  # 升序
    return itemList


def vect(username, users):
    # 返回代表用户username的向量
    items = itemAll(users)  # 返回所有的商品
    userVec = []  # 用户集合
    rating = users[username]  # 商品评分
    for item in items:
        if item in rating:  # 如果该商品存在评分则写入用户集合
            userVec.append(rating[item])
        else:
            userVec.append(0)  # 未评分按0写入,不影响计算
    return userVec


class KNN:
    def __init__(self, data, k, n):
        self.k = k  # KNN中与待推荐用户评分对商品评分行为最相似的前k个用户
        self.n = n  # 推荐结果的数量
        self.distance = euclid  # 欧几里得距离
        self.data = data  # 训练数据

    def compareDis(self, userName):
        # 计算用户userName与其他用户的距离，排序(距离，用户),装入列表返回
        result = []
        for user in self.data:
            if user != userName:  # 如果数据集中的用户名与传入的待推荐用户名不相同则计算,即不与自己计算
                distance = self.distance(self.data[user], self.data[userName])  # 给距离计算函数传入待推荐用户名数据和遍历数据集的用户数据
                result.append((distance, user))  # 格式为(距离，除待推荐用户意外的用户)
        result.sort()  # 升序
        return result

    def recommend(self, username):
        # 计算结果，返回推荐结果,列表形式
        result = {}
        knn = self.compareDis(username)[:self.k]  # 切片得到最近的k个用户,(距离,用户)
        userRatings = self.data[username]  # 数据集中待推荐用户的数据
        totalDis = 0.0  # 总距离
        for kuser in knn:
            totalDis += kuser[0]  # 累加k个用户与待推荐用户的距离
        for kuser in knn:
            weight = kuser[0] / totalDis  # 计算各用户的距离占比
            kname = kuser[1]  # 传入的格式为(距离,用户)
            kratings = self.data[kname]  # 再到数据集中找到K个用户的完整评分数据
            for item in kratings:
                if not item in userRatings:  # 找到待推荐用户没评价过的商品
                    if not item in result:  # 判断推荐列表中是否含有该商品了,避免重复
                        result[item] = kratings[item] * weight
                    else:
                        result[item] += kratings[item] * weight
        recom = list(result.items())  # 字典转列表
        recom.sort(key=lambda tuple: tuple[1], reverse=True)  # 按照列表中元组第二项即评分,降序排列
        return recom[:self.n]  # 返回前n个商品,评分越高越推荐的放到越前面


