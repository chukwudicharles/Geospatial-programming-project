#set up the file part
filepath = "C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT"
educationFileName = "C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/FOI_POINT.shp"
recreationalFileName = "C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/FOI_POLYGON.shp"
buildingFileName = "C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/BUILDING_POLYGON.shp"
#load the layers
recreationalLayer = iface.addVectorLayer("C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/FOI_POLYGON.shp", "polygon", "ogr")
educationLayer = iface.addVectorLayer("C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/FOI_POINT.shp", "points", "ogr")
buildingLayer = iface.addVectorLayer("C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/BUILDING_POLYGON.shp", "polygon", "ogr")
#buffer building layer
layerName = "polygon BUILDING_POLYGON[EPSG:28354]"
outFile = "C:/Users/User1/Downloads/doncaster/mga94_54/shape/locality_polygon/doncaster-3000/VMFEAT/BUILDING_POLYGON/buffer.shp"

bufDist = 30 # in kilometers
layers = QgsProject.instance().mapLayersByName(layerName)
layer = layers[0]
fields = "layer".fields()
feats = "layer".getFeatures()

writer = QgsVectorFileWriter(outFile, \
'UTF-8', \
"fields", \
QgsWkbTypes.Polygon, \
"layer".sourceCrs(), \
"ESRI Shapefile")

for feat in feats:
    geom = feat.geometry()
    buffer = geom.buffer(bufDist, 5)
    feat.setGeometry(buffer)
    writer.addFeature(feat)
    print('done')
    iface.addVectorLayer(outFile, '', 'ogr')
    del(writer)
#calculating proximity and checking for obese area, for education centre
from qgis.core import QgsDistanceArea
pointFOI_POINT = (752772.1077763591893017,5757459.2470082668587565)
polygonBUILDING_POLYGON = (858795.8939945478923619,5805223.0258914902806282)
d = QgsDistanceArea()
d.setEllipsoid("GDA94")
X1, Y1 = pointFOI_POINT
X2, Y2 = polygonBUILDING_POLYGON
point1 = QgsPointXY(X1, Y1)
point2 = QgsPointXY(X2, Y2)
distance = d.measureLine([point1, point2])
print(distance/1000)
for n in distanceToPolygon:
    if n < 30:
        distance = "high obese"
    elif n > 30:
        distance = "low obese"
    elif n == 30:
        distance = "predictable"
    else:
        distance = "unpredictable"
    print(distance)
#calculating proximity and checking for obese area, for recreational centre
from qgis.core import QgsDistanceArea
polygonFOI_POLYGON = (857853.7053976962342858,5804951.3267816836014390)
polygonBUILDING_POLYGON = (858795.8939945478923619,5805223.0258914902806282)
d = QgsDistanceArea()
d.setEllipsoid("GDA94")
X1, Y1 = polygonFOI_POLYGON
X2, Y2 = polygonBUILDING_POLYGON
point1 = QgsPointXY(X1, Y1)
point2 = QgsPointXY(X2, Y2)
distance1 = d.measureLine([point1, point2])
print(distance1/1000)
for n in distance1:
    if n < 30:
        distance1 = "low obese"
    elif n > 30:
        distance1 = "high obese"
    elif n == 30:
        distance1 = "predictable"
    else:
        distance1 = "unpredictable"
    print(distance1)
    
                       

    
    

    

    