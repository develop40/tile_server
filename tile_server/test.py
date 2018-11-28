import mapnik

m = mapnik.Map(256,256)
mapnik.load_map(m, 'style/styles.xml')
m.zoom_all()
mapnik.render_to_file(m,'altay.png', 'png')

# map = mapnik.Map(1024, 720)
# map.background = mapnik.Color('steelblue')
# style = mapnik.Style()
# rule = mapnik.Rule()
# polygon_symbolizer = mapnik.PolygonSymbolizer()
# polygon_symbolizer.fill = mapnik.Color('white')
# rule.symbols.append(polygon_symbolizer)
# line_symbolizer = mapnik.LineSymbolizer()
# line_symbolizer.stroke = mapnik.Color('black')
# line_symbolizer.stroke_width = 0.1
# rule.symbols.append(line_symbolizer)  # добавить символ в объект правила
# style.rules.append(rule)  # теперь добавить правило в стиль, и мы закончили
# map.append_style('My Style', style)
#
# ds = mapnik.PostGIS(host='127.0.0.1',
#                     dbname='isogd_sevastopol',
#                     user='postgres',
#                     password='qwerty12+',
#                     table='tableapi.land')
#
# layer = mapnik.Layer(' world ')
# layer.datasource = ds
# layer.styles.append('My Style')
# map.layers.append(layer)
# map.zoom_all()
# map.zoom(0.2)
# mapnik.render_to_file(map, 'world.png', 'png')
#
# z=0.5
# x=5452569.20254356
# y=5401501.80622266
#
#
# bbox = dict(minx=5452569.20254356, miny=3752079.55457865, maxx=5401501.80622266, maxy=3808263.31281919)
#
# step = max(bbox['maxx'] - bbox['minx'], bbox['maxy'] - bbox['miny']) / 2 ** z
#
# extents = dict()
#
# extents['tms'] = (
#     bbox['minx'] + x * step, bbox['miny'] + y * step,
#     bbox['minx'] + (x + 1) * step, bbox['miny'] + (y + 1) * step
# )
#
# extents['xyz'] = (
#     bbox['minx'] + x * step, bbox['maxy'] - (y + 1) * step,
#     bbox['minx'] + (x + 1) * step, bbox['maxy'] - y * step
# )
# box = mapnik.Box2d(*extents.get('xyz'))
# map.zoom_all()
# map.zoom_to_box(box)
# mapnik.render_to_file(map, 'world.png', 'png')
