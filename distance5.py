from fastapi import FastAPI
from math import sqrt
from sqlalchemy import create_engine, Column, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DB_URL = "postgresql://postgres:1234@localhost:5432/dev3"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class Distance(Base):
    __tablename__ = "distances"

    id = Column(Float, primary_key=True)
    lat1 = Column(Float)
    lon1 = Column(Float)
    lat2 = Column(Float)
    lon2 = Column(Float)
    distance = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/distance")
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    # Calculate the distance between two points using the distance formula
    distance = sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    
    # Store the calculated distance in the database
    db = SessionLocal()
    new_distance = Distance(lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2, distance=distance)
    db.add(new_distance)
    db.commit()
    db.refresh(new_distance)
    
    return {"distance": distance}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
