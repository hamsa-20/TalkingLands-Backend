from shapely.geometry import Point, Polygon as ShapelyPolygon
from . import models

def create_polygon(db, polygon_data):
    polygon = ShapelyPolygon(polygon_data.coordinates)
    db_polygon = models.Polygon(name=polygon_data.name, geom=f'SRID=4326;{polygon.wkt}')
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return db_polygon

def create_point(db, point_data):
    point = Point(point_data.longitude, point_data.latitude)
    db_point = models.Point(name=point_data.name, geom=f'SRID=4326;{point.wkt}')
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def point_in_polygon(db, point_id, polygon_id):
    point = db.query(models.Point).filter(models.Point.id == point_id).first()
    polygon = db.query(models.Polygon).filter(models.Polygon.id == polygon_id).first()
    if not point or not polygon:
        return False
    query = f"SELECT ST_Within('{point.geom}'::geometry, '{polygon.geom}'::geometry);"
    return db.execute(query).scalar()
