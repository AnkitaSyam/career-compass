from pydantic import BaseModel, model_validator, ConfigDict
from typing import List, Optional

class PathSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class InterestSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class ExamSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    title: str
    purpose: str = ""
    eligibility: str = ""
    timeline: str = ""

    @model_validator(mode="before")
    @classmethod
    def serialize_relations(cls, data):
        if not hasattr(data, "id"):
            if isinstance(data, dict):
                return {
                    "id": data.get("id"),
                    "title": data.get("title"),
                    "purpose": data.get("purpose") or "",
                    "eligibility": data.get("eligibility") or "",
                    "timeline": data.get("timeline") or "",
                }
            return data

        return {
            "id": data.id,
            "title": data.title,
            "purpose": data.purpose or "",
            "eligibility": data.eligibility or "",
            "timeline": data.timeline or "",
        }

class CollegeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    location: str
    tier: str = "Top"
    website_url: Optional[str] = None
    short_description: Optional[str] = None
    paths: List[str] = []
    careers: List[str] = []

    @model_validator(mode="before")
    @classmethod
    def serialize_relations(cls, data):
        if not hasattr(data, "id"):
            return data
        
        # Get unique path names from associated careers
        paths_list = list(set(c.path_obj.name for c in data.careers if c.path_obj))
        careers_list = [c.title for c in data.careers]

        return {
            "id": data.id,
            "name": data.name,
            "location": data.location,
            "tier": data.tier,
            "website_url": data.website_url,
            "short_description": data.short_description,
            "paths": paths_list,
            "careers": careers_list,
        }

class CareerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    title: str
    path: str
    description: Optional[str] = None
    role_details: Optional[str] = None
    education_path: Optional[str] = None
    salary: Optional[str] = None
    skills: Optional[str] = None
    salary_range: Optional[str] = None
    growth_outlook: Optional[str] = None
    interests: List[str] = []
    exams: List[str] = []
    colleges_india: List[str] = []
    colleges_abroad: List[str] = []
    colleges: List[CollegeSchema] = []

    @model_validator(mode="before")
    @classmethod
    def serialize_relations(cls, data):
        if not hasattr(data, "id"):
            # If data is a dictionary already
            return data
        
        path_name = data.path_obj.name if data.path_obj else ""
        interests_list = [interest.name for interest in data.interests]
        exams_list = [exam.id for exam in data.exams]
        india_list = [c.name for c in data.colleges if c.location == "India"]
        abroad_list = [c.name for c in data.colleges if c.location == "Abroad"]
        colleges_list = [CollegeSchema.model_validate(c) for c in data.colleges]

        return {
            "id": data.id,
            "title": data.title,
            "path": path_name,
            "description": data.description,
            "role_details": data.role_details,
            "education_path": data.education_path,
            "salary": data.salary,
            "skills": data.skills,
            "salary_range": data.salary_range,
            "growth_outlook": data.growth_outlook,
            "interests": interests_list,
            "exams": exams_list,
            "colleges_india": india_list,
            "colleges_abroad": abroad_list,
            "colleges": colleges_list,
        }
