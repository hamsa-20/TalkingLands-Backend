from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from geoalchemy2.shape import to_shape

router = APIRouter(prefix="/points", tags=["Points"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PointResponse)
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    db_point = crud.create_point(db, point)
    point_geom = to_shape(db_point.location)
    return {"id": db_point.id, "name": db_point.name, "latitude": point_geom.y, "longitude": point_geom.x}

@router.get("/", response_model=list[schemas.PointResponse])
def read_points(db: Session = Depends(get_db)):
    points = crud.get_points(db)
    result = []
    for p in points:
        geom = to_shape(p.location)
        result.append({"id": p.id, "name": p.name, "latitude": geom.y, "longitude": geom.x})
    return result
