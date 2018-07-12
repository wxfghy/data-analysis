import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
import jieba
from pylab import mpl

# 使matplotlib模块能显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['figure.figsize'] = (6.0, 4.0) # 设置图片保存的长宽比例
# 1 利用pandas从csv文件中读取数据
df = pd.read_csv('shanghai.csv', encoding = 'utf-8')

# 数字清洗
# 1 drop掉职位名称字段下含有实习两个字的记录,按索引判断,删除匹配到的所有索引号
df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)

# 2 工作经验字段格式为'3-5年',用正则匹配到两个数字,找不到数字的为'不限'或'应届',按0计
pattern = '\d+'
df['最低年限'] = df['工作经验'].str.findall(pattern)
work_year = []
for year in df['最低年限']:
    if len(year) == 0:
        work_year.append(0)
    # 如果是一个数字,就返回该数字;如果是两个数字,返回第一个
    else:
        work_year.append(int(year[0]))
df['经验'] = work_year

# 3 工资依然匹配字段中的数字,可以重复使用之前的pattern,取区间的第一个字段,即最低工资
df['最低工资'] = df['工资'].str.findall(pattern)
floor_salary = []
for sal in df['最低工资']:
    floor_salary.append(int(sal[0]))
df['月最低工资'] = floor_salary

# 4 数据清洗完成,保存为新csv文件,准备分析
df.to_csv('ok.csv', index = False)

# 数据分析
# 1 频率直方图,反映工资和职位数量关系
plt.hist(df['月最低工资'],bins = 25)
plt.xlabel('月最低工资(千元)') # 横坐标名
plt.ylabel('职位数量(个)')# 纵坐标名
plt.title("工资-职位数量统计图")# 图名
plt.savefig('工资-职位数量统计图.jpg',dpi=200)# 保存文件,分辨率200
plt.show()

# 2 圆饼图,反映职位在不同城区的分布情况,以百分数计,保留一位小数
count = df['区域'].value_counts()
plt.pie(
    count,
    startangle=90,# 从90度位置开始
    autopct='%2.1f%%',# 比例,保留一位小数
    pctdistance=1.2,# 比例离圆心距离
    explode=[0,0,0,0,0,0,0,0,0.1,0,0,0,0,0,0],# 是否让某一块远离圆心
    center=(1,0.5)# 中心位置
)
plt.axis('equal')  # 使饼图为正圆形
plt.legend(labels=count.keys(),loc='right', bbox_to_anchor=(0.1,0.5))# 显示图例
plt.savefig('城区分布图.jpg',dpi=200)
plt.show()


# 3 绘制词云,将职位福利中的字符串汇总
text = ''
for line in df['职位福利']:
    text += line# 职位福利下所有数据全写入一段字符串中
cut_text = ' '.join(jieba.cut(text))# jieba自动拆分单词装入列表
color_mask = imread('cloud.jpg')  # 设置背景图路径
cloud = WordCloud(
        font_path = 'STHeiti.ttc',# 指定字体文件位置
        background_color = 'white',# 背景色
        mask = color_mask,# 读取背景图
        max_words = 500,# 取前500个单词
        max_font_size = 100# 设置字号
        )
word_cloud = cloud.generate(cut_text)
word_cloud.to_file('word_cloud.jpg')# 可以通过wordcloud直接转换为文件
plt.imshow(word_cloud)
plt.axis('off')
plt.savefig('word.jpg',dpi=200)# 也可以通过plt读取后保存图片
plt.show()

