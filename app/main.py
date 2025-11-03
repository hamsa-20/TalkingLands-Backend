from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spatial API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Spatial API running 🚀"}

@app.post("/polygon/")
def add_polygon(polygon: schemas.PolygonCreate, db: Session = Depends(get_db)):
    return crud.create_polygon(db, polygon)

@app.post("/point/")
def add_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    return crud.create_point(db, point)

@app.get("/point-in-polygon/{point_id}/{polygon_id}")
def check_point_inside(point_id: int, polygon_id: int, db: Session = Depends(get_db)):
    result = crud.point_in_polygon(db, point_id, polygon_id)
    return {"inside": result}
