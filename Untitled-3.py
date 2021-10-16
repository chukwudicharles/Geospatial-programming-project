from pyproj import Geod

def geodesic_buffer(lon,lat,distance,segments):
    """Returns a Polygon Geometry,
    geodesic (WGS84) buffer from a pair of coordinates.

    lon --- X (GDA94) of a point
    lat --- Y (GDA94) of a point
    distance --- ellipsoidal distance for the buffer
    segments --- segments (each 90 degrees) of the polygon
    """
    g = Geod(ellps='GDA94') # geodesic object
    angle = 90 / segments # internal angles of the polygon
    coords = []
    for i in range(segments * 4 + 1):
        direct = g.fwd(lon,lat,i*angle,distance) #solve the Direct problem
        coords.append((direct[0],direct[1]))
    # create the polygon geometry from the coords list
    geo_buffer = QgsGeometry.fromPolygonXY([[QgsPointXY(pair[0],pair[1]) for pair in coords]])
    # print(geo_buffer.asWkt())
    return geo_buffer
        
layerName = "polygon BUILDING_POLYGON[EPSG:28354]"
input_id = 1
input_distance = 30000 # meters
layer = QgsProject().instance().mapLayersByName("layerName")[0]
feat = layer.getFeature(input_id)
geom = feat.geometry().centroid()
buff = geodesic_buffer(geom.asPoint().x(),geom.asPoint().y(),input_distance,5)
intersected_features_list=[]
for feature in layer.getFeatures():
    if feature.geometry().intersects(buff):
        intersected_features_list.append(str(feature.attributes()[0]))

print(intersected_features_list)