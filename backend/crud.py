from sqlalchemy.orm import Session
from sqlalchemy import or_
import models

def get_careers(db: Session):
    return db.query(models.Career).all()

def get_career_by_id(db: Session, career_id: str):
    return db.query(models.Career).filter(models.Career.id == career_id).first()

def get_careers_by_path(db: Session, path_name: str):
    return db.query(models.Career).join(models.Path).filter(models.Path.name.ilike(path_name)).all()

def get_careers_by_interest(db: Session, interest_name: str):
    return db.query(models.Career).join(models.Career.interests).filter(models.Interest.name.ilike(interest_name)).all()

def get_paths(db: Session):
    return db.query(models.Path).all()

def get_interests(db: Session):
    return db.query(models.Interest).all()

def get_exams(db: Session):
    return db.query(models.Exam).all()

def get_exam_by_id(db: Session, exam_id: str):
    return db.query(models.Exam).filter(models.Exam.id == exam_id).first()

def get_colleges(db: Session):
    return db.query(models.College).all()

def get_college_by_id(db: Session, college_id: int):
    return db.query(models.College).filter(models.College.id == college_id).first()

def search_all(db: Session, keyword: str):
    careers = db.query(models.Career).filter(
        or_(
            models.Career.title.ilike(f"%{keyword}%"),
            models.Career.description.ilike(f"%{keyword}%"),
            models.Career.role_details.ilike(f"%{keyword}%")
        )
    ).all()

    exams = db.query(models.Exam).filter(
        or_(
            models.Exam.title.ilike(f"%{keyword}%"),
            models.Exam.purpose.ilike(f"%{keyword}%"),
            models.Exam.eligibility.ilike(f"%{keyword}%")
        )
    ).all()

    colleges = db.query(models.College).filter(
        models.College.name.ilike(f"%{keyword}%")
    ).all()

    return {
        "careers": careers,
        "exams": exams,
        "colleges": colleges
    }
