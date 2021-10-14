def lineLengthCalc(layer,self):
    """Sums together the length of features in a line type vector layer, then prints the result in km."""
    # get the current active layer
    #layer = iface.activeLayer()

    total_length = 0
  #looping thrugh the layer to get the geometry and layer features.
    for feat in layer.getFeatures():
        geometry = feat.geometry()
        total_length += geometry.length()
    output_file = open('c:\qgis.txt', 'w')
    for f in layer.getFeatures():
        geom = f.geometry()
        line = '%s, %s, %f, %f\n' % (f['name'], f['iata_code'],
              geom.asPoint().y(), geom.asPoint().x())
        unicode_line = line.encode('utf-8')
        output_file.write(unicode_line)
    output_file.close()
    # print out the result
    print("Total length of features in layer "+ layer.sourceName()+ " is:",
          round(total_length/1000, 1), "km")
    V = QgsDistanceArea()
    V.setEllipsoid('WGS84')
    point2 = QgsPointXY(geom.asPoint().y(), geom.asPoint().x())
    if(point <30):
        print("high obese area")
    else:
         print("Non exist")





layer = iface.activeLayer()

feats = [ feat for feat in layer.getFeatures() ]

epsg = layer.crs().postgisSrid()

uri = "Polygon?crs=epsg:" + str(epsg) + "&field=id:integer""&index=yes"

mem_layer = QgsVectorLayer(uri,
                           'square_buffer',
                           'memory')

prov = mem_layer.dataProvider()
#30 km centroid buffer
for i, feat in enumerate(feats):
    new_feat = QgsFeature()
    new_feat.setAttributes([i])
    tmp_feat = feat.geometry().buffer(30, -1).boundingBox().asWktPolygon()
    new_feat.setGeometry(QgsGeometry.fromWkt(tmp_feat))
    prov.addFeatures([new_feat])

QgsProject.instance().addMapLayer(mem_layer)
lineLengthCalc(layer)


