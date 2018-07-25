import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

# 使matplotlib模块能显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['figure.figsize'] = (7.0, 4.0) # 设置图片保存的长宽比例
# 1 利用pandas从csv文件中读取数据
df = pd.read_csv('total.csv', encoding = 'utf-8')
# 给定颜色集合
colorlist=['royalblue','mediumaquamarine','darkgreen','darkorange',
           'silver','firebrick','lawngreen','palegreen','dodgerblue',
           'purple','hotpink','tan','gold']
# 2 圆饼图,反映招聘岗位数前三的城区,以百分数计,保留一位小数
count = df['区域'].value_counts()
patches,text,autotexts=plt.pie(
    count[:3],
    startangle=90,# 从90度位置开始
    autopct='%2.1f%%',# 比例,保留一位小数
    pctdistance=1.2,# 比例离圆心距离
    center=(1,0.5),# 中心位置
    colors=colorlist[:3],
)
# 透明度
for i, p in enumerate(patches):
    p.set_alpha(0.6*(i+1))

plt.axis('equal')  # 使饼图为正圆形
plt.legend(labels=count.keys(),loc='right', bbox_to_anchor=(0.1,0.5))# 显示图例
plt.savefig('区域分布图.jpg',dpi=200)
plt.show()

# 反映招聘岗位数前十的公司
count = df['公司简称'].value_counts()
patches,text,autotexts=plt.pie(
    count[:10],
    startangle=90,# 从90度位置开始
    autopct='%2.1f%%',# 比例,保留一位小数
    pctdistance=1.2,# 比例离圆心距离
    center=(1,0.5),# 中心位置
    colors=colorlist[:10]
)
for i, p in enumerate(patches):
    p.set_alpha(0.6*(i+1))
plt.axis('equal')  # 使饼图为正圆形
plt.legend(labels=count.keys(),loc='right', bbox_to_anchor=(0.1,0.5))# 显示图例
plt.savefig('公司分布图.jpg',dpi=200)
plt.show()

# 反映融资阶段
count = df['融资阶段'].value_counts()
patches,text,autotexts=plt.pie(
    count,
    startangle=90,# 从90度位置开始
    autopct='%2.1f%%',# 比例,保留一位小数
    pctdistance=1.2,# 比例离圆心距离
    center=(1,0.5),# 中心位置
    colors=colorlist[:len(count)]
)
for i, p in enumerate(patches):
    p.set_alpha(0.6*(i+1))
plt.axis('equal')  # 使饼图为正圆形
plt.legend(labels=count.keys(),loc='right', bbox_to_anchor=(0.1,0.5))# 显示图例
plt.savefig('融资阶段分布图.jpg',dpi=200)
plt.show()