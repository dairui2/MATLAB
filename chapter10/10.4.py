# 堆叠面积图展示近10年全国总人口的变化情况(由于5个指标都是类似的，所以可以用堆叠面积图展示)
# 从excel文件中读取数据

import xlwings as xw
from pyecharts import options as opts
from pyecharts.charts import Line

app = xw.App(visible=True, add_book=False)
f=r'./全国总人口10年数据.xlsx'

wb = app.books.open(f)
# 获取活动的工作表
sheet1 = wb.sheets.active

# 获取表格数据区域
rng = sheet1.range('A3:K8')

# 获取表格数据区域的数据
data = rng.value

# 列标题
x_data = data[0][1:]        #获取表格中列标题，作为图表的x轴数据

# 关闭工作簿对象
wb.close()

# 退出excel应用程序
app.quit()

(
    Line()
    .add_xaxis(xaxis_data=x_data)       #添加一组y轴数据
    .add_yaxis(
        series_name='年末人口总数',
        stack='总量',                     #对stack设置相同的组名，就会进行堆叠
        y_axis=data[1][1:],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),     #设置为面积
        label_opts=opts.LabelOpts(is_show=False)
    )

    .add_yaxis(
        series_name='男性人口',
        stack='总量',
        y_axis=data[2][1:],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name='女性人口',
        stack='总量',
        y_axis=data[3][1:],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name = '城镇人口',
        stack = '总量',
        y_axis = data[4][1:],
        areastyle_opts = opts.AreaStyleOpts(opacity=0.5),
        label_opts = opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name='乡村人口',
        stack='总量',
        y_axis=data[5][1:],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=True, position='top')
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title='10年全国总人口变化'),
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        xaxis_opts=opts.AxisOpts()
    )
    .render('./堆叠面积图.html')
)

print('生成完成')