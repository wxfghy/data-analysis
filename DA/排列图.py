from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import dodge, factor_cmap
import pandas as pd
# # 数据清洗,获得招聘岗位数量前十的公司记录
# df1 = pd.read_csv('total.csv',encoding='utf8')
# coms = df1['公司简称'].value_counts()
# comlist = list(coms.keys())[:10]
# indlist=[]
# for i in range(len(comlist)):
#     ind = df1[df1.公司简称 == comlist[i]].index
#     indlist.append(ind[0])
# for ind in indlist:
#     line = df1.loc[df1.index == ind]
#     line.to_csv(f'{ind}.csv',index=False)# 合并后去除重复项,保留10条数据

# 招聘数量前10的公司数据
df = pd.read_csv('top10.csv',encoding='utf8')
# df = df[:50]# 切片取前50条
# 横纵坐标,字符串列表形式
xrange=[]
for money in df['区域']:
    if money not in xrange:
        xrange.append(money)
yrange=[]
for area in df['公司简称']:
    if area not in yrange:
        yrange.append(area)
print(xrange,yrange)# 打印一下看看坐标是否符合预期
# 按'区域'字段给定不同颜色
colorlist=['royalblue','mediumaquamarine','darkgreen','darkorange',
           'silver','firebrick','lawngreen','palegreen','dodgerblue',
           'purple','hotpink','tan','gold']
cmap = dict(zip(xrange,colorlist[:len(yrange)]))# 拉链后为元组,直接转化字典作颜色集合
TOOLS = "pan,wheel_zoom,reset,hover,save"# 加载工具,拖动,滚动缩放,重置,鼠标悬停,保存
# 悬停时显示的字段@{字段名}去df中找字符串
TOOLTIPS = [
    ("公司全名", "@{公司全名}"),
    ("公司规模", "@{公司规模}"),
    ("融资阶段", "@{融资阶段}"),
]
# 画图主函数figure
p = figure(title="公司介绍", plot_width=600, plot_height=800,
           x_range=xrange, y_range=yrange,
           tools=TOOLS, toolbar_location="left", tooltips=TOOLTIPS)
# rect矩阵,按x,y坐标字段指定位置,长宽为95%,透明度0.6,以区域做图例
p.rect('区域', "公司简称", 0.95, 0.95, source=df, fill_alpha=0.6, legend="区域",
       color=factor_cmap('区域', palette=list(cmap.values()), factors=list(cmap.keys())))
# 矩形内显示的内容
text_props = {"source": df, "text_align": "left", "text_baseline": "top"}
x = dodge("区域", -0.4, range=p.x_range)# 左移0.4
y = dodge('公司简称', 0.3, range=p.y_range)# 上移0.3
# 第一行内容
r = p.text(x=x, y='公司简称', text="公司简称", **text_props)
r.glyph.text_font_style="bold"# 黑体
r.glyph.text_font_size="6pt"# 字号
# 第二行内容,在第一行上边
r = p.text(x=x, y=y, text="区域", **text_props)
r.glyph.text_font_size="8pt"
# 规定其他参数
p.outline_line_color = None
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_standoff = 0
#p.legend.orientation = "horizontal"# 水平显示图例
p.legend.location ="top_right"# 图例位于顶部偏右
# 输出文件
output_file("排列图.html")
show(p)