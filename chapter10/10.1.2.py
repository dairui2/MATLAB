# Matplotlib(MATLAB+Plot+Library)库：基础的数据可视化库
# pyecharts库：Echarts库是百度开源的数据可视化图标库

from pyecharts.charts import Bar

# 创建柱状图对象
bar = Bar()

# 北京城区列表
clist = ['西城', '东城' ,'朝阳' ,'海淀' ,'大兴' ,'昌平', '丰台' ,'通州' ,'房山' ,'顺义','石景山' ,'密云' ,'延庆' ,'门头沟', '怀柔', '平谷']

# 最高房价列表
plist = [201991, 130969, 129508, 119170, 115606, 79933, 77067, 72727, 56296, 55803, 53000, 51250, 49934, 46000, 43937, 33980]

bar.add_xaxis(clist)                    #设置x轴数据
bar.add_yaxis('北京城区最高房价',plist)     #设置y轴数据

# 生成本地HTML文件，默认在当前目录下生成render.html文件；也可以生成目录参数，例如bar.render('mycharts.html')
bar.render()        #渲染图表，、

print('生成完成')