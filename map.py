from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

# data = [['United States',1],['China',1],['Japan',4],['Korea',5],['France',1],['Germany',1],['Italy',1]]
# title_ = "办公建筑"

# data = [['United States',3],['France',1]]
# title_ = "厂房"

# data = [['China',1],['Japan',3],['Korea',3]]
# title_ = "餐厅"

# data = [['China',4],['United States',6],['Spain',1]]
# title_ = "监狱"

# data = [['China',4],['United States',1],['Japan',2],['France',1],['Spain',1]]
# title_ = "交通工具"

# data = [['United States',1],['France',1],['Korea',4]]
# title_ = "教堂"

# data = [['United States',2]]
# title_ = "旅馆"

# data = [['China',2],['Japan',9],['France',1],['Korea',3]]
# title_ = "其它（包含小剧场_展览馆_健身房等特殊类型场所）"

# data = [['China',1]]
# title_ = "商场"

# data = [['United States',2],['Korea',1]]
# title_ = "学校"

# data = [['United States',7],['Korea',1],['Japan',8],['Germany',3],['Spain',1]]
# title_ = "养老院"

data = [['United States',2],['Korea',2]]
title_ = "医院（非普通医院）"

c = (
    Map(init_opts=opts.InitOpts())
    .add("", data, "world",is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title=title_),
        legend_opts=opts.LegendOpts(is_show=False), 
        visualmap_opts=opts.VisualMapOpts(max_=5, is_piecewise=True,
                                      pieces=[
                                        {"max": 10, "min": 4, "label": ">5", "color": "#8A0808"},
                                        {"max": 4, "min": 3, "label": "4", "color": "#B40404"},
                                        {"max": 3, "min": 2, "label": "3", "color": "#DF0101"},
                                        {"max": 2, "min": 1, "label": "2", "color": "#F78181"},
                                        {"max": 1, "min": 0, "label": "1", "color": "#F5A9A9"},
                                        {"max": 0, "min": 0, "label": "0", "color": "#fababa"},
                                        ]),
    )
    .render("20201207/map_world"+title_+".html")
)


