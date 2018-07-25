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
df = pd.read_csv('total.csv', encoding = 'utf-8')

# 3 绘制词云,将职位福利中的字符串汇总
text = ''
for line in df['职位福利']:
    text += line# 职位福利下所有数据全写入一段字符串中
cut_text = ' '.join(jieba.cut(text))# jieba自动拆分单词装入列表
color_mask = imread('love.jpg')  # 设置背景图路径
cloud = WordCloud(
        font_path = 'STHeiti.ttc',# 指定字体文件位置
        background_color = 'white',# 背景色
        mask = color_mask,# 读取背景图
        max_words = 500,# 取前500个单词
        max_font_size = 200# 设置字号
        )
word_cloud = cloud.generate(cut_text)
word_cloud.to_file('职位福利词云图.jpg')# 可以通过wordcloud直接转换为文件
plt.imshow(word_cloud)
plt.axis('off')
#plt.savefig('word.jpg',dpi=200)# 也可以通过plt读取后保存图片
plt.show()