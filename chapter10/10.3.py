# 3D柱状图
import random
from pyecharts import options as opts
from pyecharts.charts import Bar3D

# 生成测试数据
data = [[x, y, random.randint(10, 40)] for y in range(7) for x in range(24)]

hours = ['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm']
weeks = ['星期六','星期五','星期四','星期三','星期二','星期一','星期日']

c = (
    Bar3D(init_opts=opts.InitOpts(width='1200px', height='600px'))
        .add(
        '',
        data,
        xaxis3d_opts=opts.Axis3DOpts(name='小时', type_="category", data=hours),
        yaxis3d_opts=opts.Axis3DOpts(name='星期', type_="category", data=weeks),
        zaxis3d_opts=opts.Axis3DOpts(name='温度', type_="value"),
        # grid3d_opts=opts.Grid3DOpts(width=200, depth=80, rotate_speed=30),
        )
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=50, min_=0),
        title_opts=opts.TitleOpts(title='Q市7x24小时温度'),
        )
        .render('./3D柱状图2.html')
)
