#环状图

from pyecharts import options as opts
from pyecharts.charts import Pie

# 各种活动项目的标题列表
actives = ['工作','睡觉','吃饭','玩耍']

# 各种活动项目所占时间的列表
slices = [8, 7, 3, 6]

# 打包由元组构成的列表
actives_slices_zip = zip(actives, slices)       #通过zip函数将两个列表打包成由元组构成的列表

# 通过列表推导式返回列表的列表
data_pair = [list(z) for z in actives_slices_zip]   #通过列表推导式重构列表对象data_pair, data_pair是一个列表对象，其中的元素又是一个列表，即列表的列表，也就是二维列表
c = (
    Pie()   #创建饼图对象
    .add(series_name='我一天的活动', data_pair=data_pair,
         radius=['30%','70%'])    #series_name='' 设置系列，data_pair='' 设置列名; radius属性可以将饼图改成环状图，30%是内环占用半径的比例，70%是外环占用半径的比例
    .set_global_opts(title_opts=opts.TitleOpts(title='饼状图'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {c}'))   #设置系列标签显示格式，参数b获取系列名，即actives列表的内容。参数c获取系列数值，即slices列表的内容
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            formatter='{a} <br/>{b}: {c} ({d}%)'                        #设置系列提示框的显示格式，参数b和c同上。参数d表示该系列所占的百分比
        )
    )
    .render('./环状图.html')
)

print('生成完成')