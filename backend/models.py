from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

# Association table for Career <-> Interest
career_interests = Table(
    "career_interests",
    Base.metadata,
    Column("career_id", String, ForeignKey("careers.id", ondelete="CASCADE"), primary_key=True),
    Column("interest_id", Integer, ForeignKey("interests.id", ondelete="CASCADE"), primary_key=True),
)

# Association table for Career <-> Exam
career_exams = Table(
    "career_exams",
    Base.metadata,
    Column("career_id", String, ForeignKey("careers.id", ondelete="CASCADE"), primary_key=True),
    Column("exam_id", String, ForeignKey("exams.id", ondelete="CASCADE"), primary_key=True),
)

# Association table for Career <-> College
career_colleges = Table(
    "career_colleges",
    Base.metadata,
    Column("career_id", String, ForeignKey("careers.id", ondelete="CASCADE"), primary_key=True),
    Column("college_id", Integer, ForeignKey("colleges.id", ondelete="CASCADE"), primary_key=True),
)

class Path(Base):
    __tablename__ = "paths"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    careers = relationship("Career", back_populates="path_obj")

class Interest(Base):
    __tablename__ = "interests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    careers = relationship("Career", secondary=career_interests, back_populates="interests")

class Exam(Base):
    __tablename__ = "exams"

    id = Column(String, primary_key=True, index=True) # e.g. "JEE-Main"
    title = Column(String, nullable=False)
    purpose = Column(Text)
    eligibility = Column(Text)
    timeline = Column(Text)

    careers = relationship("Career", secondary=career_exams, back_populates="exams")

class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False) # "India" or "Abroad"
    tier = Column(String, default="Top", nullable=False)
    website_url = Column(String, nullable=True)
    short_description = Column(Text, nullable=True)

    __table_args__ = (UniqueConstraint("name", "location", name="uix_name_location"),)

    careers = relationship("Career", secondary=career_colleges, back_populates="colleges")

class Career(Base):
    __tablename__ = "careers"

    id = Column(String, primary_key=True, index=True) # e.g. "data-scientist"
    title = Column(String, nullable=False)
    path_id = Column(Integer, ForeignKey("paths.id", ondelete="SET NULL"), nullable=True)
    
    # Career Information
    description = Column(Text)
    role_details = Column(Text)
    education_path = Column(Text)

    # Optional/legacy fields
    salary = Column(String, nullable=True)
    skills = Column(Text, nullable=True)
    salary_range = Column(String, nullable=True)
    growth_outlook = Column(String, nullable=True)

    path_obj = relationship("Path", back_populates="careers")
    interests = relationship("Interest", secondary=career_interests, back_populates="careers")
    exams = relationship("Exam", secondary=career_exams, back_populates="careers")
    colleges = relationship("College", secondary=career_colleges, back_populates="careers")