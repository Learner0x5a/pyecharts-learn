from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts .globals import ChartType, SymbolType, GeoType

# geo = Geo()
# geo.add_coordinate_json(json_file="country.json")
# geo.add_schema(maptype="world")
# geo.add("",[("Australia",128326),
# ("Brazil",44037),
# ("South Africa",7649),
# ("India",3562),
# ("Peru",2779),
# ("Iran",2698),
# ("Ukrainie",2040),
# ("Canada",1792),
# ("Mongolia",1514),
# ("Russia",1069),
# ("Mauritania",1374),
# ("Kazakhsan",701),
# ("Malaysia",554),
# ("New Zealand",422),
# ("Indonesia",148),
# ("Sweden",113),
# ("Mexico",121),
# ("Sierra Leone",109),
# ],type_=ChartType.SCATTER)
 
# geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=130000,type_='size',is_show=False),title_opts=opts.TitleOpts(title="mygeo")).set_colors(["#82318E"])
# geo.render("geo_world.html")

def geo_chart() -> Geo:
    c = (
        Geo()
        .add_coordinate_json(json_file="country.json")
        .add_schema(maptype="world")
        .add("",[("French",10),
                ("Canada",3),
                ("Singapore",1),
                ("China",6),
                ("South Africa",1),
                ("India",2),
                ("Israel",4),
                ("United States",12),
                ("Japan",4),
                ("South Korea",1),
                ("Australia",2),
                ("Malaysia",1),
                # ("New Zealand",422),
                # ("Indonesia",148),
                # ("Sweden",113),
                # ("Mexico",121),
                # ("Sierra Leone",109),
                ],type_=ChartType.SCATTER)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=12,type_='size',is_show=False)).set_colors(["#82318E"])
        .render("geo_world.html")
    )
    return c

geo_chart()