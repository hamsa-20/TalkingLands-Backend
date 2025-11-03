from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from geoalchemy2.shape import to_shape

router = APIRouter(prefix="/polygons", tags=["Polygons"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PolygonResponse)
def create_polygon(polygon: schemas.PolygonCreate, db: Session = Depends(get_db)):
    db_polygon = crud.create_polygon(db, polygon)
    geom = to_shape(db_polygon.area)
    return {"id": db_polygon.id, "name": db_polygon.name, "coordinates": list(geom.exterior.coords)}

@router.get("/", response_model=list[schemas.PolygonResponse])
def read_polygons(db: Session = Depends(get_db)):
    polygons = crud.get_polygons(db)
    result = []
    for poly in polygons:
        geom = to_shape(poly.area)
        result.append({"id": poly.id, "name": poly.name, "coordinates": list(geom.exterior.coords)})
    return result
