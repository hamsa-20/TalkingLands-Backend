# 🗺️ Spatial API – TalkingLands Backend Assignment

This project is built as part of the **TalkingLands Backend Developer (Python)** assignment.  
It provides RESTful APIs using **FastAPI** to create polygons and points, and to check if a point lies inside a polygon.  
Spatial data is stored in **PostgreSQL** with **PostGIS** enabled.

---

## 🚀 Features

- ➕ **Add Polygon** — Create and store polygons with coordinates.  
- ➕ **Add Point** — Create and store latitude/longitude points.  
- 📍 **Point-in-Polygon Check** — Determine if a point lies inside a polygon.  
- 💾 **PostGIS Integration** — Spatial queries handled at database level.  
- ⚡ Built with **FastAPI**, **SQLAlchemy**, **GeoAlchemy2**, and **Shapely**.

---

## 🗂️ Project Structure

spatial_api/
│
├── app/
│ ├── init.py
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ └── routes/
│ ├── init.py
│ ├── points.py
│ └── polygons.py
│
├── .env
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd spatial_api
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # for Windows
# OR
source venv/bin/activate  # for Linux/Mac
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
🗄️ Database Setup (PostgreSQL + PostGIS)
1️⃣ Start PostgreSQL service
Make sure PostgreSQL is running:

bash
Copy code
net start postgresql-x64-18
2️⃣ Open psql and create DB
bash
Copy code
psql -U postgres
CREATE DATABASE spatialdb;
\c spatialdb
CREATE EXTENSION postgis;
3️⃣ Add connection string to .env
bash
Copy code
DATABASE_URL=postgresql://postgres:<your-password>@localhost/spatialdb
Replace <your-password> with your PostgreSQL password.

▶️ Running the Application
bash
Copy code
uvicorn app.main:app --reload
Open in browser:
👉 http://127.0.0.1:8000/docs

🧭 API Endpoints
➕ Create Polygon
POST /polygons/

json
Copy code
{
  "name": "Test Polygon",
  "coordinates": [
    [77.59, 12.97],
    [77.60, 12.97],
    [77.60, 12.98],
    [77.59, 12.98],
    [77.59, 12.97]
  ]
}
➕ Create Point
POST /points/

json
Copy code
{
  "name": "Point1",
  "latitude": 12.975,
  "longitude": 77.595
}
📍 Check if Point Lies Inside Polygon
GET /point-in-polygon/{point_id}/{polygon_id}

Example:

pgsql
Copy code
GET /point-in-polygon/1/1
Response:

json
Copy code
{
  "inside": true
}