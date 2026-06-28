from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas
import crud

# Ensure tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CareerCompass Backend")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_no_cache_headers(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "CareerCompass Backend Running"}

@app.get("/careers", response_model=List[schemas.CareerSchema])
def get_careers(db: Session = Depends(get_db)):
    return crud.get_careers(db)

@app.get("/career/{id}", response_model=schemas.CareerSchema)
def get_career(id: str, db: Session = Depends(get_db)):
    career = crud.get_career_by_id(db, id)
    if not career:
        raise HTTPException(status_code=404, detail="Career not found")
    return career

@app.get("/search")
def search(keyword: str = Query(...), db: Session = Depends(get_db)):
    results = crud.search_all(db, keyword)
    return {
        "careers": [schemas.CareerSchema.model_validate(c) for c in results["careers"]],
        "exams": [schemas.ExamSchema.model_validate(e) for e in results["exams"]],
        "colleges": [schemas.CollegeSchema.model_validate(c) for c in results["colleges"]]
    }

@app.get("/paths", response_model=List[schemas.PathSchema])
def get_paths(db: Session = Depends(get_db)):
    return crud.get_paths(db)

@app.get("/interests", response_model=List[schemas.InterestSchema])
def get_interests(db: Session = Depends(get_db)):
    return crud.get_interests(db)

@app.get("/exams", response_model=List[schemas.ExamSchema])
def get_exams(db: Session = Depends(get_db)):
    return crud.get_exams(db)

@app.get("/exam/{id}", response_model=schemas.ExamSchema)
def get_exam(id: str, db: Session = Depends(get_db)):
    exam = crud.get_exam_by_id(db, id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam

@app.get("/colleges", response_model=List[schemas.CollegeSchema])
def get_colleges(db: Session = Depends(get_db)):
    return crud.get_colleges(db)

@app.get("/college/{id}", response_model=schemas.CollegeSchema)
def get_college(id: int, db: Session = Depends(get_db)):
    college = crud.get_college_by_id(db, id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college

@app.get("/careers/by-path/{path}", response_model=List[schemas.CareerSchema])
def get_careers_by_path(path: str, db: Session = Depends(get_db)):
    return crud.get_careers_by_path(db, path)

@app.get("/careers/by-interest/{interest}", response_model=List[schemas.CareerSchema])
def get_careers_by_interest(interest: str, db: Session = Depends(get_db)):
    return crud.get_careers_by_interest(db, interest)