# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.faker import Faker

# c = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("geo", [list(z) for z in zip(Faker.country, Faker.values())])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#     .render("geo_base.html")
# )
# print([list(z) for z in zip(Faker.provinces, Faker.values())])

# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.faker import Faker
# from pyecharts.globals import ChartType

# c = (
#     Geo()
#     .add_schema(maptype="china")
#     .add(
#         "geo",
#         [list(z) for z in zip(Faker.provinces, Faker.values())],
#         type_=ChartType.EFFECT_SCATTER,
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"))
#     .render("geo_effectscatter.html")
# )

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts .globals import ChartType, SymbolType, GeoType
geo = Geo()
 
# # 新增坐标点，添加名称跟经纬度
# geo.add_coordinate(name="China",longitude=104.195,latitude=35.675)
# geo.add_coordinate(name="Australia",longitude=133.775,latitude=-25.274)
# geo.add_coordinate(name="Brazil",longitude=-51.925,latitude=-14.235)
# geo.add_coordinate(name="South Africa",longitude=22.937,latitude=-30.559)
# geo.add_coordinate(name="India",longitude=78.962,latitude=20.593)
# geo.add_coordinate(name="Peru",longitude=-75.015,latitude=-9.189)
# geo.add_coordinate(name="Iran",longitude=53.688,latitude=32.427)
# geo.add_coordinate(name="Ukraine",longitude=31.165,latitude=48.379)
# geo.add_coordinate(name="Canada",longitude=-106.346,latitude=56.130)
# geo.add_coordinate(name="Mongolia",longitude=103.847,latitude=46.862)
# geo.add_coordinate(name="Russia",longitude=37.618,latitude=55.751)
# geo.add_coordinate(name="Mauritania",longitude=21.008,latitude=-10.941)
# geo.add_coordinate(name="Kazakhstan",longitude=66.924,latitude=48.019)
# geo.add_coordinate(name="UAE",longitude=53.848,latitude=23.424)
# geo.add_coordinate(name="Malaysia",longitude=101.976,latitude=4.210)
# geo.add_coordinate(name="New Zealand",longitude=174.886,latitude=-40.900)
# geo.add_coordinate(name="Indonesia",longitude=113.921,latitude=-0.789)
# geo.add_coordinate(name="Sweden",longitude=18.643,latitude=60.128)
# geo.add_coordinate(name="Mexico",longitude=-102.553,latitude=23.634)
# geo.add_coordinate(name="Sierra Leone",longitude=-11.779,latitude=8.461)
geo.add_coordinate_json(json_file="country.json")
 
# 添加数据项
geo.add_schema(maptype="world")
geo.add("",[("Australia",128326),
("Brazil",44037),
("South Africa",7649),
("India",3562),
("Peru",2779),
("Iran",2698),
("Ukrainie",2040),
("Canada",1792),
("Mongolia",1514),
("Russia",1069),
("Mauritania",1374),
("Kazakhsan",701),
# ("UAE",490),
("Malaysia",554),
("New Zealand",422),
("Indonesia",148),
("Sweden",113),
("Mexico",121),
("Sierra Leone",109),
],type_=ChartType.EFFECT_SCATTER)
 
# # 绘制流向
# geo.add("流向图",[
# ("Australia","China"),
# ("Brazil","China"),
# ("South Africa","China"),
# ("India","China"),
# ("Peru","China"),
# ("Iran","China"),
# ("Ukraine","China"),
# ("Canada","China"),
# ("Mongolia","China"),
# ("Russia","China"),
# ("Mauritania","China"),
# ("Kazakhstan","China"),
# # ("UAE","China"),
# ("Malaysia","China"),
# ("New Zealand","China"),
# ("Indonesia","China"),
# ("Sweden","China"),
# ("Mexico","China"),
# ("Sierra Leone","China"),
# ],
# type_= GeoType.LINES,
# effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,symbol_size=5,color="#82318E"),
# linestyle_opts=opts.LineStyleOpts(curve=0.2),
# )
 
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=130000,type_='size',is_show=False),title_opts=opts.TitleOpts(title="mygeo")).set_colors(["#82318E"])
geo.render("geo_world.html")