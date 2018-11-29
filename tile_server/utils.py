import pdb

import mapnik
import math


# # Размеры тайла
# TILE_WIDTH = 256
# TILE_HEIGHT = 256
#
# # Размеры карты
# BBOX_MINX = -20037508.0
# BBOX_MINY = -20037508.0
# BBOX_MAXX = 20037508.0
# BBOX_MAXY = 20037508.0
# # Каталог с xml-файлами с описаниями слоёв
# MAPNIK_CONFIGS = 'tile_server/style'
# # Каталог для хранения кэша тайлов
# CACHE_PATH = 'tile_server/tiles'

def tms(z, x, y, service, mapname):
    # (4370311.220000, 4911352.860000) - (4403732.650000, 4958349.910000)
    # Extent: (4370177.610000, 4908530.650000) - (4411390.670000, 4958581.500000)
    # (38.376357, 44.940402) - (48.804400, 51.182006)

    bbox = dict(minx=-180, miny=-90, maxx=180, maxy=90)
    BBOX_MAXX = 180
    BBOX_MINX = -180
    BBOX_MAXY = 90
    BBOX_MINY = -90
    stepx = (BBOX_MAXX - 1.0 - BBOX_MINX) / (2 ** z)
    stepy = (BBOX_MAXY - 1.0 - BBOX_MINY) / (2 ** z)

    step = max(bbox['maxx'] - bbox['minx'], bbox['maxy'] - bbox['miny']) / 2 ** z

    extents = dict()

    extents['tms'] = (
        bbox['minx'] + x * step,
        bbox['miny'] + y * step,
        bbox['minx'] + (x + 1) * step,
        bbox['miny'] + (y + 1) * step
    )

    extents['xyz'] = (
        bbox['minx'] + x * step,
        bbox['maxy'] - (y + 1) * step,
        bbox['minx'] + (x + 1) * step,
        bbox['maxy'] - y * step
    )

    tile = dict(width=256, height=256)
    map = mapnik.Map(tile['width'], tile['height'])
    map.background = mapnik.Color('transparent')
    # mapnik.load_map(map, 'tile_server/style/mrsk.xml')

    style = mapnik.Style()
    rule = mapnik.Rule()
    # polygon_symbolizer = mapnik.PolygonSymbolizer()
    # polygon_symbolizer.fill = mapnik.Color('white')
    # rule.symbols.append(polygon_symbolizer)

    point_symbolizer= mapnik.PointSymbolizer()
    rule.symbols.append(point_symbolizer)

    line_symbolizer = mapnik.LineSymbolizer()
    line_symbolizer.stroke = mapnik.Color('red')
    line_symbolizer.stroke_width = 1
    rule.symbols.append(line_symbolizer)  # добавить символ в объект правила
    style.rules.append(rule)  # теперь добавить правило в стиль, и мы закончили
    map.append_style('My Style', style)

    layer = mapnik.Layer(mapname)
    ds = mapnik.PostGIS(host='127.0.0.1',
                        dbname='mrsk',
                        user='postgres',
                        password='qwerty12+',
                        table=mapname)
    layer.datasource = ds
    layer.styles.append('My Style')
    map.layers.append(layer)




    # layer = mapnik.Layer('point')
    # ds = mapnik.PostGIS(host='127.0.0.1',
    #                     dbname='isogd_sevastopol',
    #                     user='postgres',
    #                     password='qwerty12+',
    #                     table='tableapi.table_test_2_points_2')
    # layer.datasource= ds
    # # pdb.set_trace()
    # style= mapnik.Style()
    # rule = mapnik.Rule()
    # point_symbolizer = mapnik.PointSymbolizer()
    # point_symbolizer.file= "/style/point_style.png"
    # # pdb.set_trace()
    #
    # rule.symbols.append(point_symbolizer)
    # style.rules.append(rule)
    # map.append_style('My Style', style)

    # map.zoom_all()
    # mapnik.render_to_file(map, 'altay.png', 'png')
    # pdb.set_trace()
    box = mapnik.Box2d(*extents.get(service))

    # map.zoom_all()
    mapnik.load_map(map, 'tile_server/style/mrsk.xml')
    map.zoom_to_box(box)
    # mapnik.render_to_file(map, '{0}{1}{2}.png'.format(x,y,z), 'png')
    im = mapnik.Image(map.width, map.height)
    # pdb.set_trace()
    mapnik.render_layer(map, im, layer=2)
    output = im.tostring('png')
    # box = mapnik.Box2d(*extents.get(service))
    # map.zoom_to_box(box)
    # mapnik.render_to_file(map, 'world.png', 'png')
    # im = mapnik.Image(map.width, map.height)
    # mapnik.render(map, im)
    # output = im.tostring('png')
    # # Передаём ответ клиенту
    return output
