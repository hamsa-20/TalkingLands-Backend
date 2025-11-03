from pydantic import BaseModel

class PolygonCreate(BaseModel):
    name: str
    coordinates: list

class PointCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
