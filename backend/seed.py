import os
import json
from database import SessionLocal, engine, Base
import models

def validate_careers_data(data):
    if not isinstance(data, dict):
        raise ValueError("Root JSON must be an object/dict")
    
    allowed_root = {"careers", "exams"}
    unrecognized_root = set(data.keys()) - allowed_root
    if unrecognized_root:
        raise ValueError(f"Unrecognized root level keys: {unrecognized_root}")
        
    for idx, career in enumerate(data.get("careers", [])):
        # Allow keys starting with // (comments)
        keys = [k for k in career.keys() if not k.startswith("//")]
        required_career = {
            "id", "name", "path", "interest_tags", "short_description", 
            "about", "educational_roadmap", "entrance_exams", "salary_range", 
            "growth_outlook", "colleges"
        }
        missing = required_career - set(keys)
        extra = set(keys) - required_career
        if missing:
            raise ValueError(f"Career at index {idx} ({career.get('id')}) is missing required keys: {missing}")
        if extra:
            raise ValueError(f"Career at index {idx} ({career.get('id')}) has unrecognized keys: {extra}")
            
        if not isinstance(career["interest_tags"], list):
            raise ValueError(f"Career {career['id']} 'interest_tags' must be a list")
        if not isinstance(career["entrance_exams"], list):
            raise ValueError(f"Career {career['id']} 'entrance_exams' must be a list")
        if not isinstance(career["colleges"], list):
            raise ValueError(f"Career {career['id']} 'colleges' must be a list")
        if not isinstance(career["educational_roadmap"], list):
            raise ValueError(f"Career {career['id']} 'educational_roadmap' must be a list")
            
        for c_idx, college in enumerate(career["colleges"]):
            c_keys = [k for k in college.keys() if not k.startswith("//")]
            required_college = {"name", "location", "tier", "website_url", "short_description"}
            c_missing = required_college - set(c_keys)
            c_extra = set(c_keys) - required_college
            if c_missing:
                raise ValueError(f"College at index {c_idx} in career {career['id']} is missing keys: {c_missing}")
            if c_extra:
                raise ValueError(f"College at index {c_idx} in career {career['id']} has unrecognized keys: {c_extra}")
            if college["location"] not in ["India", "Abroad"]:
                raise ValueError(f"College {college['name']} in career {career['id']} has invalid location: {college['location']}")
            if college["tier"] not in ["Top", "Tier 2", "Tier 3"]:
                raise ValueError(f"College {college['name']} in career {career['id']} has invalid tier: {college['tier']}")

    for idx, exam in enumerate(data.get("exams", [])):
        e_keys = [k for k in exam.keys() if not k.startswith("//")]
        required_exam = {"id", "title", "purpose", "eligibility", "timeline"}
        e_missing = required_exam - set(e_keys)
        e_extra = set(e_keys) - required_exam
        if e_missing:
            raise ValueError(f"Exam at index {idx} ({exam.get('id')}) is missing keys: {e_missing}")
        if e_extra:
            raise ValueError(f"Exam at index {idx} ({exam.get('id')}) has unrecognized keys: {e_extra}")

def seed_db():
    # Drop and recreate tables to ensure fresh seed
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    json_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "data", "careers.json")
    if not os.path.exists(json_path):
        print(f"Error: careers.json not found at {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Validate JSON before seeding
    try:
        validate_careers_data(data)
        print("Data shape validation passed!")
    except Exception as e:
        print(f"Schema Validation Error: {e}")
        db.close()
        raise e

    # 1. Populate Paths
    path_map = {}
    for car in data.get("careers", []):
        p_name = car.get("path")
        if p_name and p_name not in path_map:
            path_obj = models.Path(name=p_name)
            db.add(path_obj)
            db.flush()
            path_map[p_name] = path_obj

    # 2. Populate Interests
    interest_map = {}
    for car in data.get("careers", []):
        for i_name in car.get("interest_tags", []):
            if i_name not in interest_map:
                interest = models.Interest(name=i_name)
                db.add(interest)
                db.flush()
                interest_map[i_name] = interest

    # 3. Populate Exams
    exam_map = {}
    for ex in data.get("exams", []):
        exam = models.Exam(
            id=ex["id"],
            title=ex["title"],
            purpose=ex.get("purpose"),
            eligibility=ex.get("eligibility"),
            timeline=ex.get("timeline")
        )
        db.add(exam)
        db.flush()
        exam_map[ex["id"]] = exam

    # 4. Populate Colleges
    college_map = {}
    for car in data.get("careers", []):
        for col in car.get("colleges", []):
            c_name = col["name"]
            c_loc = col["location"]
            key = (c_name, c_loc)
            if key not in college_map:
                college = models.College(
                    name=c_name,
                    location=c_loc,
                    tier=col.get("tier", "Top"),
                    website_url=col.get("website_url"),
                    short_description=col.get("short_description")
                )
                db.add(college)
                db.flush()
                college_map[key] = college

    # 5. Populate Careers and link relationships
    for car in data.get("careers", []):
        path_obj = path_map.get(car.get("path"))
        
        # Serialize the educational_roadmap list as a " || " separated string for DB storage
        roadmap_str = " || ".join(car.get("educational_roadmap", []))
        
        career = models.Career(
            id=car.get("id"),
            title=car.get("name"),
            path_obj=path_obj,
            description=car.get("short_description"),
            role_details=car.get("about"),
            education_path=roadmap_str,
            salary_range=car.get("salary_range"),
            growth_outlook=car.get("growth_outlook")
        )
        
        db.add(career)
        db.flush() # Ensure career has been added to session
        
        # Associate interests
        for i_name in car.get("interest_tags", []):
            interest = interest_map.get(i_name)
            if interest:
                career.interests.append(interest)
                
        # Associate exams
        for ex_id in car.get("entrance_exams", []):
            exam = exam_map.get(ex_id)
            if not exam:
                # Create exam inline if missing from base lists
                exam = models.Exam(id=ex_id, title=ex_id)
                db.add(exam)
                db.flush()
                exam_map[ex_id] = exam
            career.exams.append(exam)
                
        # Associate colleges
        for col in car.get("colleges", []):
            college = college_map.get((col["name"], col["location"]))
            if college:
                career.colleges.append(college)

    db.commit()
    db.close()
    print("Database seeded successfully from careers.json!")

if __name__ == "__main__":
    seed_db()