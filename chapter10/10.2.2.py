# 链式API:对象调用它的函数时，还会返回对象本身，这样才可以连续调用。链式API常用语函数式编程语言中，pyecharts支持链式API。
# 对象A.函数1().函数2().函数3().函数4(): 对象A.函数1()返回对象A; 对象A.函数1().函数2()返回对象A; 对象A.函数1().函数2().函数3()返回对象A

from pyecharts.charts import Line
from pyecharts import options as opts

# 城区列表
clist = ['西城', '东城' ,'朝阳' ,'海淀' ,'大兴' ,'昌平', '丰台' ,'通州' ,'房山' ,'顺义','石景山' ,'密云' ,'延庆' ,'门头沟', '怀柔', '平谷']
# 最高房价列表
plist = [201991, 130969, 129508, 119170, 115606, 79933, 77067, 72727, 56296, 55803, 53000, 51250, 49934, 46000, 43937, 33980]

c = (
    Line()      #创建折现图对象
    .add_xaxis(clist)                       #设置x轴数据
    .add_yaxis('最高房价',
               y_axis=plist,
               symbol='emptydiamond',       #设置标记图形：emptydiamond空心菱形，emptycircle空心圆形，circle实心圆形，emptyrect空心矩形，rect实心矩形，roundRect圆角矩形，triangle三角形
               is_symbol_show=True,         #设置是否显示标记图形
               label_opts=opts.LabelOpts(is_show=True),    #设置是否显示标签的数据
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5), color='rgba(77, 119, 255)')             #设置y轴数据；AreaStyleOpts设置面积图的风格；color设置颜色

    #设置图表
    .set_global_opts(
        title_opts= opts.TitleOpts(title = '北京各城区最高房价'),    #设置图标标题
        yaxis_opts= opts.AxisOpts(name='最高房价'),                 #设置y轴标题
        xaxis_opts= opts.AxisOpts(name='城区')                     #设置x轴标题
    )
    .render('./面积图2.html')                  #指定文件名，渲染图片
)

print('生成完成')