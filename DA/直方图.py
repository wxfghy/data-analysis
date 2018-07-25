import numpy as np
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

output_file('工资直方图.html')
colorlist=['royalblue','mediumaquamarine','darkgreen','darkorange',
           'silver','firebrick','lawngreen','palegreen','dodgerblue',
           'purple','hotpink','tan','gold']
# 本科及以下学历

df1 = pd.read_csv('sal01.csv',encoding='utf8')
pattern = '\d+'

df1['工资数字'] = df1['工资'].str.findall(pattern)
floor_sal=[]
for sal in df1['工资数字']:
    floor_sal.append(int(sal[0]))
df1['最低工资'] = floor_sal
ceil_sal=[]
for sal in df1['工资数字']:
    ceil_sal.append(int(sal[1]))
df1['最高工资'] = ceil_sal

p1 = figure(title='本科及以下-最低工资')
hist, bin_edges = np.histogram(df1['最低工资'],bins=30)
# bin_edges : (length(hist)+1)
p1.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:],
        fill_color=colorlist[3], line_color='white',fill_alpha=0.6)
p1.xaxis.axis_label = '工资 (千元/月)'
p1.yaxis.axis_label = '职位数 (个)'
p1.width = 500
p1.height = 500
p1.background_fill_color = 'white'

p2 = figure(title='本科及以下-最高工资')
hist, bin_edges = np.histogram(df1['最高工资'],bins=30)
# bin_edges : (length(hist)+1)
p2.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:],
        fill_color=colorlist[3], line_color='white', fill_alpha=0.6)
p2.xaxis.axis_label = '工资 (千元/月)'
p2.yaxis.axis_label = '职位数 (个)'
p2.width = 500
p2.height = 500
p2.background_fill_color = 'white'

# 硕士及以上学历

df2 = pd.read_csv('sal02.csv',encoding='utf8')
pattern = '\d+'

df2['工资数字'] = df2['工资'].str.findall(pattern)
floor_sal=[]
for sal in df2['工资数字']:
    floor_sal.append(int(sal[0]))
df2['最低工资'] = floor_sal
ceil_sal=[]
for sal in df2['工资数字']:
    ceil_sal.append(int(sal[1]))
df2['最高工资'] = ceil_sal

p3 = figure(title='硕士及以上-最低工资')
hist, bin_edges = np.histogram(df2['最低工资'],bins=30)
# bin_edges : (length(hist)+1)
p3.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:],
        fill_color=colorlist[0], line_color='white', fill_alpha=0.6)
p3.xaxis.axis_label = '工资 (千元/月)'
p3.yaxis.axis_label = '职位数 (个)'
p3.width = 500
p3.height = 500
p3.background_fill_color = 'white'

p4 = figure(title='硕士及以上-最高工资')
hist, bin_edges = np.histogram(df2['最高工资'],bins=30)
# bin_edges : (length(hist)+1)
p4.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:],
        fill_color=colorlist[0], line_color='white', fill_alpha=0.6)
p4.xaxis.axis_label = '工资 (千元/月)'
p4.yaxis.axis_label = '职位数 (个)'
p4.width = 500
p4.height = 500
p4.background_fill_color = 'white'

# 汇总

df3 = pd.read_csv('total.csv',encoding='utf8')
pattern = '\d+'

df3['工资数字'] = df3['工资'].str.findall(pattern)
floor_sal=[]
for sal in df3['工资数字']:
    floor_sal.append(int(sal[0]))
df3['最低工资'] = floor_sal
ceil_sal=[]
for sal in df3['工资数字']:
    ceil_sal.append(int(sal[1]))
df3['最高工资'] = ceil_sal

p5 = figure(title='汇总-最低工资')
hist, bin_edges = np.histogram(df3['最低工资'],bins=30)
# bin_edges : (length(hist)+1)
p5.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:],
        fill_color=colorlist[6], line_color='white', fill_alpha=0.6)
p5.xaxis.axis_label = '工资 (千元/月)'
p5.yaxis.axis_label = '职位数 (个)'
p5.width = 500
p5.height = 500
p5.background_fill_color = 'white'

p6 = figure(title='汇总-最高工资')
hist, bin_edges = np.histogram(df3['最高工资'],bins=30)
# bin_edges : (length(hist)+1)
p6.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:],
        fill_color=colorlist[6], line_color='white', fill_alpha=0.6)
p6.xaxis.axis_label = '工资 (千元/月)'
p6.yaxis.axis_label = '职位数 (个)'
p6.width = 500
p6.height = 500
p6.background_fill_color = 'white'

show(gridplot(p5,p6,p1,p2,p3,p4, ncols=2))
