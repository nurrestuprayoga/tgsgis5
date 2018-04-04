import mapnik
m = mapnik.Map(2400,1800)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FCEA29')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 20.0

r.symbols.append(line_symbolizer)
basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'),'DejaVu Sans Bold',2,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius=2
r.symbols.append(basinsLabels)

point_sym=mapnik.PointSymbolizer()
point_sym.allow_overlap=True
r.symbols.append(point_sym)

s.rules.append(r)

highlight=mapnik.PolygonSymbolizer()
highlight.fill=mapnik.Color('red')
germany=mapnik.Rule()
germany.filter=mapnik.Expression("[NAME]='Germany'")
germany.symbols.append(highlight)
s.rules.append(germany)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:/gis4/SHP_Country/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)


s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="D:/gis4/New folder/IND_PNT_polyline.shp")
layer = mapnik.Layer('pantai')
layer.datasource = ds 
layer.styles.append('My Style2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="D:/gis4/ne_50m_geography_regions_polys/ne_50m_geography_regions_polys.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds 
layer.styles.append('My Style3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="D:/gis4/ne_50m_geography_marine_polys/ne_50m_geography_marine_polys.shp")
layer = mapnik.Layer('laut')
layer.datasource = ds 
layer.styles.append('My Style4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="D:/gis4/ne_50m_admin_0_countries_lakes/ne_50m_admin_0_countries_lakes.shp")
layer = mapnik.Layer('sungai')
layer.datasource = ds 
layer.styles.append('My Style5')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style6',s)
ds = mapnik.Shapefile(file="D:/gis4/New folder/IND_PNT_rectangle.shp")
layer = mapnik.Layer('kota')
layer.datasource = ds 
layer.styles.append('My Style6')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'pt5.png', 'png')
print "rendered image to 'pt5.png'"
