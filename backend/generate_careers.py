# -*- coding: utf-8 -*-
import json
import os

def generate_careers_json():
    exams = [
        {"id": "JEE-Main", "title": "JEE Main", "purpose": "Engineering (B.E./B.Tech) admissions in premier government institutes like NITs, IIITs, and CFTIs, and qualifying for JEE Advanced.", "eligibility": "Class 12 pass with Physics, Chemistry, and Mathematics as core subjects.", "timeline": "Conducted in January and April 2026 (Over)"},
        {"id": "NEET", "title": "NEET UG (National Eligibility cum Entrance Test)", "purpose": "Admissions to undergraduate medical (MBBS, BDS, AYUSH) and veterinary courses across India.", "eligibility": "Class 12 pass with Physics, Chemistry, and Biology/Biotechnology.", "timeline": "Conducted in May 2026 (Over)"},
        {"id": "CLAT", "title": "CLAT (Common Law Admission Test)", "purpose": "Admission to 5-year integrated undergraduate law programs (BA-LLB, BBA-LLB) at 24 National Law Universities (NLUs) in India.", "eligibility": "Class 12 pass (minimum 45% marks; 40% for SC/ST). No age limit.", "timeline": "Conducted in December 2025 (Over) / Next: December 2026 (Upcoming)"},
        {"id": "UCEED", "title": "UCEED (Undergraduate Common Entrance Examination for Design)", "purpose": "Admission to Bachelor of Design (B.Des) programs at IIT Bombay, IIT Delhi, IIT Guwahati, IIT Hyderabad, and IIITDM Jabalpur.", "eligibility": "Open to all streams (Science, Commerce, Humanities). Must have passed Class 12.", "timeline": "Conducted in January 2026 (Over)"},
        {"id": "NID-DAT", "title": "NID DAT (Design Aptitude Test)", "purpose": "Admission to undergraduate B.Des courses at National Institute of Design (NID) campuses across India.", "eligibility": "Class 12 pass in any stream (Science, Commerce, Humanities). Age limit applies (usually under 20).", "timeline": "Prelims: December 2025, Mains: April/May 2026 (Over)"},
        {"id": "NCHMCT-JEE", "title": "NCHMCT JEE", "purpose": "Admission to B.Sc. Hospitality and Hotel Administration programs across central and state IHMs (Institutes of Hotel Management).", "eligibility": "Class 12 pass in any stream, with English as a compulsory subject.", "timeline": "Conducted in May 2026 (Over)"},
        {"id": "ACET", "title": "ACET (Actuarial Common Entrance Test)", "purpose": "Entry exam to gain membership to the Institute of Actuaries of India (IAI) to begin taking actuarial professional papers.", "eligibility": "Class 12 pass with English and Mathematics as major subjects.", "timeline": "Conducted in March and June 2026 (Over) / Next: December 2026 (Upcoming)"},
        {"id": "IPMAT", "title": "IPMAT (Integrated Program in Management Aptitude Test)", "purpose": "Admission to the prestigious 5-year Integrated Program in Management (BBA+MBA) at IIM Indore, IIM Rohtak, and other partner institutes.", "eligibility": "Class 12 pass in any stream (minimum 60% aggregate; 55% for SC/ST).", "timeline": "Conducted in May 2026 (Over)"},
        {"id": "CUET-UG", "title": "CUET UG (Common University Entrance Test)", "purpose": "Admission to undergraduate programs in all Central Universities (like Delhi University, JNU, BHU) and participating state/private colleges.", "eligibility": "Class 12 pass. Subject combinations depend on the chosen university course requirements.", "timeline": "Conducted in May 2026 (Over)"},
        {"id": "SAT", "title": "SAT (Scholastic Assessment Test)", "purpose": "Standardized test for undergraduate admissions to colleges in the USA, Canada, UK, and a growing list of premium Indian private universities.", "eligibility": "No specific eligibility criteria; open to high school students.", "timeline": "Conducted multiple times a year: March, May, June 2026 (Over) / Next: August, October, November, December 2026 (Upcoming)"},
        {"id": "IELTS", "title": "IELTS (International English Language Testing System)", "purpose": "Measures English language proficiency for study, migration, or work abroad in English-speaking nations.", "eligibility": "Generally recommended for candidates aged 16 and above.", "timeline": "Conducted multiple times a month throughout the year (Upcoming/Ongoing)"},
        {"id": "NATA", "title": "NATA (National Aptitude Test in Architecture)", "purpose": "Admission to 5-year Bachelor of Architecture (B.Arch) courses in colleges across India.", "eligibility": "Class 12 pass with Physics, Chemistry, and Mathematics, or 10+3 Diploma with Mathematics.", "timeline": "Conducted in weekly phases from April to July 2026 (Ongoing/Over)"},
        {"id": "UPSC-CSE", "title": "UPSC Civil Services Examination", "purpose": "Recruitment to prestigious Indian civil services including IAS, IFS, IPS, and IRS.", "eligibility": "Graduation degree in any stream. Minimum age of 21 years.", "timeline": "Prelims: May 31, 2026 (Over) / Mains: September 2026 (Upcoming)"},
        {"id": "ISI-Admission-Test", "title": "ISI Admission Test", "purpose": "Admission to Bachelor of Statistics (B.Stat Hons) and Bachelor of Mathematics (B.Math Hons) programs at ISI Kolkata and Bengaluru.", "eligibility": "Class 12 pass with Mathematics and English.", "timeline": "Conducted in May 2026 (Over)"},
        {"id": "BITSAT", "title": "BITSAT", "purpose": "Admission to integrated first-degree programs (B.E., B.Pharm, M.Sc.) at BITS Pilani, Goa, and Hyderabad campuses.", "eligibility": "Class 12 pass with Physics, Chemistry, and Mathematics/Biology, and English with minimum 75% marks in PCM/B.", "timeline": "Session 1: April 2026, Session 2: May 2026 (Over)"},
        {"id": "IIST-Admission", "title": "IIST Admission", "purpose": "Admission to B.Tech (Aerospace and Avionics) programs at Indian Institute of Space Science and Technology (IIST).", "eligibility": "Class 12 pass with Physics, Chemistry, and Mathematics, plus qualifying in JEE Advanced.", "timeline": "Registrations closed in June 2026 (Over)"},
        {"id": "ICAR-AIEEA", "title": "ICAR AIEEA", "purpose": "Admission to Bachelor degree programs in Agriculture and Allied Sciences at State Agricultural Universities.", "eligibility": "Class 12 pass with Physics, Chemistry, and Biology/Mathematics/Agriculture.", "timeline": "Conducted via CUET-UG in May 2026 (Over)"},
        {"id": "CUET-PG", "title": "CUET PG", "purpose": "Admission to Postgraduate programs (including Clinical Psychology) in Central and participating Universities.", "eligibility": "Bachelor's degree in the relevant subject/discipline.", "timeline": "Conducted in March 2026 (Over)"},
        {"id": "CAT", "title": "CAT (Common Admission Test)", "purpose": "Admission to MBA/PGP programs at Indian Institutes of Management (IIMs) and top business schools.", "eligibility": "Bachelor's degree with at least 50% marks (45% for SC/ST/PwD).", "timeline": "Scheduled for November 29, 2026 (Upcoming)"},
        {"id": "AILET", "title": "AILET (All India Law Entrance Test)", "purpose": "Admission to BA LLB (Hons) and LLM programs at NLU Delhi.", "eligibility": "Class 12 pass (minimum 45% marks) or appearing.", "timeline": "Conducted in December 2025 (Over) / Next: December 2026 (Upcoming)"},
        {"id": "LSAT-India", "title": "LSAT India", "purpose": "Admission to integrated law programs at participating Indian private universities.", "eligibility": "Class 12 pass in any stream.", "timeline": "Conducted in January and May 2026 (Over)"},
        {"id": "LSAT", "title": "LSAT (Law School Admission Test - International)", "purpose": "Admission to law schools in USA, Canada, and select other countries.", "eligibility": "Bachelor's degree or high school graduate (varies by program).", "timeline": "Conducted multiple times a year (Upcoming)"},
        {"id": "NIFT", "title": "NIFT Entrance Exam", "purpose": "Admission to design (B.Des, B.FTech) and management programs at National Institute of Fashion Technology.", "eligibility": "Class 12 pass in any stream (for B.Des) or with PCM (for B.FTech).", "timeline": "Conducted in February 2026 (Over)"},
        {"id": "NDA-Exam", "title": "NDA (National Defence Academy) Entrance Exam", "purpose": "Admission to the Army, Navy, and Air Force wings of the NDA and Indian Naval Academy Course.", "eligibility": "Class 12 pass in any stream (for Army) or with Physics and Mathematics (for Navy and Air Force). Unmarried male/female candidates.", "timeline": "Conducted twice a year (NDA I in April, NDA II in September)."},
        {"id": "IGRUA-Entrance", "title": "IGRUA Commercial Pilot License (CPL) Entrance Exam", "purpose": "Admission to the Ab-initio Commercial Pilot License (CPL) training course at IGRUA.", "eligibility": "Class 12 pass with English, Physics, and Mathematics (minimum 50-55% aggregate). Minimum age 17.", "timeline": "Conducted in May/June annually."},
    ]

    def build_colleges(career_name, path_name):
        return [
            {
                "name": f"Indian Institute of {career_name} (Example Top)",
                "location": "India",
                "tier": "Top",
                "website_url": "https://www.example.edu/",
                "short_description": f"Premier national institute for training and advanced research in {career_name}."
            },
            {
                "name": f"National Academy of {career_name} (Example Tier 2)",
                "location": "India",
                "tier": "Tier 2",
                "website_url": "https://www.example-academy.edu.in/",
                "short_description": "Highly respected institute offering vocational and undergraduate courses."
            },
            {
                "name": f"Global School of {career_name} (Example Abroad)",
                "location": "Abroad",
                "tier": "Top",
                "website_url": "https://www.example-abroad.edu/",
                "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements."
            }
        ]

    raw_paths_careers = {
    "Computer Science & Technology": [
        {
            "id": "software-engineer-developer",
            "name": "Software Engineer/Developer",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Professional role working in the field of Software Engineer/Developer to design, implement, or manage solutions.",
            "about": "A Software Engineer/Developer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Software Engineer/Developer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "frontend-developer",
            "name": "Frontend Developer",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Professional role working in the field of Frontend Developer to design, implement, or manage solutions.",
            "about": "A Frontend Developer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Frontend Developer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "backend-developer",
            "name": "Backend Developer",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Professional role working in the field of Backend Developer to design, implement, or manage solutions.",
            "about": "A Backend Developer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Backend Developer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "full-stack-developer",
            "name": "Full-Stack Developer",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Develops both frontend user interfaces and backend database engines for websites.",
            "about": "Full-Stack Developers manage client-side UI code (HTML/CSS/JS) and server-side logic and database queries. You will build user accounts, connect APIs, and optimize web app speeds.",
            "educational_roadmap": [
                "Class 12 in any stream (Science/Commerce preferred).",
                "B.Tech in CS/IT, BCA, or B.Sc. in Computer Science (3-4 years).",
                "Assemble a Github portfolio showcasing working web applications.",
                "Join tech startups or take on international freelance contracts."
            ],
            "entrance_exams": [
                "JEE-Main",
                "CUET-UG"
            ],
            "salary_range": "₹4–12 LPA",
            "growth_outlook": "High growth, high freelance flexibility",
            "colleges": [
                {
                    "name": "Indian Institute of Full-Stack Web Developer (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Full-Stack Web Developer.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Full-Stack Web Developer (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Full-Stack Web Developer (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "mobile-app-developer-android-ios",
            "name": "Mobile App Developer (Android/iOS)",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Professional role working in the field of Mobile App Developer (Android/iOS) to design, implement, or manage solutions.",
            "about": "A Mobile App Developer (Android/iOS) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Mobile App Developer (Android/iOS)."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "game-developer",
            "name": "Game Developer",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Professional role working in the field of Game Developer to design, implement, or manage solutions.",
            "about": "A Game Developer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Game Developer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "web-developer",
            "name": "Web Developer",
            "interest_tags": [
                "Software & App Development"
            ],
            "short_description": "Professional role working in the field of Web Developer to design, implement, or manage solutions.",
            "about": "A Web Developer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Web Developer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "aiml-engineer",
            "name": "AI/ML Engineer",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Develops algorithms and mathematical models that enable computers to learn, make decisions, and act autonomously.",
            "about": "AI and Machine Learning Engineers design the systems that power self-driving cars, recommend songs, or chat like humans. You will write code in Python, C++, or Julia, work with neural network architectures (transformers, CNNs), optimize training datasets, and deploy machine learning models on cloud platforms. It requires strong math, logic, and coding skills.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Mathematics (PCM) background.",
                "Clear JEE Main, JEE Advanced, or BITSAT.",
                "Obtain B.Tech/B.E. in Computer Science, AI, or Data Science (4 years).",
                "Learn Python, TensorFlow/PyTorch, and linear algebra through online portfolios.",
                "Complete M.Tech or M.Sc. in Machine Learning or Artificial Intelligence (Optional)."
            ],
            "entrance_exams": [
                "JEE-Main",
                "BITSAT"
            ],
            "salary_range": "₹8–24 LPA",
            "growth_outlook": "Exceptional demand, key sector in the New Economy",
            "colleges": [
                {
                    "name": "IIT Bombay, Mumbai",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iitb.ac.in/",
                    "short_description": "Highly prestigious engineering institute with active AI research labs.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "IIIT Hyderabad, Hyderabad",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iiit.ac.in/",
                    "short_description": "National leader in robotics, computer vision, and machine learning research.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Carnegie Mellon University, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.cmu.edu/",
                    "short_description": "Global pioneer in artificial intelligence and computer science education.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "data-scientist",
            "name": "Data Scientist",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Analyzes complex datasets using statistics and machine learning to uncover insights and solve business problems.",
            "about": "Data Scientists combine programming, mathematics, and analytical reasoning. You'll write code in Python or R, clean messy datasets, build machine learning models to predict trends, and design data visualizations to present your findings to decision-makers. It's a rapidly growing field perfect for students who love logic, data, and computers.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Mathematics (PCM) background.",
                "Clear JEE Main, BITSAT, or ISI Admission Test.",
                "Obtain B.Tech/B.E. in Computer Science or B.Sc. in Statistics/Mathematics (3-4 years).",
                "Complete M.Sc. in Data Science or MCA (Optional, 2 years).",
                "Acquire junior role or internships to gain professional experience."
            ],
            "entrance_exams": [
                "JEE-Main",
                "ISI-Admission-Test",
                "BITSAT"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "High demand, 30% YoY growth",
            "colleges": [
                {
                    "name": "Indian Statistical Institute (ISI), Kolkata",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.isical.ac.in/",
                    "short_description": "India's premier institute for statistics and mathematical sciences.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "IIT Madras, Chennai",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iitm.ac.in/",
                    "short_description": "Renowned for its engineering and computer science programs.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "BITS Pilani, Pilani",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.bits-pilani.ac.in/",
                    "short_description": "A top-tier private institute for engineering and technology.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "IIIT Delhi, New Delhi",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.iiitd.ac.in/",
                    "short_description": "Excellent state university with a strong focus on CS and IT.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Stanford University, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.stanford.edu/",
                    "short_description": "Global leader in computer science and data studies.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "data-analyst",
            "name": "Data Analyst",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Professional role working in the field of Data Analyst to design, implement, or manage solutions.",
            "about": "A Data Analyst applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Data Analyst."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "data-engineer",
            "name": "Data Engineer",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Professional role working in the field of Data Engineer to design, implement, or manage solutions.",
            "about": "A Data Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Data Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "ai-research-scientist",
            "name": "AI Research Scientist",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Professional role working in the field of AI Research Scientist to design, implement, or manage solutions.",
            "about": "A AI Research Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in AI Research Scientist."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "computer-vision-engineer",
            "name": "Computer Vision Engineer",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Professional role working in the field of Computer Vision Engineer to design, implement, or manage solutions.",
            "about": "A Computer Vision Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Computer Vision Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "nlp-engineer",
            "name": "NLP Engineer",
            "interest_tags": [
                "Data & AI"
            ],
            "short_description": "Professional role working in the field of NLP Engineer to design, implement, or manage solutions.",
            "about": "A NLP Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in NLP Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "cybersecurity-analyst",
            "name": "Cybersecurity Analyst",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Protects an organization's computer networks, data, and digital systems from unauthorized access, hacks, and security threats.",
            "about": "Cybersecurity Analysts act as digital security guards. You will monitor network traffic for suspicious activity, set up firewalls, conduct vulnerability assessments (ethical hacking), and respond to security breaches. As threats grow globally, companies of all sizes are investing heavily in defensive cybersecurity teams.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Mathematics (PCM) background.",
                "Clear JEE Main, BITSAT, or CUET-UG.",
                "Obtain B.Tech or B.Sc. in Computer Science or Cybersecurity (3-4 years).",
                "Obtain professional certifications like CEH (Certified Ethical Hacker) or CompTIA Security+.",
                "Join an IT firm or corporate security operations center (SOC)."
            ],
            "entrance_exams": [
                "JEE-Main",
                "BITSAT"
            ],
            "salary_range": "₹5–15 LPA",
            "growth_outlook": "High growth, critical corporate priority worldwide",
            "colleges": [
                {
                    "name": "IIT Madras, Chennai",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iitm.ac.in/",
                    "short_description": "Renowned engineering institute with a dedicated cybersecurity laboratory.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "IIIT Delhi, New Delhi",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.iiitd.ac.in/",
                    "short_description": "Highly respected state university with strong cybersecurity specializations.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Carnegie Mellon University, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.cmu.edu/",
                    "short_description": "Top-tier university globally for information security research.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "ethical-hacker-penetration-tester",
            "name": "Ethical Hacker/Penetration Tester",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Professional role working in the field of Ethical Hacker/Penetration Tester to design, implement, or manage solutions.",
            "about": "A Ethical Hacker/Penetration Tester applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Ethical Hacker/Penetration Tester."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "network-engineer",
            "name": "Network Engineer",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Professional role working in the field of Network Engineer to design, implement, or manage solutions.",
            "about": "A Network Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Network Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "cloud-architect-engineer",
            "name": "Cloud Architect/Engineer",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Professional role working in the field of Cloud Architect/Engineer to design, implement, or manage solutions.",
            "about": "A Cloud Architect/Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Cloud Architect/Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "devops-engineer",
            "name": "DevOps Engineer",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Bridges the gap between software development and IT operations, automating server deployments.",
            "about": "DevOps Engineers manage the deployment pipelines of tech platforms. You will set up automated testing scripts, configure server clusters, handle scaling events, and debug infrastructure downtime.",
            "educational_roadmap": [
                "Class 12 with PCM.",
                "B.Tech in Computer Science or Information Technology (4 years).",
                "Learn containerization (Docker, Kubernetes) and CI/CD tools.",
                "Join infrastructure engineering teams at cloud-scale businesses."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹6–16 LPA",
            "growth_outlook": "Very high demand, key operations role in modern IT",
            "colleges": [
                {
                    "name": "Indian Institute of DevOps & Site Reliability Engineer (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in DevOps & Site Reliability Engineer.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of DevOps & Site Reliability Engineer (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of DevOps & Site Reliability Engineer (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "site-reliability-engineer",
            "name": "Site Reliability Engineer",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Professional role working in the field of Site Reliability Engineer to design, implement, or manage solutions.",
            "about": "A Site Reliability Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Site Reliability Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "it-systems-administrator",
            "name": "IT Systems Administrator",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Professional role working in the field of IT Systems Administrator to design, implement, or manage solutions.",
            "about": "A IT Systems Administrator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in IT Systems Administrator."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "database-administrator",
            "name": "Database Administrator",
            "interest_tags": [
                "Cybersecurity & Infrastructure"
            ],
            "short_description": "Configures, secures, and maintains database servers to ensure quick and reliable access to enterprise data.",
            "about": "Database Administrators maintain complex SQL and NoSQL servers. You will organize schema architecture, verify daily data backups, handle server security permissions, and tune slow database queries.",
            "educational_roadmap": [
                "Class 12 with PCM or Commerce.",
                "B.Tech in CS, BCA, or B.Sc. in Computer Science.",
                "Obtain database administration certifications (Oracle, Microsoft SQL, etc.).",
                "Join IT service companies or financial databases."
            ],
            "entrance_exams": [
                "JEE-Main",
                "CUET-UG"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Stable, business operations support role",
            "colleges": [
                {
                    "name": "Indian Institute of Database Administrator (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Database Administrator.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Database Administrator (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Database Administrator (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "computer-hardware-engineer",
            "name": "Computer Hardware Engineer",
            "interest_tags": [
                "Hardware & Engineering"
            ],
            "short_description": "Professional role working in the field of Computer Hardware Engineer to design, implement, or manage solutions.",
            "about": "A Computer Hardware Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Computer Hardware Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "robotics-engineer",
            "name": "Robotics Engineer",
            "interest_tags": [
                "Hardware & Engineering"
            ],
            "short_description": "Designs, builds, and tests robotic systems and autonomous devices for manufacturing, space, and medical industries.",
            "about": "Robotics engineers write software to control robotic movements, design physical sensors and joints, and deploy automated systems. You'll bridge the gap between mechanical engineering, electrical circuits, and artificial intelligence.",
            "educational_roadmap": [
                "Class 12 with PCM background.",
                "Clear JEE-Main or BITSAT.",
                "B.Tech in Mechatronics, Mechanical, or Computer Science (4 years).",
                "Gather internships in robotics labs and industrial automation firms."
            ],
            "entrance_exams": [
                "JEE-Main",
                "BITSAT"
            ],
            "salary_range": "₹6–18 LPA",
            "growth_outlook": "High growth, fueled by industrial automation",
            "colleges": [
                {
                    "name": "Indian Institute of Robotics Engineering (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Robotics Engineering.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Robotics Engineering (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Robotics Engineering (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "embedded-systems-engineer",
            "name": "Embedded Systems Engineer",
            "interest_tags": [
                "Hardware & Engineering"
            ],
            "short_description": "Professional role working in the field of Embedded Systems Engineer to design, implement, or manage solutions.",
            "about": "A Embedded Systems Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Embedded Systems Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "vlsi-chip-design-engineer",
            "name": "VLSI/Chip Design Engineer",
            "interest_tags": [
                "Hardware & Engineering"
            ],
            "short_description": "Professional role working in the field of VLSI/Chip Design Engineer to design, implement, or manage solutions.",
            "about": "A VLSI/Chip Design Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in VLSI/Chip Design Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "mechatronics-engineer",
            "name": "Mechatronics Engineer",
            "interest_tags": [
                "Hardware & Engineering"
            ],
            "short_description": "Professional role working in the field of Mechatronics Engineer to design, implement, or manage solutions.",
            "about": "A Mechatronics Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Mechatronics Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "electronics-engineer",
            "name": "Electronics Engineer",
            "interest_tags": [
                "Hardware & Engineering"
            ],
            "short_description": "Professional role working in the field of Electronics Engineer to design, implement, or manage solutions.",
            "about": "A Electronics Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Electronics Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "telecom-engineer",
            "name": "Telecom Engineer",
            "interest_tags": [
                "Telecom & Networks"
            ],
            "short_description": "Professional role working in the field of Telecom Engineer to design, implement, or manage solutions.",
            "about": "A Telecom Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Telecom Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "network-architect",
            "name": "Network Architect",
            "interest_tags": [
                "Telecom & Networks"
            ],
            "short_description": "Professional role working in the field of Network Architect to design, implement, or manage solutions.",
            "about": "A Network Architect applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Network Architect."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "wireless-5g-engineer",
            "name": "Wireless/5G Engineer",
            "interest_tags": [
                "Telecom & Networks"
            ],
            "short_description": "Professional role working in the field of Wireless/5G Engineer to design, implement, or manage solutions.",
            "about": "A Wireless/5G Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Wireless/5G Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "technical-product-manager",
            "name": "Technical Product Manager",
            "interest_tags": [
                "Product, Design & Quality"
            ],
            "short_description": "Professional role working in the field of Technical Product Manager to design, implement, or manage solutions.",
            "about": "A Technical Product Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Technical Product Manager."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "ui-ux-designer",
            "name": "UI/UX Designer",
            "interest_tags": [
                "Product, Design & Quality"
            ],
            "short_description": "Professional role working in the field of UI/UX Designer to design, implement, or manage solutions.",
            "about": "A UI/UX Designer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in UI/UX Designer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "qa-test-engineer",
            "name": "QA/Test Engineer",
            "interest_tags": [
                "Product, Design & Quality"
            ],
            "short_description": "Professional role working in the field of QA/Test Engineer to design, implement, or manage solutions.",
            "about": "A QA/Test Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in QA/Test Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "technical-writer",
            "name": "Technical Writer",
            "interest_tags": [
                "Product, Design & Quality"
            ],
            "short_description": "Simplifies highly complex product designs and technical software code into user manuals and developer guidelines.",
            "about": "Technical Writers bridge technology and human users, documenting software APIs, developer guides, and manufacturing operations details.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Science).",
                "B.A. in English/Linguistics or B.Sc. in Computer Science.",
                "Build a portfolio writing clear instructional documentation."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹5–13 LPA",
            "growth_outlook": "Steady demand in IT and engineering corporations",
            "colleges": [
                {
                    "name": "Indian Institute of Technical Writing (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Technical Writing.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Technical Writing (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Technical Writing (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "blockchain-developer",
            "name": "Blockchain Developer",
            "interest_tags": [
                "Emerging Tech"
            ],
            "short_description": "Professional role working in the field of Blockchain Developer to design, implement, or manage solutions.",
            "about": "A Blockchain Developer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Blockchain Developer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "ar-vr-developer",
            "name": "AR/VR Developer",
            "interest_tags": [
                "Emerging Tech"
            ],
            "short_description": "Creates immersive virtual reality worlds and augmented reality filters for headsets and mobile phones.",
            "about": "AR/VR developers build code for spatial computing platforms. You will work inside game engines (Unity, Unreal), program physics logic, and design interactive 3D assets.",
            "educational_roadmap": [
                "Class 12 with PCM background.",
                "B.Tech in Computer Science, Game Design, or B.Des in Digital Media (4 years).",
                "Learn C# or C++ scripting and 3D modeling pipelines.",
                "Join gaming studios, educational software firms, or tech labs."
            ],
            "entrance_exams": [
                "JEE-Main",
                "UCEED"
            ],
            "salary_range": "₹5–13 LPA",
            "growth_outlook": "Rapidly growing niche in gaming, training, and retail industries",
            "colleges": [
                {
                    "name": "Indian Institute of AR/VR Systems Developer (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in AR/VR Systems Developer.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of AR/VR Systems Developer (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of AR/VR Systems Developer (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "iot-engineer",
            "name": "IoT Engineer",
            "interest_tags": [
                "Emerging Tech"
            ],
            "short_description": "Professional role working in the field of IoT Engineer to design, implement, or manage solutions.",
            "about": "A IoT Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in IoT Engineer."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "quantum-computing-researcher",
            "name": "Quantum Computing Researcher",
            "interest_tags": [
                "Emerging Tech"
            ],
            "short_description": "Professional role working in the field of Quantum Computing Researcher to design, implement, or manage solutions.",
            "about": "A Quantum Computing Researcher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with PCM / PCB background.",
                "Clear engineering entrance exams like JEE Main, BITSAT, or state-level CETs.",
                "Complete B.Tech/B.E. in Computer Science, Information Technology, or Electronics (4 years), or BCA/B.Sc. CS.",
                "Learn key development frameworks and modern programming languages (e.g., Python, JavaScript, C++, SQL).",
                "Build a GitHub portfolio with personal/open-source projects and complete a junior developer internship.",
                "Obtain vendor certifications (e.g. AWS, Cisco, RedHat) and join tech firms as a junior specialist in Quantum Computing Researcher."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Medicine & Healthcare": [
        {
            "id": "doctor-physician",
            "name": "Doctor (General Physician)",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Diagnoses illnesses, prescribes treatments, and provides primary medical care to patients.",
            "about": "Medical Doctors diagnose acute and chronic illnesses, interpret diagnostic lab tests, prescribe therapeutics, and counsel patients on lifestyle health practices. It is a highly respected career dedicated to saving lives.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear NEET-UG exam.",
                "Complete Bachelor of Medicine and Bachelor of Surgery (MBBS) (5.5 years including internship).",
                "Register with National Medical Commission (NMC)."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹8–20 LPA",
            "growth_outlook": "Stable demand, critical public health role",
            "colleges": [
                {
                    "name": "Indian Institute of Medical Doctor / General Physician (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Medical Doctor / General Physician.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Medical Doctor / General Physician (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Medical Doctor / General Physician (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "pediatrician",
            "name": "Pediatrician",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of Pediatrician to design, implement, or manage solutions.",
            "about": "A Pediatrician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Pediatrician (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Pediatrician.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Pediatrician (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Pediatrician (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "cardiologist",
            "name": "Cardiologist",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of Cardiologist to design, implement, or manage solutions.",
            "about": "A Cardiologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Cardiologist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Cardiologist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Cardiologist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Cardiologist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "gynecologist",
            "name": "Gynecologist",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of Gynecologist to design, implement, or manage solutions.",
            "about": "A Gynecologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Gynecologist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Gynecologist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Gynecologist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Gynecologist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "orthopedic-surgeon",
            "name": "Orthopedic Surgeon",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of Orthopedic Surgeon to design, implement, or manage solutions.",
            "about": "A Orthopedic Surgeon applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Orthopedic Surgeon (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Orthopedic Surgeon.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Orthopedic Surgeon (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Orthopedic Surgeon (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "ent-specialist",
            "name": "ENT Specialist",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of ENT Specialist to design, implement, or manage solutions.",
            "about": "A ENT Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of ENT Specialist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in ENT Specialist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of ENT Specialist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of ENT Specialist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "surgeon",
            "name": "Surgeon",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Performs medical operations to treat injuries, diseases, and deformities in human organs.",
            "about": "Surgeons are medical doctors who specialize in invasive operations. You will consult on pre-operative scans, execute precision operations in clean theatres, and handle post-operative patient wards.",
            "educational_roadmap": [
                "Class 12 with PCB.",
                "Clear NEET-UG and complete MBBS (5.5 years).",
                "Clear NEET-PG and complete Master of Surgery (MS) or DNB (3 years).",
                "Complete fellowships in super-specialties (Cardiology, Neurosurgery, etc.)."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹12–35 LPA",
            "growth_outlook": "High demand, highly specialized pathway",
            "colleges": [
                {
                    "name": "Indian Institute of Specialist Surgeon (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Specialist Surgeon.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Specialist Surgeon (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Specialist Surgeon (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "anesthesiologist",
            "name": "Anesthesiologist",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of Anesthesiologist to design, implement, or manage solutions.",
            "about": "A Anesthesiologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Anesthesiologist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Anesthesiologist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Anesthesiologist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Anesthesiologist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "psychiatrist",
            "name": "Psychiatrist",
            "interest_tags": [
                "Clinical Medicine"
            ],
            "short_description": "Professional role working in the field of Psychiatrist to design, implement, or manage solutions.",
            "about": "A Psychiatrist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Psychiatrist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Psychiatrist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Psychiatrist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Psychiatrist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "dentist",
            "name": "Dentist",
            "interest_tags": [
                "Dental Care"
            ],
            "short_description": "Diagnoses, treats, and prevents diseases of the teeth, gums, and oral cavity.",
            "about": "Dentists clean teeth, fill cavities, perform root canals, design dental crowns, treat gum infections, and handle jaw corrections.",
            "educational_roadmap": [
                "Class 12 with PCB.",
                "Clear NEET-UG exam.",
                "Complete Bachelor of Dental Surgery (BDS) (5 years including internship).",
                "Register with Dental Council of India (DCI) and open clinic or join hospital."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹4–12 LPA",
            "growth_outlook": "Steady demand, expanding wellness and cosmetic sectors",
            "colleges": [
                {
                    "name": "Indian Institute of Dentist / Dental Surgeon (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Dentist / Dental Surgeon.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Dentist / Dental Surgeon (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Dentist / Dental Surgeon (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "dental-hygienist",
            "name": "Dental Hygienist",
            "interest_tags": [
                "Dental Care"
            ],
            "short_description": "Professional role working in the field of Dental Hygienist to design, implement, or manage solutions.",
            "about": "A Dental Hygienist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Dental Hygienist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Dental Hygienist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Dental Hygienist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Dental Hygienist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "orthodontist",
            "name": "Orthodontist",
            "interest_tags": [
                "Dental Care"
            ],
            "short_description": "Professional role working in the field of Orthodontist to design, implement, or manage solutions.",
            "about": "A Orthodontist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Clear the National Eligibility cum Entrance Test (NEET-UG).",
                "Complete Bachelor of Medicine & Surgery (MBBS) or Dental Surgery (BDS) (5 years).",
                "Register with regulatory councils and complete a rotatory clinical internship."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": [
                {
                    "name": "Indian Institute of Orthodontist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Orthodontist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Orthodontist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Orthodontist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "nurse",
            "name": "Nurse",
            "interest_tags": [
                "Nursing & Allied Care"
            ],
            "short_description": "Provides professional clinical care, monitors patients, and assists physicians in hospital clinics.",
            "about": "Nurses administer therapeutics, dress wounds, monitor vitals, update clinical charts, and counsel patients. They form the core execution layer of clinical setups.",
            "educational_roadmap": [
                "Class 12 in Science (PCB).",
                "Obtain B.Sc. in Nursing (4 years) or General Nursing and Midwifery (GNM) diploma.",
                "Register with the State Nursing Council.",
                "Join public or private hospital wards."
            ],
            "entrance_exams": [
                "NEET",
                "CUET-UG"
            ],
            "salary_range": "₹3–8 LPA",
            "growth_outlook": "High demand globally, expanding public health sector",
            "colleges": [
                {
                    "name": "Indian Institute of Registered Nurse / Healthcare Provider (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Registered Nurse / Healthcare Provider.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Registered Nurse / Healthcare Provider (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Registered Nurse / Healthcare Provider (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "physiotherapist",
            "name": "Physiotherapist",
            "interest_tags": [
                "Nursing & Allied Care"
            ],
            "short_description": "Helps patients restore physical mobility and manage pain after athletic injuries, surgeries, or strokes.",
            "about": "Physiotherapists design custom exercise routines, apply massage techniques, use electrotherapy devices, and track joint recovery coordinates.",
            "educational_roadmap": [
                "Class 12 with PCB background.",
                "Clear university entrance exams.",
                "Bachelor of Physiotherapy (BPT) (4.5 years including clinical internship).",
                "Join hospitals, athletic franchises, or open custom physiotherapy clinics."
            ],
            "entrance_exams": [
                "NEET",
                "CUET-UG"
            ],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "Strong demand in geriatric wellness and competitive sports panels",
            "colleges": [
                {
                    "name": "Indian Institute of Physiotherapist & Rehabilitation Specialist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Physiotherapist & Rehabilitation Specialist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Physiotherapist & Rehabilitation Specialist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Physiotherapist & Rehabilitation Specialist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "occupational-therapist",
            "name": "Occupational Therapist",
            "interest_tags": [
                "Nursing & Allied Care"
            ],
            "short_description": "Professional role working in the field of Occupational Therapist to design, implement, or manage solutions.",
            "about": "A Occupational Therapist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Occupational Therapist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "speech-therapist",
            "name": "Speech Therapist",
            "interest_tags": [
                "Nursing & Allied Care"
            ],
            "short_description": "Professional role working in the field of Speech Therapist to design, implement, or manage solutions.",
            "about": "A Speech Therapist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Speech Therapist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "midwife",
            "name": "Midwife",
            "interest_tags": [
                "Nursing & Allied Care"
            ],
            "short_description": "Professional role working in the field of Midwife to design, implement, or manage solutions.",
            "about": "A Midwife applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Midwife."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "emergency-medical-technician-paramedic",
            "name": "Emergency Medical Technician (Paramedic)",
            "interest_tags": [
                "Nursing & Allied Care"
            ],
            "short_description": "Professional role working in the field of Emergency Medical Technician (Paramedic) to design, implement, or manage solutions.",
            "about": "A Emergency Medical Technician (Paramedic) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Emergency Medical Technician (Paramedic)."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "optometrist",
            "name": "Optometrist",
            "interest_tags": [
                "Vision Care"
            ],
            "short_description": "Professional role working in the field of Optometrist to design, implement, or manage solutions.",
            "about": "A Optometrist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Optometrist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "ophthalmologist",
            "name": "Ophthalmologist",
            "interest_tags": [
                "Vision Care"
            ],
            "short_description": "Professional role working in the field of Ophthalmologist to design, implement, or manage solutions.",
            "about": "A Ophthalmologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Ophthalmologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "medical-lab-technician",
            "name": "Medical Lab Technician",
            "interest_tags": [
                "Diagnostics & Lab"
            ],
            "short_description": "Professional role working in the field of Medical Lab Technician to design, implement, or manage solutions.",
            "about": "A Medical Lab Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Medical Lab Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "radiologist",
            "name": "Radiologist",
            "interest_tags": [
                "Diagnostics & Lab"
            ],
            "short_description": "Professional role working in the field of Radiologist to design, implement, or manage solutions.",
            "about": "A Radiologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Radiologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "pathologist",
            "name": "Pathologist",
            "interest_tags": [
                "Diagnostics & Lab"
            ],
            "short_description": "Professional role working in the field of Pathologist to design, implement, or manage solutions.",
            "about": "A Pathologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Pathologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sonographer",
            "name": "Sonographer",
            "interest_tags": [
                "Diagnostics & Lab"
            ],
            "short_description": "Professional role working in the field of Sonographer to design, implement, or manage solutions.",
            "about": "A Sonographer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Sonographer."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "pharmacist",
            "name": "Pharmacist",
            "interest_tags": [
                "Pharma & Alternative Medicine"
            ],
            "short_description": "Dispenses medicines, reviews patient prescriptions, and advises on therapeutics safety.",
            "about": "Pharmacists read physician prescriptions, check for harmful drug interactions, dispense dosage instructions, and advise on drug compounds storage.",
            "educational_roadmap": [
                "Class 12 with PCB or PCM.",
                "B.Pharm (Bachelor of Pharmacy) (4 years).",
                "Obtain registered pharmacist license from Pharmacy Council of India (PCI).",
                "Join hospital pharmacies, retail drugstores, or pharmaceutical companies."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3–7 LPA",
            "growth_outlook": "Steady demand, linked to expanding healthcare distribution grids",
            "colleges": [
                {
                    "name": "Indian Institute of Clinical Pharmacist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Clinical Pharmacist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Clinical Pharmacist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Clinical Pharmacist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "ayurveda-practitioner",
            "name": "Ayurveda Practitioner",
            "interest_tags": [
                "Pharma & Alternative Medicine"
            ],
            "short_description": "Professional role working in the field of Ayurveda Practitioner to design, implement, or manage solutions.",
            "about": "A Ayurveda Practitioner applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Ayurveda Practitioner."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "homeopathy-practitioner",
            "name": "Homeopathy Practitioner",
            "interest_tags": [
                "Pharma & Alternative Medicine"
            ],
            "short_description": "Professional role working in the field of Homeopathy Practitioner to design, implement, or manage solutions.",
            "about": "A Homeopathy Practitioner applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Homeopathy Practitioner."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "naturopath",
            "name": "Naturopath",
            "interest_tags": [
                "Pharma & Alternative Medicine"
            ],
            "short_description": "Professional role working in the field of Naturopath to design, implement, or manage solutions.",
            "about": "A Naturopath applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Naturopath."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "nutritionist-dietitian",
            "name": "Nutritionist/Dietitian",
            "interest_tags": [
                "Nutrition & Wellness"
            ],
            "short_description": "Professional role working in the field of Nutritionist/Dietitian to design, implement, or manage solutions.",
            "about": "A Nutritionist/Dietitian applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Nutritionist/Dietitian."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "biomedical-engineer",
            "name": "Biomedical Engineer",
            "interest_tags": [
                "Health Systems & Tech"
            ],
            "short_description": "Professional role working in the field of Biomedical Engineer to design, implement, or manage solutions.",
            "about": "A Biomedical Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Biomedical Engineer."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "hospital-administrator",
            "name": "Hospital Administrator",
            "interest_tags": [
                "Health Systems & Tech"
            ],
            "short_description": "Professional role working in the field of Hospital Administrator to design, implement, or manage solutions.",
            "about": "A Hospital Administrator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Hospital Administrator."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "public-health-specialist",
            "name": "Public Health Specialist",
            "interest_tags": [
                "Health Systems & Tech"
            ],
            "short_description": "Professional role working in the field of Public Health Specialist to design, implement, or manage solutions.",
            "about": "A Public Health Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Public Health Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "health-informatics-specialist",
            "name": "Health Informatics Specialist",
            "interest_tags": [
                "Health Systems & Tech"
            ],
            "short_description": "Professional role working in the field of Health Informatics Specialist to design, implement, or manage solutions.",
            "about": "A Health Informatics Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Health Informatics Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "medical-equipment-technician",
            "name": "Medical Equipment Technician",
            "interest_tags": [
                "Health Systems & Tech"
            ],
            "short_description": "Professional role working in the field of Medical Equipment Technician to design, implement, or manage solutions.",
            "about": "A Medical Equipment Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Medical Equipment Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "clinical-researcher",
            "name": "Clinical Researcher",
            "interest_tags": [
                "Medical Research"
            ],
            "short_description": "Professional role working in the field of Clinical Researcher to design, implement, or manage solutions.",
            "about": "A Clinical Researcher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Clinical Researcher."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "pharmacologist",
            "name": "Pharmacologist",
            "interest_tags": [
                "Medical Research"
            ],
            "short_description": "Professional role working in the field of Pharmacologist to design, implement, or manage solutions.",
            "about": "A Pharmacologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB).",
                "Prepare for and clear the NEET-UG entrance examination.",
                "Obtain a professional medical or allied degree (MBBS, BDS, BAMS, BHMS, or BPT depending on sub-field) (4.5 - 5.5 years).",
                "Complete a compulsory rotatory clinical internship in a registered teaching hospital.",
                "Register with the National Medical Commission (NMC) or relevant state allied health council.",
                "Complete a post-graduate residency (MD/MS/DNB) or specialization training to practice as a certified Pharmacologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹6–15 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "epidemiologist",
            "name": "Epidemiologist",
            "interest_tags": [
                "Medical Research"
            ],
            "short_description": "Investigates the patterns and causes of diseases in human populations to prevent future disease outbreaks.",
            "about": "Epidemiologists collect public health data, trace disease vector sources, design pandemic containment models, and draft public safety codes.",
            "educational_roadmap": [
                "Class 12 with PCB/PCM.",
                "Obtain MBBS, B.Sc. in biology/stats, or B.Pharm (3-5 years).",
                "Complete Master of Public Health (MPH) or M.Sc. in Epidemiology (2 years).",
                "Join government health units, WHO panels, or health research groups."
            ],
            "entrance_exams": [
                "NEET",
                "CUET-UG"
            ],
            "salary_range": "₹5–13 LPA",
            "growth_outlook": "High demand in public administration and global healthcare consultancy",
            "colleges": [
                {
                    "name": "Indian Institute of Epidemiologist & Public Health Researcher (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Epidemiologist & Public Health Researcher.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Epidemiologist & Public Health Researcher (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Epidemiologist & Public Health Researcher (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        }
    ],
    "Pure Sciences & Research": [
        {
            "id": "research-scientist-physics",
            "name": "Research Scientist (Physics)",
            "interest_tags": [
                "Physical Sciences"
            ],
            "short_description": "Professional role working in the field of Research Scientist (Physics) to design, implement, or manage solutions.",
            "about": "A Research Scientist (Physics) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Research Scientist (Physics)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "materials-scientist",
            "name": "Materials Scientist",
            "interest_tags": [
                "Physical Sciences"
            ],
            "short_description": "Investigates the chemical structures of materials to design durable plastics, metals, polymers, and superconductors.",
            "about": "Materials Scientists design new polymers, carbon structures, and battery chemicals. You will compile chemical specs, test fatigue limits, and consult on industrial packaging.",
            "educational_roadmap": [
                "Class 12 with PCM.",
                "B.Sc. in Chemistry or B.Tech in Materials Engineering (3-4 years).",
                "M.Sc. in Chemistry or Material Sciences (2 years).",
                "Join packaging companies, battery startups, or research institutes."
            ],
            "entrance_exams": [
                "JEE-Main",
                "CUET-UG"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Strong demand, driven by green energy storage requirements",
            "colleges": [
                {
                    "name": "Indian Institute of Materials Scientist & Chemist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Materials Scientist & Chemist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Materials Scientist & Chemist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Materials Scientist & Chemist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "astronomer-astrophysicist",
            "name": "Astronomer/Astrophysicist",
            "interest_tags": [
                "Physical Sciences"
            ],
            "short_description": "Professional role working in the field of Astronomer/Astrophysicist to design, implement, or manage solutions.",
            "about": "A Astronomer/Astrophysicist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Astronomer/Astrophysicist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "nuclear-scientist",
            "name": "Nuclear Scientist",
            "interest_tags": [
                "Physical Sciences"
            ],
            "short_description": "Professional role working in the field of Nuclear Scientist to design, implement, or manage solutions.",
            "about": "A Nuclear Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Nuclear Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "research-scientist-chemistry",
            "name": "Research Scientist (Chemistry)",
            "interest_tags": [
                "Chemical Sciences"
            ],
            "short_description": "Professional role working in the field of Research Scientist (Chemistry) to design, implement, or manage solutions.",
            "about": "A Research Scientist (Chemistry) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Research Scientist (Chemistry)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "biochemist",
            "name": "Biochemist",
            "interest_tags": [
                "Chemical Sciences"
            ],
            "short_description": "Studies the chemical processes and changes occurring inside living organisms to develop health enzymes.",
            "about": "Biochemists research metabolic paths, synthesize enzymes, map cell responses to therapeutics, and check toxic chemical indices in crops.",
            "educational_roadmap": [
                "Class 12 with PCB/PCM.",
                "B.Sc. in Biochemistry or Chemistry (3 years).",
                "M.Sc. in Biochemistry (2 years).",
                "Join clinical research institutes or agricultural labs."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, expanding pharma and agrochemical lines",
            "colleges": [
                {
                    "name": "Indian Institute of Biochemist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Biochemist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Biochemist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Biochemist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "analytical-chemist",
            "name": "Analytical Chemist",
            "interest_tags": [
                "Chemical Sciences"
            ],
            "short_description": "Professional role working in the field of Analytical Chemist to design, implement, or manage solutions.",
            "about": "A Analytical Chemist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Analytical Chemist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "research-scientist-biology",
            "name": "Research Scientist (Biology)",
            "interest_tags": [
                "Biological Sciences"
            ],
            "short_description": "Professional role working in the field of Research Scientist (Biology) to design, implement, or manage solutions.",
            "about": "A Research Scientist (Biology) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Research Scientist (Biology)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "microbiologist",
            "name": "Microbiologist",
            "interest_tags": [
                "Biological Sciences"
            ],
            "short_description": "Professional role working in the field of Microbiologist to design, implement, or manage solutions.",
            "about": "A Microbiologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Microbiologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "geneticist",
            "name": "Geneticist",
            "interest_tags": [
                "Biological Sciences"
            ],
            "short_description": "Professional role working in the field of Geneticist to design, implement, or manage solutions.",
            "about": "A Geneticist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Geneticist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "zoologist",
            "name": "Zoologist",
            "interest_tags": [
                "Biological Sciences"
            ],
            "short_description": "Professional role working in the field of Zoologist to design, implement, or manage solutions.",
            "about": "A Zoologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Zoologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "botanist",
            "name": "Botanist",
            "interest_tags": [
                "Biological Sciences"
            ],
            "short_description": "Professional role working in the field of Botanist to design, implement, or manage solutions.",
            "about": "A Botanist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Botanist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "geologist",
            "name": "Geologist",
            "interest_tags": [
                "Earth Sciences"
            ],
            "short_description": "Studies Earth's structures, rock layers, minerals, and tectonic history to consult on mining and earthquakes.",
            "about": "Geologists map mineral sites, trace groundwater flows, assess land stability for bridges, and analyze seismic sensor feeds.",
            "educational_roadmap": [
                "Class 12 with PCM/PCB.",
                "B.Sc. in Geology or Earth Sciences (3 years).",
                "M.Sc. in Applied Geology or Geophysics (2 years).",
                "Join geological surveys, mining entities, or civil engineering firms."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Steady demand, linked to resources management",
            "colleges": [
                {
                    "name": "Indian Institute of Geologist / Geophysicist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Geologist / Geophysicist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Geologist / Geophysicist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Geologist / Geophysicist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "oceanographer",
            "name": "Oceanographer",
            "interest_tags": [
                "Earth Sciences"
            ],
            "short_description": "Professional role working in the field of Oceanographer to design, implement, or manage solutions.",
            "about": "A Oceanographer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Oceanographer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "meteorologist",
            "name": "Meteorologist",
            "interest_tags": [
                "Earth Sciences"
            ],
            "short_description": "Analyzes atmospheric radar, pressure grids, and satellite feeds to predict weather patterns and model climate changes.",
            "about": "Meteorologists compile weather models, track cyclonic movements, check atmospheric ozone indicators, and warn governments on disaster management patterns.",
            "educational_roadmap": [
                "Class 12 with PCM.",
                "B.Sc. in Atmospheric Science or Physics.",
                "M.Sc. in Meteorology / Climate Science (2 years).",
                "Join national weather departments, satellite agencies, or agricultural planning bodies."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Steady demand, critical role for climate adaptation planning",
            "colleges": [
                {
                    "name": "Indian Institute of Meteorologist / Climate Scientist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Meteorologist / Climate Scientist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Meteorologist / Climate Scientist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Meteorologist / Climate Scientist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "seismologist",
            "name": "Seismologist",
            "interest_tags": [
                "Earth Sciences"
            ],
            "short_description": "Professional role working in the field of Seismologist to design, implement, or manage solutions.",
            "about": "A Seismologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Seismologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "environmental-scientist",
            "name": "Environmental Scientist",
            "interest_tags": [
                "Environmental Science"
            ],
            "short_description": "Studies the environment and works to find sustainable solutions to pollution, climate change, and habitat loss.",
            "about": "Environmental Scientists conduct field research (collecting water, soil, and air samples), assess the environmental impact of construction projects, advise governments on policies, and design strategies to restore damaged ecosystems. It's a hands-on, meaningful career for people who want to save the planet.",
            "educational_roadmap": [
                "Class 12 with PCB or PCM background.",
                "Clear CUET-UG or ICAR-AIEEA.",
                "B.Sc. in Environmental Science, Ecology, or Forestry (3 years).",
                "M.Sc. in Environmental Management or Environmental Engineering (2 years).",
                "Join an environmental consultancy or government agency."
            ],
            "entrance_exams": [
                "ICAR-AIEEA",
                "SAT"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, expanding corporate ESG demands",
            "colleges": [
                {
                    "name": "Jawaharlal Nehru University (JNU), New Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.jnu.ac.in/",
                    "short_description": "Outstanding environmental sciences department.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Forest Research Institute (FRI), Dehradun",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "http://fri.res.in/",
                    "short_description": "Premier institute for forestry education and research.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Yale University, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.yale.edu/",
                    "short_description": "Top-tier global center for environmental research.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "ecologist",
            "name": "Ecologist",
            "interest_tags": [
                "Environmental Science"
            ],
            "short_description": "Professional role working in the field of Ecologist to design, implement, or manage solutions.",
            "about": "A Ecologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Ecologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "astrobiologist",
            "name": "Astrobiologist",
            "interest_tags": [
                "Space Science"
            ],
            "short_description": "Studies the origin, evolution, distribution, and future of life in the universe, including searching for extraterrestrial life.",
            "about": "Astrobiologists study how life starts on Earth to understand how it could survive on other planets. It is highly interdisciplinary, combining biology, chemistry, geology, and physics. You'll analyze soil samples from extreme environments (like hot springs or Antarctica), design space mission search parameters, or study Mars rover telemetry data.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB) or PCM.",
                "Clear IIST Admission Test or CUET-UG.",
                "B.Sc. in Biology, Chemistry, Physics, or Geology (3 years).",
                "M.Sc. in Astrobiology or space sciences (2 years).",
                "Ph.D. in specialized science to secure research positions."
            ],
            "entrance_exams": [
                "IIST-Admission",
                "NEET",
                "SAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Moderate growth, highly selective niche",
            "colleges": [
                {
                    "name": "Indian Institute of Space Science and Technology (IIST), Thiruvananthapuram",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iist.ac.in/",
                    "short_description": "Asia's first space university, sponsored by ISRO.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "IISER Pune, Pune",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iiserpune.ac.in/",
                    "short_description": "Premier science education and research institute.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Indian Institute of Science (IISc), Bengaluru",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://iisc.ac.in/",
                    "short_description": "India's highest-ranked institution for advanced scientific research.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Arizona State University, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.asu.edu/",
                    "short_description": "Hosts the pioneering ASU Astrobiology initiative.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "aerospace-research-scientist",
            "name": "Aerospace Research Scientist",
            "interest_tags": [
                "Space Science"
            ],
            "short_description": "Professional role working in the field of Aerospace Research Scientist to design, implement, or manage solutions.",
            "about": "A Aerospace Research Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Aerospace Research Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "statistician",
            "name": "Statistician",
            "interest_tags": [
                "Mathematics & Statistics"
            ],
            "short_description": "Professional role working in the field of Statistician to design, implement, or manage solutions.",
            "about": "A Statistician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Statistician."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "applied-mathematician",
            "name": "Applied Mathematician",
            "interest_tags": [
                "Mathematics & Statistics"
            ],
            "short_description": "Professional role working in the field of Applied Mathematician to design, implement, or manage solutions.",
            "about": "A Applied Mathematician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Applied Mathematician."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "forensic-scientist",
            "name": "Forensic Scientist",
            "interest_tags": [
                "Applied & Forensic Science"
            ],
            "short_description": "Analyzes crime scene evidence, DNA profiles, fingerprints, and toxic compounds to assist legal investigations.",
            "about": "Forensic Scientists study physical evidence (hair, fingerprints, bullet casings) in crime labs. You will run spectroscopy, write evidence summaries, and testify in law courts.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, Biology/Math.",
                "B.Sc. in Forensic Science (3 years).",
                "M.Sc. in Forensic Science / Toxicology (2 years).",
                "Join government forensic labs or state policing units."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3.5–9 LPA",
            "growth_outlook": "Stable demand, linked to modern policing and state crime labs",
            "colleges": [
                {
                    "name": "Indian Institute of Forensic Scientist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Forensic Scientist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Forensic Scientist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Forensic Scientist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "patent-examiner",
            "name": "Patent Examiner",
            "interest_tags": [
                "Applied & Forensic Science"
            ],
            "short_description": "Professional role working in the field of Patent Examiner to design, implement, or manage solutions.",
            "about": "A Patent Examiner applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Patent Examiner."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "science-communicator-journalist",
            "name": "Science Communicator/Journalist",
            "interest_tags": [
                "Science Communication"
            ],
            "short_description": "Professional role working in the field of Science Communicator/Journalist to design, implement, or manage solutions.",
            "about": "A Science Communicator/Journalist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Science Communicator/Journalist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "research-lab-technician",
            "name": "Research Lab Technician",
            "interest_tags": [
                "Science Communication"
            ],
            "short_description": "Professional role working in the field of Research Lab Technician to design, implement, or manage solutions.",
            "about": "A Research Lab Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Research Lab Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "science-policy-analyst",
            "name": "Science Policy Analyst",
            "interest_tags": [
                "Science Communication"
            ],
            "short_description": "Professional role working in the field of Science Policy Analyst to design, implement, or manage solutions.",
            "about": "A Science Policy Analyst applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCM for physical/earth sciences, PCB for biological/chemical sciences).",
                "Clear national admissions exams like CUET-UG, NEST, or JEE Main.",
                "Obtain a B.Sc. or Integrated BS-MS degree in the targeted scientific discipline (3-5 years).",
                "Complete a Master's degree (M.Sc. or MS) in your specialized field of study (2 years).",
                "Clear national eligibility tests (like CSIR-NET or GATE) to secure junior research fellowships (JRF).",
                "Complete a Ph.D. program, publish research in peer-reviewed journals, and pursue post-doctoral fellowships to work as Science Policy Analyst."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Business, Finance & Economics": [
        {
            "id": "chartered-accountant",
            "name": "Chartered Accountant",
            "interest_tags": [
                "Accounting & Auditing"
            ],
            "short_description": "Manages corporate audit records, verifies tax compliances, and advises on business financial structures.",
            "about": "Chartered Accountants audit financial books, check tax regulations compliance, design corporate accounting systems, and consult on mergers. It is a highly respected, crucial business finance role.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce with Math highly useful).",
                "Register with the Institute of Chartered Accountants of India (ICAI).",
                "Clear CA Foundation, Intermediate, and Final exams.",
                "Complete 2-3 years of practical articleship training under a practicing CA."
            ],
            "entrance_exams": [],
            "salary_range": "₹7–18 LPA",
            "growth_outlook": "Very steady demand across all business sectors",
            "colleges": [
                {
                    "name": "Indian Institute of Chartered Accountant (CA) (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Chartered Accountant (CA).",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Chartered Accountant (CA) (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Chartered Accountant (CA) (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "auditor",
            "name": "Auditor",
            "interest_tags": [
                "Accounting & Auditing"
            ],
            "short_description": "Professional role working in the field of Auditor to design, implement, or manage solutions.",
            "about": "A Auditor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Auditor."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "tax-consultant",
            "name": "Tax Consultant",
            "interest_tags": [
                "Accounting & Auditing"
            ],
            "short_description": "Professional role working in the field of Tax Consultant to design, implement, or manage solutions.",
            "about": "A Tax Consultant applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Tax Consultant."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "cost-accountant",
            "name": "Cost Accountant",
            "interest_tags": [
                "Accounting & Auditing"
            ],
            "short_description": "Professional role working in the field of Cost Accountant to design, implement, or manage solutions.",
            "about": "A Cost Accountant applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Cost Accountant."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "investment-banker",
            "name": "Investment Banker",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Helps corporations, governments, and institutional clients raise capital, value companies, and manage mergers and acquisitions.",
            "about": "Investment Bankers are financial advisory experts. You'll create financial models in Excel, evaluate companies, put together investor pitch decks, and assist companies with IPOs (Initial Public Offerings). It is a high-stakes, fast-paced corporate role that rewards strong analytical skills, resilience, and attention to detail.",
            "educational_roadmap": [
                "Class 12 with Commerce or PCM background.",
                "Clear IPMAT, CUET-UG, or SAT.",
                "B.Com / BBA / B.Sc. in Finance or Economics (3 years).",
                "Clear Chartered Accountant (CA) exams or CFA levels.",
                "Complete MBA in Finance from a premier business school (2 years)."
            ],
            "entrance_exams": [
                "CAT",
                "IPMAT",
                "SAT"
            ],
            "salary_range": "₹8–25 LPA",
            "growth_outlook": "High growth, competitive markets",
            "colleges": [
                {
                    "name": "Shri Ram College of Commerce (SRCC), Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.srcc.edu/",
                    "short_description": "India's highest-ranked commerce college.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Shaheed Sukhdev College of Business Studies (SSCBS), Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://sscbs.du.ac.in/",
                    "short_description": "Premier DU college for business administration and finance.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "London School of Economics (LSE), UK",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.lse.ac.uk/",
                    "short_description": "Global hub for economics and finance studies.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "actuary",
            "name": "Actuary",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Uses statistical models to evaluate the probability of future risk events in insurance, finance, and pension funds.",
            "about": "Actuaries are risk architects. You'll calculate the likelihood of accidents, fires, pandemics, or market crashes, and help insurance companies set premium prices that cover the risk while remaining profitable. It is one of the highest-paying mathematical careers globally.",
            "educational_roadmap": [
                "Class 12 with Mathematics as a core subject.",
                "Clear ACET (Actuarial Common Entrance Test).",
                "Enroll as student member in IAI (India) or IFoA (UK).",
                "Clear 13-15 professional examinations while completing B.Sc. or B.Com.",
                "Obtain fellowship status to practice as a certified Actuary."
            ],
            "entrance_exams": [
                "ACET",
                "CUET-UG"
            ],
            "salary_range": "₹7–20 LPA",
            "growth_outlook": "High growth, low competition due to high certification standards",
            "colleges": [
                {
                    "name": "Institute of Actuaries of India (IAI), Mumbai",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "http://www.actuariesindia.org/",
                    "short_description": "The statutory body governing actuarial practice and exams in India.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Amity University, Noida",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.amity.edu/",
                    "short_description": "Offers structured B.Sc. courses in Actuarial Science.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "University of Waterloo, Canada",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://uwaterloo.ca/",
                    "short_description": "World-class co-op program in actuarial science.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "stock-broker-trader",
            "name": "Stock Broker/Trader",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Professional role working in the field of Stock Broker/Trader to design, implement, or manage solutions.",
            "about": "A Stock Broker/Trader applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Stock Broker/Trader."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "insurance-underwriter",
            "name": "Insurance Underwriter",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Professional role working in the field of Insurance Underwriter to design, implement, or manage solutions.",
            "about": "A Insurance Underwriter applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Insurance Underwriter."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "credit-analyst",
            "name": "Credit Analyst",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Professional role working in the field of Credit Analyst to design, implement, or manage solutions.",
            "about": "A Credit Analyst applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Credit Analyst."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "venture-capital-analyst",
            "name": "Venture Capital Analyst",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Evaluates startup business models, market sizes, and teams to identify promising companies for investment.",
            "about": "Venture Capital Analysts work for VC firms, identifying early-stage startups to fund. You will conduct market research, perform financial due diligence, meet with founders, and help manage portfolio company relationships.",
            "educational_roadmap": [
                "Class 12 Commerce or Science.",
                "BBA / B.Com / B.Tech from a premier institute.",
                "Gain experience in investment banking, startup operations, or consulting."
            ],
            "entrance_exams": [
                "CAT",
                "IPMAT"
            ],
            "salary_range": "₹8–18 LPA",
            "growth_outlook": "High growth, linked to the startup ecosystem",
            "colleges": [
                {
                    "name": "Indian Institute of Venture Capital (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Venture Capital.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Venture Capital (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Venture Capital (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "financial-planner-advisor",
            "name": "Financial Planner/Advisor",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Professional role working in the field of Financial Planner/Advisor to design, implement, or manage solutions.",
            "about": "A Financial Planner/Advisor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Financial Planner/Advisor."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "portfolio-manager",
            "name": "Portfolio Manager",
            "interest_tags": [
                "Finance & Investment"
            ],
            "short_description": "Professional role working in the field of Portfolio Manager to design, implement, or manage solutions.",
            "about": "A Portfolio Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Portfolio Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "business-analyst",
            "name": "Business Analyst",
            "interest_tags": [
                "Strategy & Consulting"
            ],
            "short_description": "Analyzes business workflows, documents software requirements, and aligns tech updates with corporate strategy.",
            "about": "Business Analysts evaluate corporate operations, write database queries to identify workflow bottlenecks, outline software specifications, and coordinate developers and executives.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "B.Com, BBA, or B.Tech (3-4 years).",
                "Learn business modeling and requirements tracking tools.",
                "Join IT consulting firms, corporate banks, or startup panels."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "High demand in IT services and enterprise consulting",
            "colleges": [
                {
                    "name": "Indian Institute of Business Analyst (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Business Analyst.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Business Analyst (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Business Analyst (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "management-consultant",
            "name": "Management Consultant",
            "interest_tags": [
                "Strategy & Consulting"
            ],
            "short_description": "Professional role working in the field of Management Consultant to design, implement, or manage solutions.",
            "about": "A Management Consultant applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Management Consultant."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "economist",
            "name": "Economist",
            "interest_tags": [
                "Strategy & Consulting"
            ],
            "short_description": "Studies the production and distribution of resources, analyzes inflation rates, and advises on monetary policy.",
            "about": "Economists evaluate market trends, write research briefs on interest rates, analyze tariff impacts, and model consumer demand cycles for banks and government units.",
            "educational_roadmap": [
                "Class 12 with Commerce/Humanities (Math is compulsory).",
                "B.Sc. or B.A. in Economics (3 years).",
                "M.Sc. in Economics or Applied Econometrics (2 years).",
                "Join corporate research banks, public policy consultancies, or government planning units."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹5–14 LPA",
            "growth_outlook": "Steady demand, critical role for policy planning",
            "colleges": [
                {
                    "name": "Indian Institute of Economist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Economist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Economist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Economist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "strategy-consultant",
            "name": "Strategy Consultant",
            "interest_tags": [
                "Strategy & Consulting"
            ],
            "short_description": "Professional role working in the field of Strategy Consultant to design, implement, or manage solutions.",
            "about": "A Strategy Consultant applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Strategy Consultant."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "marketing-manager",
            "name": "Marketing Manager",
            "interest_tags": [
                "Marketing & Growth"
            ],
            "short_description": "Coordinates brand marketing budgets, plans advertising timelines, and manages customer acquisition panels.",
            "about": "Marketing Managers lead advertising squads, design social branding cycles, analyze user feedback patterns, and track customer conversion indicators.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "BBA, B.Com, or B.A. in Mass Communication (3 years).",
                "MBA in Marketing Management (2 years).",
                "Join consumer goods companies, tech startups, or advertising agencies."
            ],
            "entrance_exams": [
                "CUET-UG",
                "CAT"
            ],
            "salary_range": "₹5–15 LPA",
            "growth_outlook": "Steady demand, critical growth driver for brands",
            "colleges": [
                {
                    "name": "Indian Institute of Brand Marketing Manager (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Brand Marketing Manager.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Brand Marketing Manager (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Brand Marketing Manager (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "brand-manager",
            "name": "Brand Manager",
            "interest_tags": [
                "Marketing & Growth"
            ],
            "short_description": "Shapes and preserves a brand's public image, product placements, and marketing narratives to drive consumer loyalty.",
            "about": "Brand Managers coordinate advertising budgets, run packaging redesigns, design campaign launches, and track consumer perception indicators to grow brand value.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce preferred).",
                "BBA, B.Com, or Bachelor of Mass Media (3 years).",
                "Complete MBA in Marketing from a top-tier business school (2 years)."
            ],
            "entrance_exams": [
                "CAT",
                "IPMAT"
            ],
            "salary_range": "₹6–16 LPA",
            "growth_outlook": "Steady demand, highly competitive",
            "colleges": [
                {
                    "name": "Indian Institute of Brand Management (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Brand Management.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Brand Management (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Brand Management (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "e-commerce-manager",
            "name": "E-commerce Manager",
            "interest_tags": [
                "Marketing & Growth"
            ],
            "short_description": "Professional role working in the field of E-commerce Manager to design, implement, or manage solutions.",
            "about": "A E-commerce Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified E-commerce Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "digital-marketing-specialist",
            "name": "Digital Marketing Specialist",
            "interest_tags": [
                "Marketing & Growth"
            ],
            "short_description": "Professional role working in the field of Digital Marketing Specialist to design, implement, or manage solutions.",
            "about": "A Digital Marketing Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Digital Marketing Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "market-research-analyst",
            "name": "Market Research Analyst",
            "interest_tags": [
                "Marketing & Growth"
            ],
            "short_description": "Professional role working in the field of Market Research Analyst to design, implement, or manage solutions.",
            "about": "A Market Research Analyst applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Market Research Analyst."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "human-resources-manager",
            "name": "Human Resources Manager",
            "interest_tags": [
                "Operations & People"
            ],
            "short_description": "Professional role working in the field of Human Resources Manager to design, implement, or manage solutions.",
            "about": "A Human Resources Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Human Resources Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "operations-manager",
            "name": "Operations Manager",
            "interest_tags": [
                "Operations & People"
            ],
            "short_description": "Professional role working in the field of Operations Manager to design, implement, or manage solutions.",
            "about": "A Operations Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Operations Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "supply-chain-manager",
            "name": "Supply Chain Manager",
            "interest_tags": [
                "Operations & People"
            ],
            "short_description": "Professional role working in the field of Supply Chain Manager to design, implement, or manage solutions.",
            "about": "A Supply Chain Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Supply Chain Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "logistics-manager",
            "name": "Logistics Manager",
            "interest_tags": [
                "Operations & People"
            ],
            "short_description": "Professional role working in the field of Logistics Manager to design, implement, or manage solutions.",
            "about": "A Logistics Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Logistics Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "entrepreneur",
            "name": "Entrepreneur/Startup Founder",
            "interest_tags": [
                "Entrepreneurship & Trade"
            ],
            "short_description": "Designs a unique business model, secures seed funding, builds team squads, and manages startup sales.",
            "about": "Entrepreneurs identify market gaps, design prototypes, pitch pitches to venture capitalists, organize team budgets, and manage startup growth.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "Complete BBA, B.Com, or B.Tech (useful but optional; hands-on skill is key).",
                "Launch prototype products and participate in startup incubator programs."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–30 LPA",
            "growth_outlook": "High risk, high potential growth in tech ecosystem",
            "colleges": [
                {
                    "name": "Indian Institute of Entrepreneur / Startup Founder (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Entrepreneur / Startup Founder.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Entrepreneur / Startup Founder (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Entrepreneur / Startup Founder (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "import-export-trade-specialist",
            "name": "Import-Export Trade Specialist",
            "interest_tags": [
                "Entrepreneurship & Trade"
            ],
            "short_description": "Professional role working in the field of Import-Export Trade Specialist to design, implement, or manage solutions.",
            "about": "A Import-Export Trade Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Mathematics background highly recommended).",
                "Clear entrance exams like CUET-UG, IPMAT, or prepare for CA/CFA foundation exams.",
                "Obtain B.Com, BBA, B.A. Economics, or B.Sc. Finance (3 years).",
                "Pursue professional certifications (e.g., Chartered Accountancy (ICAI), CFA, FRM, or a specialized MBA).",
                "Complete corporate internships, article training, or financial analysis workshops (1-3 years).",
                "Acquire client consulting or junior analyst experience to enter firms as a certified Import-Export Trade Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Social Sciences & Humanities": [
        {
            "id": "psychologist",
            "name": "Psychologist",
            "interest_tags": [
                "Mind & Behavior"
            ],
            "short_description": "Studies cognitive, emotional, and social behaviors and provides counseling therapy to improve mental health.",
            "about": "Psychologists analyze human behavior and help individuals navigate mental health issues, relationship challenges, and stress. You can work in private clinics, corporate offices, or educational settings.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities preferred).",
                "B.A. or B.Sc. in Psychology (3 years).",
                "M.A. or M.Sc. in Counseling/Clinical Psychology (2 years).",
                "Optional: M.Phil or PhD for clinical licensing in India."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "Rapidly rising demand due to mental health awareness",
            "colleges": [
                {
                    "name": "Indian Institute of Psychologist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Psychologist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Psychologist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Psychologist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "mental-health-counselor",
            "name": "Mental Health Counselor",
            "interest_tags": [
                "Mind & Behavior"
            ],
            "short_description": "Professional role working in the field of Mental Health Counselor to design, implement, or manage solutions.",
            "about": "A Mental Health Counselor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Mental Health Counselor."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "behavioral-scientist",
            "name": "Behavioral Scientist",
            "interest_tags": [
                "Mind & Behavior"
            ],
            "short_description": "Professional role working in the field of Behavioral Scientist to design, implement, or manage solutions.",
            "about": "A Behavioral Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Behavioral Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sociologist",
            "name": "Sociologist",
            "interest_tags": [
                "Society & Culture"
            ],
            "short_description": "Studies human society, social relationships, class structures, and cultural behaviors in communities.",
            "about": "Sociologists analyze demographic shifts, study family dynamics, write research reports on social inequality, and advise NGOs and policy think tanks.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities preferred).",
                "B.A. in Sociology (3 years).",
                "M.A. and Ph.D. in Sociology (2-5 years).",
                "Join social research institutes, NGOs, or policy think-tanks."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3.5–8 LPA",
            "growth_outlook": "Stable, research-driven funding",
            "colleges": [
                {
                    "name": "Indian Institute of Sociologist & Social Researcher (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Sociologist & Social Researcher.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Sociologist & Social Researcher (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Sociologist & Social Researcher (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "anthropologist",
            "name": "Anthropologist",
            "interest_tags": [
                "Society & Culture"
            ],
            "short_description": "Professional role working in the field of Anthropologist to design, implement, or manage solutions.",
            "about": "A Anthropologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Anthropologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "historian",
            "name": "Historian",
            "interest_tags": [
                "Society & Culture"
            ],
            "short_description": "Researches, analyzes, and interprets the past through historical records, manuscripts, and archives.",
            "about": "Historians write books, teach in universities, consult for museums and archeological sites, and verify historical documents.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities preferred).",
                "B.A. in History (3 years).",
                "M.A. and Ph.D. in History (2-5 years).",
                "Join heritage agencies, museums, or universities as professor."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Niche academic sector, stable research pathways",
            "colleges": [
                {
                    "name": "Indian Institute of Historian & Academic Researcher (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Historian & Academic Researcher.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Historian & Academic Researcher (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Historian & Academic Researcher (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "archaeologist",
            "name": "Archaeologist",
            "interest_tags": [
                "Society & Culture"
            ],
            "short_description": "Professional role working in the field of Archaeologist to design, implement, or manage solutions.",
            "about": "A Archaeologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Archaeologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "journalist",
            "name": "Journalist",
            "interest_tags": [
                "Media & Communication"
            ],
            "short_description": "Gathers information, conducts interviews, and writes news articles or broadcasts media reports.",
            "about": "Journalists report on public affairs, investigate crime stories, interview politicians, write column briefs, and host visual media broadcasts.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "B.A. in Journalism & Mass Communication or English (3 years).",
                "Build a portfolio writing for student newspapers or local web blogs.",
                "Join news channels, digital media platforms, or work as freelance reporter."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "Stable demand, expanding rapidly in digital media channels",
            "colleges": [
                {
                    "name": "Indian Institute of Journalist / News Reporter (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Journalist / News Reporter.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Journalist / News Reporter (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Journalist / News Reporter (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "content-writer-editor",
            "name": "Content Writer/Editor",
            "interest_tags": [
                "Media & Communication"
            ],
            "short_description": "Professional role working in the field of Content Writer/Editor to design, implement, or manage solutions.",
            "about": "A Content Writer/Editor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Content Writer/Editor."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "translator-interpreter",
            "name": "Translator/Interpreter",
            "interest_tags": [
                "Media & Communication"
            ],
            "short_description": "Professional role working in the field of Translator/Interpreter to design, implement, or manage solutions.",
            "about": "A Translator/Interpreter applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Translator/Interpreter."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "public-relations-specialist",
            "name": "Public Relations Specialist",
            "interest_tags": [
                "Media & Communication"
            ],
            "short_description": "Professional role working in the field of Public Relations Specialist to design, implement, or manage solutions.",
            "about": "A Public Relations Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Public Relations Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "political-scientist",
            "name": "Political Scientist",
            "interest_tags": [
                "Governance & Policy"
            ],
            "short_description": "Studies government structures, voting patterns, public policies, and political theories.",
            "about": "Political Scientists analyze political campaigns, write briefs on foreign relations, forecast election results, and teach political science.",
            "educational_roadmap": [
                "Class 12 in Humanities/Arts.",
                "B.A. in Political Science (3 years).",
                "M.A. and Ph.D. in Political Science or International Relations (2-5 years).",
                "Join polling organizations, embassies, think-tanks, or academic boards."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Steady demand, critical role in policy consultancies",
            "colleges": [
                {
                    "name": "Indian Institute of Political Scientist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Political Scientist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Political Scientist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Political Scientist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "public-policy-analyst",
            "name": "Public Policy Analyst",
            "interest_tags": [
                "Governance & Policy"
            ],
            "short_description": "Researches, evaluates, and shapes government laws and community programs to resolve societal issues.",
            "about": "Public Policy Analysts look at complex issues like education quality, healthcare access, or urban traffic. You'll collect demographic data, write research briefs, evaluate if current government welfare schemes are working, and recommend improvements. You can work for think-tanks, NGOs, consulting firms, or ministries.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Commerce preferred).",
                "Clear CUET-UG or SAT.",
                "B.A. in Political Science, Economics, or Sociology (3 years).",
                "Master of Public Policy (MPP) or Master of Public Administration (MPA) (2 years).",
                "Join a think-tank, consultancy, or NGO as a policy researcher."
            ],
            "entrance_exams": [
                "CUET-UG",
                "SAT"
            ],
            "salary_range": "₹5–13 LPA",
            "growth_outlook": "Growing role in corporate consulting and government advisory",
            "colleges": [
                {
                    "name": "National Law School of India University (NLSIU), Bengaluru",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.nls.ac.in/",
                    "short_description": "Hosts a highly reputed Master of Public Policy (MPP) program.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Azim Premji University, Bengaluru",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://azimpremjiuniversity.edu.in/",
                    "short_description": "Pioneering private university focused on public policy and education.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Harvard Kennedy School, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.hks.harvard.edu/",
                    "short_description": "Global gold standard for public policy and administrative training.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "human-rights-researcher",
            "name": "Human Rights Researcher",
            "interest_tags": [
                "Governance & Policy"
            ],
            "short_description": "Professional role working in the field of Human Rights Researcher to design, implement, or manage solutions.",
            "about": "A Human Rights Researcher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Human Rights Researcher."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "educator-teacher",
            "name": "Educator/Teacher",
            "interest_tags": [
                "Education & Knowledge"
            ],
            "short_description": "Professional role working in the field of Educator/Teacher to design, implement, or manage solutions.",
            "about": "A Educator/Teacher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Educator/Teacher."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "librarian",
            "name": "Librarian",
            "interest_tags": [
                "Education & Knowledge"
            ],
            "short_description": "Professional role working in the field of Librarian to design, implement, or manage solutions.",
            "about": "A Librarian applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Librarian."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "archivist-museum-curator",
            "name": "Archivist/Museum Curator",
            "interest_tags": [
                "Education & Knowledge"
            ],
            "short_description": "Professional role working in the field of Archivist/Museum Curator to design, implement, or manage solutions.",
            "about": "A Archivist/Museum Curator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Archivist/Museum Curator."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "linguist",
            "name": "Linguist",
            "interest_tags": [
                "Education & Knowledge"
            ],
            "short_description": "Studies the structure, development, syntax, and meaning of human languages, often assisting AI speech engines.",
            "about": "Linguists analyze grammar structures, translate ancient texts, consult on language policies, and design Natural Language Processing (NLP) models.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "B.A. in Linguistics or English/Foreign Languages (3 years).",
                "M.A. in Applied Linguistics or Computational Linguistics (2 years).",
                "Join technology companies for AI training or academic setups."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–12 LPA",
            "growth_outlook": "Rising growth, driven by computational linguistics and NLP products",
            "colleges": [
                {
                    "name": "Indian Institute of Linguist & Language Specialist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Linguist & Language Specialist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Linguist & Language Specialist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Linguist & Language Specialist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "academic-researcher",
            "name": "Academic Researcher",
            "interest_tags": [
                "Education & Knowledge"
            ],
            "short_description": "Professional role working in the field of Academic Researcher to design, implement, or manage solutions.",
            "about": "A Academic Researcher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Academic Researcher."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "social-worker",
            "name": "Social Worker",
            "interest_tags": [
                "Social Impact"
            ],
            "short_description": "Professional role working in the field of Social Worker to design, implement, or manage solutions.",
            "about": "A Social Worker applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Social Worker."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "ngo-program-manager",
            "name": "NGO Program Manager",
            "interest_tags": [
                "Social Impact"
            ],
            "short_description": "Professional role working in the field of NGO Program Manager to design, implement, or manage solutions.",
            "about": "A NGO Program Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in NGO Program Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "community-development-officer",
            "name": "Community Development Officer",
            "interest_tags": [
                "Social Impact"
            ],
            "short_description": "Professional role working in the field of Community Development Officer to design, implement, or manage solutions.",
            "about": "A Community Development Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Community Development Officer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "philosopher-ethicist-academic",
            "name": "Philosopher/Ethicist (Academic)",
            "interest_tags": [
                "Philosophy & Ethics"
            ],
            "short_description": "Professional role working in the field of Philosopher/Ethicist (Academic) to design, implement, or manage solutions.",
            "about": "A Philosopher/Ethicist (Academic) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (Humanities/Arts preferred).",
                "Clear university admissions tests such as CUET-UG.",
                "Complete B.A. or B.Sc. in Psychology, Sociology, History, Journalism, or Political Science (3 years).",
                "Complete a Master's degree (M.A. or M.Sc.) in your chosen specialty or public policy (2 years).",
                "Build a professional portfolio (write columns, compile community logs, or complete museum/NGO internships).",
                "Enter the sector as a researcher, counselor, journalist, or public policy consultant in Philosopher/Ethicist (Academic)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Vocational / Skilled Trades": [
        {
            "id": "electrician",
            "name": "Electrician",
            "interest_tags": [
                "Electrical & Electronics"
            ],
            "short_description": "Professional role working in the field of Electrician to design, implement, or manage solutions.",
            "about": "A Electrician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Electrician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "industrial-electrician",
            "name": "Industrial Electrician",
            "interest_tags": [
                "Electrical & Electronics"
            ],
            "short_description": "Professional role working in the field of Industrial Electrician to design, implement, or manage solutions.",
            "about": "A Industrial Electrician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Industrial Electrician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "solar-panel-installer-technician",
            "name": "Solar Panel Installer/Technician",
            "interest_tags": [
                "Electrical & Electronics"
            ],
            "short_description": "Professional role working in the field of Solar Panel Installer/Technician to design, implement, or manage solutions.",
            "about": "A Solar Panel Installer/Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Solar Panel Installer/Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "electronics-repair-technician",
            "name": "Electronics Repair Technician",
            "interest_tags": [
                "Electrical & Electronics"
            ],
            "short_description": "Professional role working in the field of Electronics Repair Technician to design, implement, or manage solutions.",
            "about": "A Electronics Repair Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Electronics Repair Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "automotive-technician-mechanic",
            "name": "Automotive Technician/Mechanic",
            "interest_tags": [
                "Mechanical & Automotive"
            ],
            "short_description": "Professional role working in the field of Automotive Technician/Mechanic to design, implement, or manage solutions.",
            "about": "A Automotive Technician/Mechanic applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Automotive Technician/Mechanic."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "diesel-mechanic",
            "name": "Diesel Mechanic",
            "interest_tags": [
                "Mechanical & Automotive"
            ],
            "short_description": "Professional role working in the field of Diesel Mechanic to design, implement, or manage solutions.",
            "about": "A Diesel Mechanic applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Diesel Mechanic."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "cnc-machine-operator",
            "name": "CNC Machine Operator",
            "interest_tags": [
                "Mechanical & Automotive"
            ],
            "short_description": "Professional role working in the field of CNC Machine Operator to design, implement, or manage solutions.",
            "about": "A CNC Machine Operator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for CNC Machine Operator."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "tool-and-die-maker",
            "name": "Tool & Die Maker",
            "interest_tags": [
                "Mechanical & Automotive"
            ],
            "short_description": "Professional role working in the field of Tool & Die Maker to design, implement, or manage solutions.",
            "about": "A Tool & Die Maker applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Tool & Die Maker."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "heavy-equipment-operator",
            "name": "Heavy Equipment Operator",
            "interest_tags": [
                "Mechanical & Automotive"
            ],
            "short_description": "Operates heavy machinery like excavators, bulldozers, and tower cranes at mining and construction sites.",
            "about": "Operators control hydraulic machinery, monitor load limits, clear land areas, and coordinates excavation depths with site engineers.",
            "educational_roadmap": [
                "Class 12 pass.",
                "Complete a Heavy Motor Vehicle (HMV) license and training certificate course (1 year)."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–8 LPA",
            "growth_outlook": "Steady demand, driven by government highway projects",
            "colleges": [
                {
                    "name": "Indian Institute of Heavy Machinery Operation (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Heavy Machinery Operation.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Heavy Machinery Operation (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Heavy Machinery Operation (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "plumber",
            "name": "Plumber",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of Plumber to design, implement, or manage solutions.",
            "about": "A Plumber applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Plumber."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "carpenter",
            "name": "Carpenter",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of Carpenter to design, implement, or manage solutions.",
            "about": "A Carpenter applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Carpenter."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "welder",
            "name": "Welder",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of Welder to design, implement, or manage solutions.",
            "about": "A Welder applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Welder."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "mason-construction-supervisor",
            "name": "Mason/Construction Supervisor",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of Mason/Construction Supervisor to design, implement, or manage solutions.",
            "about": "A Mason/Construction Supervisor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Mason/Construction Supervisor."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "hvac-technician",
            "name": "HVAC Technician",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of HVAC Technician to design, implement, or manage solutions.",
            "about": "A HVAC Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for HVAC Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "refrigeration-and-ac-technician",
            "name": "Refrigeration & AC Technician",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of Refrigeration & AC Technician to design, implement, or manage solutions.",
            "about": "A Refrigeration & AC Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Refrigeration & AC Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "painter-decorator",
            "name": "Painter/Decorator",
            "interest_tags": [
                "Construction & Building"
            ],
            "short_description": "Professional role working in the field of Painter/Decorator to design, implement, or manage solutions.",
            "about": "A Painter/Decorator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Painter/Decorator."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "tailor-fashion-designer-vocational-track",
            "name": "Tailor/Fashion Designer (vocational track)",
            "interest_tags": [
                "Personal Care & Craft"
            ],
            "short_description": "Professional role working in the field of Tailor/Fashion Designer (vocational track) to design, implement, or manage solutions.",
            "about": "A Tailor/Fashion Designer (vocational track) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Tailor/Fashion Designer (vocational track)."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "beautician-cosmetologist",
            "name": "Beautician/Cosmetologist",
            "interest_tags": [
                "Personal Care & Craft"
            ],
            "short_description": "Professional role working in the field of Beautician/Cosmetologist to design, implement, or manage solutions.",
            "about": "A Beautician/Cosmetologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Beautician/Cosmetologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "jewelry-designer",
            "name": "Jewelry Designer/Goldsmith",
            "interest_tags": [
                "Personal Care & Craft"
            ],
            "short_description": "Designs jewelry, casts precious metals, sets gems, and polishes finished jewelry products.",
            "about": "Goldsmiths sketch layouts on CAD, melt gold/silver, weld joints, set diamonds and rubies, and restore antique jewelry items.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "Diploma in Jewelry Design & Gemology (1-2 years).",
                "Gain experience as apprentice in jewelry production units."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–10 LPA",
            "growth_outlook": "Stable growth, luxury designer demand is rising",
            "colleges": [
                {
                    "name": "Indian Institute of Jewelry Design (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Jewelry Design.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Jewelry Design (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Jewelry Design (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "bakery-pastry-chef",
            "name": "Bakery/Pastry Chef",
            "interest_tags": [
                "Food Production"
            ],
            "short_description": "Professional role working in the field of Bakery/Pastry Chef to design, implement, or manage solutions.",
            "about": "A Bakery/Pastry Chef applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Bakery/Pastry Chef."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "food-processing-technician",
            "name": "Food Processing Technician",
            "interest_tags": [
                "Food Production"
            ],
            "short_description": "Professional role working in the field of Food Processing Technician to design, implement, or manage solutions.",
            "about": "A Food Processing Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Food Processing Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "printing-technician",
            "name": "Printing Technician",
            "interest_tags": [
                "Printing & Manufacturing"
            ],
            "short_description": "Professional role working in the field of Printing Technician to design, implement, or manage solutions.",
            "about": "A Printing Technician applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Printing Technician."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "machine-tool-operator",
            "name": "Machine Tool Operator",
            "interest_tags": [
                "Printing & Manufacturing"
            ],
            "short_description": "Professional role working in the field of Machine Tool Operator to design, implement, or manage solutions.",
            "about": "A Machine Tool Operator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 10 or Class 12 in any stream.",
                "Enroll in a government-recognized Industrial Training Institute (ITI) for the specific trade (1-2 years).",
                "Complete a National Apprenticeship Certificate (NAC) training program in an engineering yard or assembly floor (1-2 years).",
                "Acquire industrial safety certifications and specialized machine handling experience.",
                "Start working as a certified tradesman/technician, or establish a specialized local service firm for Machine Tool Operator."
            ],
            "entrance_exams": [],
            "salary_range": "₹2.5–6 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Defense & Civil Services": [
        {
            "id": "army-officer",
            "name": "Army Officer",
            "interest_tags": [
                "Armed Forces"
            ],
            "short_description": "Leads military platoons, coordinates defense strategy, and handles combat operations in the Indian Army.",
            "about": "Army Officers command squads, oversee tactical strategies, operate high-tech weapons, lead border security, and assist civil administrations during emergency scenarios.",
            "educational_roadmap": [
                "Class 12 in any stream (open to all; PCM required for technical wings).",
                "Clear NDA Entrance Exam (written).",
                "Clear the Service Selection Board (SSB) interviews and medical tests.",
                "Undergo 3 years training at NDA (Khadakwasla) followed by 1 year at IMA (Dehradun)."
            ],
            "entrance_exams": [
                "NDA-Exam"
            ],
            "salary_range": "₹8–18 LPA",
            "growth_outlook": "Highly prestigious, stable public service career",
            "colleges": [
                {
                    "name": "Indian Institute of Defense Studies (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Defense Studies.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Defense Studies (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Defense Studies (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "navy-officer",
            "name": "Navy Officer",
            "interest_tags": [
                "Armed Forces"
            ],
            "short_description": "Commands warship divisions, coordinates naval strategy, and manages sea operations in the Indian Navy.",
            "about": "Navy Officers manage warship propulsion, steer logistics, run maritime patrols, coordinate anti-piracy operations, and direct search and rescue services.",
            "educational_roadmap": [
                "Class 12 with Physics and Mathematics (PCM) background.",
                "Clear NDA Entrance Exam.",
                "Pass SSB interviews and naval medical checks.",
                "Complete 4 years training at NDA and Indian Naval Academy (Ezhimala)."
            ],
            "entrance_exams": [
                "NDA-Exam"
            ],
            "salary_range": "₹8–18 LPA",
            "growth_outlook": "Prestigious government role, excellent service benefits",
            "colleges": [
                {
                    "name": "Indian Institute of Naval Operations (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Naval Operations.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Naval Operations (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Naval Operations (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "air-force-officer-pilot",
            "name": "Air Force Officer (Pilot)",
            "interest_tags": [
                "Armed Forces"
            ],
            "short_description": "Professional role working in the field of Air Force Officer (Pilot) to design, implement, or manage solutions.",
            "about": "A Air Force Officer (Pilot) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Air Force Officer (Pilot)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "air-force-officer-technical",
            "name": "Air Force Officer (Technical)",
            "interest_tags": [
                "Armed Forces"
            ],
            "short_description": "Professional role working in the field of Air Force Officer (Technical) to design, implement, or manage solutions.",
            "about": "A Air Force Officer (Technical) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Air Force Officer (Technical)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "coast-guard-officer",
            "name": "Coast Guard Officer",
            "interest_tags": [
                "Coast & Border Security"
            ],
            "short_description": "Protects maritime zones, prevents smuggling, and ensures coastal security in territorial waters.",
            "about": "Coast Guard Officers run high-speed interceptor boats, audit shipping logs, combat marine pollution, and rescue stranded fishermen.",
            "educational_roadmap": [
                "Class 12 with Physics and Mathematics.",
                "Complete a Bachelor's degree in any science or engineering subject.",
                "Clear the Coast Guard Assistant Commandant Selection Test and SSB."
            ],
            "entrance_exams": [],
            "salary_range": "₹7–15 LPA",
            "growth_outlook": "Stable government career, expanding coastal defense",
            "colleges": [
                {
                    "name": "Indian Institute of Coast Guard Studies (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Coast Guard Studies.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Coast Guard Studies (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Coast Guard Studies (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "bsf-officer",
            "name": "Border Security Force Officer",
            "interest_tags": [
                "Coast & Border Security"
            ],
            "short_description": "Commands border outposts, checks illegal cross-border infiltration, and guards national borders.",
            "about": "BSF Officers lead border patrols, prevent smuggling, manage border fencing gates, and coordinate with local border intelligence bureaus.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Complete any Bachelor's degree.",
                "Clear the UPSC Central Armed Police Forces (CAPF) Assistant Commandant exam."
            ],
            "entrance_exams": [],
            "salary_range": "₹7–15 LPA",
            "growth_outlook": "Stable government service pathways",
            "colleges": [
                {
                    "name": "Indian Institute of Border Security (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Border Security.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Border Security (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Border Security (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "paramilitary-forces-officer-crpf-cisf-etc",
            "name": "Paramilitary Forces Officer (CRPF/CISF/etc.)",
            "interest_tags": [
                "Coast & Border Security"
            ],
            "short_description": "Professional role working in the field of Paramilitary Forces Officer (CRPF/CISF/etc.) to design, implement, or manage solutions.",
            "about": "A Paramilitary Forces Officer (CRPF/CISF/etc.) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Paramilitary Forces Officer (CRPF/CISF/etc.)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "defense-research-engineer-drdo",
            "name": "Defense Research Engineer (DRDO)",
            "interest_tags": [
                "Defense Technology & Intelligence"
            ],
            "short_description": "Professional role working in the field of Defense Research Engineer (DRDO) to design, implement, or manage solutions.",
            "about": "A Defense Research Engineer (DRDO) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Defense Research Engineer (DRDO)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "naval-architect-defense",
            "name": "Naval Architect (Defense)",
            "interest_tags": [
                "Defense Technology & Intelligence"
            ],
            "short_description": "Professional role working in the field of Naval Architect (Defense) to design, implement, or manage solutions.",
            "about": "A Naval Architect (Defense) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Naval Architect (Defense)."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "military-intelligence-officer",
            "name": "Military Intelligence Officer",
            "interest_tags": [
                "Defense Technology & Intelligence"
            ],
            "short_description": "Professional role working in the field of Military Intelligence Officer to design, implement, or manage solutions.",
            "about": "A Military Intelligence Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Military Intelligence Officer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "defense-cybersecurity-specialist",
            "name": "Defense Cybersecurity Specialist",
            "interest_tags": [
                "Defense Technology & Intelligence"
            ],
            "short_description": "Professional role working in the field of Defense Cybersecurity Specialist to design, implement, or manage solutions.",
            "about": "A Defense Cybersecurity Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Defense Cybersecurity Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "defense-estate-officer",
            "name": "Defense Estate Officer",
            "interest_tags": [
                "Defense Support Services"
            ],
            "short_description": "Professional role working in the field of Defense Estate Officer to design, implement, or manage solutions.",
            "about": "A Defense Estate Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Defense Estate Officer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "combat-medic",
            "name": "Combat Medic",
            "interest_tags": [
                "Defense Support Services"
            ],
            "short_description": "Professional role working in the field of Combat Medic to design, implement, or manage solutions.",
            "about": "A Combat Medic applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Combat Medic."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "military-logistics-officer",
            "name": "Military Logistics Officer",
            "interest_tags": [
                "Defense Support Services"
            ],
            "short_description": "Professional role working in the field of Military Logistics Officer to design, implement, or manage solutions.",
            "about": "A Military Logistics Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream (PCM is compulsory for Navy / Air Force technical entries).",
                "Prepare for and clear the National Defence Academy (NDA) or Combined Defence Services (CDS) entrance exams.",
                "Complete officer academic degrees (B.E., B.Sc., B.A.) at NDA or regular universities.",
                "Pass the Services Selection Board (SSB) interview, medical evaluation, and physical fitness rounds.",
                "Complete officer cadet training at IMA, INA, AFA, or OTA.",
                "Commission as a Lieutenant, Sub-Lieutenant, or Flying Officer to assume duties as Military Logistics Officer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Government (UPSC/SSC track)": [
        {
            "id": "ias-officer",
            "name": "IAS Officer",
            "interest_tags": [
                "All-India Civil Services"
            ],
            "short_description": "Manages public administration, implements policy decisions, and oversees developmental budgets in government districts.",
            "about": "IAS Officers formulate state policies, manage land revenues, allocate government funds, supervise infrastructure projects, and coordinate relief operations.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Complete any Bachelor's degree (3-4 years).",
                "Prepare for and clear the UPSC Civil Services Exam (Prelims, Mains, Interview).",
                "Complete administrative training at LBSNAA, Mussoorie."
            ],
            "entrance_exams": [
                "UPSC-CSE"
            ],
            "salary_range": "₹7–15 LPA",
            "growth_outlook": "Highly prestigious administrative career",
            "colleges": [
                {
                    "name": "St. Stephen's College, Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.ststephens.edu/",
                    "short_description": "Famous for historic alumni in civil administration.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Presidency University, Kolkata",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.presiuniv.ac.in/web/",
                    "short_description": "Acclaimed heritage university producing civil service officers.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "University of Delhi, New Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "http://du.ac.in/",
                    "short_description": "Hosts multiple colleges offering outstanding UPSC exam preparation support.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "ips-officer",
            "name": "IPS Officer",
            "interest_tags": [
                "All-India Civil Services"
            ],
            "short_description": "Oversees law enforcement, maintains public safety, and directs counter-insurgency policing districts.",
            "about": "IPS Officers command state police departments, direct crime prevention squads, coordinate intelligence alerts, and enforce highway safety codes.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Complete any Bachelor's degree.",
                "Prepare for and clear the UPSC Civil Services Exam.",
                "Complete police training at SVPNPA, Hyderabad."
            ],
            "entrance_exams": [
                "UPSC-CSE"
            ],
            "salary_range": "₹7–15 LPA",
            "growth_outlook": "Highly respected public security role",
            "colleges": [
                {
                    "name": "St. Stephen's College, Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.ststephens.edu/",
                    "short_description": "Famous DU college with civil services legacy.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "St. Xavier's College, Mumbai",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://xaviers.edu/",
                    "short_description": "Top-tier college offering excellent Humanities courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Police Academy, Hyderabad",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.svpnpa.gov.in/",
                    "short_description": "India's premier training center for IPS officers.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "ifs-officer",
            "name": "IFS Officer (Foreign Service)",
            "interest_tags": [
                "All-India Civil Services"
            ],
            "short_description": "Represents the nation's foreign affairs, drafts international trade treaties, and manages embassies globally.",
            "about": "IFS officers manage international relations, lead bilateral summits, analyze foreign media reports, and assist citizens traveling abroad.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Complete any Bachelor's degree.",
                "Clear the UPSC Civil Services Exam.",
                "Complete training at Sushma Swaraj Institute of Foreign Service, Delhi."
            ],
            "entrance_exams": [
                "UPSC-CSE"
            ],
            "salary_range": "₹8–18 LPA",
            "growth_outlook": "Prestigious foreign posting career",
            "colleges": [
                {
                    "name": "Indian Institute of Foreign Policy (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Foreign Policy.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Foreign Policy (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Foreign Policy (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "irs-officer",
            "name": "IRS Officer (Revenue Service)",
            "interest_tags": [
                "All-India Civil Services"
            ],
            "short_description": "Manages direct and indirect tax collections, audited corporate balance sheets, and checks money laundering.",
            "about": "IRS officers head tax commissioners, execute tax audit assessments, lead financial intelligence searches, and draft national tax policies.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce preferred).",
                "Complete any Bachelor's degree.",
                "Clear the UPSC Civil Services Exam."
            ],
            "entrance_exams": [
                "UPSC-CSE"
            ],
            "salary_range": "₹7–15 LPA",
            "growth_outlook": "Secure government administrative career",
            "colleges": [
                {
                    "name": "Indian Institute of Public Finance (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Public Finance.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Public Finance (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Public Finance (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "income-tax-inspector",
            "name": "Income Tax Inspector",
            "interest_tags": [
                "Revenue & Customs"
            ],
            "short_description": "Professional role working in the field of Income Tax Inspector to design, implement, or manage solutions.",
            "about": "A Income Tax Inspector applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Income Tax Inspector."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "customs-and-central-excise-officer",
            "name": "Customs & Central Excise Officer",
            "interest_tags": [
                "Revenue & Customs"
            ],
            "short_description": "Professional role working in the field of Customs & Central Excise Officer to design, implement, or manage solutions.",
            "about": "A Customs & Central Excise Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Customs & Central Excise Officer."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "ssc-cgl-officer-central-govt-group-b-c-roles",
            "name": "SSC CGL Officer (Central Govt Group B/C roles)",
            "interest_tags": [
                "Revenue & Customs"
            ],
            "short_description": "Professional role working in the field of SSC CGL Officer (Central Govt Group B/C roles) to design, implement, or manage solutions.",
            "about": "A SSC CGL Officer (Central Govt Group B/C roles) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for SSC CGL Officer (Central Govt Group B/C roles)."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "railway-officer-rrb-recruited",
            "name": "Railway Officer (RRB-recruited)",
            "interest_tags": [
                "Public Sector & Local Bodies"
            ],
            "short_description": "Professional role working in the field of Railway Officer (RRB-recruited) to design, implement, or manage solutions.",
            "about": "A Railway Officer (RRB-recruited) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Railway Officer (RRB-recruited)."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "postal-service-officer",
            "name": "Postal Service Officer",
            "interest_tags": [
                "Public Sector & Local Bodies"
            ],
            "short_description": "Professional role working in the field of Postal Service Officer to design, implement, or manage solutions.",
            "about": "A Postal Service Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Postal Service Officer."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "municipal-local-government-administrator",
            "name": "Municipal/Local Government Administrator",
            "interest_tags": [
                "Public Sector & Local Bodies"
            ],
            "short_description": "Professional role working in the field of Municipal/Local Government Administrator to design, implement, or manage solutions.",
            "about": "A Municipal/Local Government Administrator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Municipal/Local Government Administrator."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "state-civil-services-officer-state-psc",
            "name": "State Civil Services Officer (State PSC)",
            "interest_tags": [
                "Public Sector & Local Bodies"
            ],
            "short_description": "Professional role working in the field of State Civil Services Officer (State PSC) to design, implement, or manage solutions.",
            "about": "A State Civil Services Officer (State PSC) applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for State Civil Services Officer (State PSC)."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "indian-statistical-service-officer",
            "name": "Indian Statistical Service Officer",
            "interest_tags": [
                "Statistical & Audit Services"
            ],
            "short_description": "Professional role working in the field of Indian Statistical Service Officer to design, implement, or manage solutions.",
            "about": "A Indian Statistical Service Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Indian Statistical Service Officer."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "indian-audit-and-accounts-service-officer",
            "name": "Indian Audit & Accounts Service Officer",
            "interest_tags": [
                "Statistical & Audit Services"
            ],
            "short_description": "Professional role working in the field of Indian Audit & Accounts Service Officer to design, implement, or manage solutions.",
            "about": "A Indian Audit & Accounts Service Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain any Bachelor's degree from a recognized university (3 years).",
                "Prepare for national-level competitive tests (e.g. UPSC Civil Services, SSC CGL, State PSC).",
                "Clear the multi-stage examinations consisting of Prelims, Mains, and Personality Tests.",
                "Undergo executive administrative training at service academies (e.g., LBSNAA, SVPNPA).",
                "Join public departments as a commissioned officer, tax inspector, or administrator for Indian Audit & Accounts Service Officer."
            ],
            "entrance_exams": [
                "SSC-CGL"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Sports & Fitness": [
        {
            "id": "professional-athlete",
            "name": "Professional Athlete",
            "interest_tags": [
                "Competitive Sport"
            ],
            "short_description": "Competes in professional tournaments, maintains peak physical fitness, and represents clubs or the nation.",
            "about": "Professional Athletes undergo rigorous daily training, study opponent tactics, coordinate with nutritionists, and participate in tournaments. It requires immense physical commitment, resilience, and discipline.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "Undergo specialized athletic training at local and state sports academies.",
                "Participate and win in district, state, and national tournaments to gain recruitment."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–25 LPA",
            "growth_outlook": "High risk, short career span but potentially lucrative",
            "colleges": [
                {
                    "name": "Indian Institute of Sports Science (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Sports Science.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Sports Science (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Sports Science (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "esports-player-manager",
            "name": "Esports Player/Manager",
            "interest_tags": [
                "Competitive Sport"
            ],
            "short_description": "Professional role working in the field of Esports Player/Manager to design, implement, or manage solutions.",
            "about": "A Esports Player/Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Esports Player/Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sports-coach",
            "name": "Sports Coach",
            "interest_tags": [
                "Coaching & Training"
            ],
            "short_description": "Instructs athletes in sports rules, coordinates team tactical plays, and monitors physical development.",
            "about": "Coaches analyze game videos, run conditioning drills, coordinate game lineups, and recruit young talent for schools, colleges, and clubs.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "Complete a Bachelor of Physical Education (B.P.Ed) or Diploma in Sports Coaching from NSNIS Patiala (1-3 years)."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "Steady demand in schools, universities, and private clubs",
            "colleges": [
                {
                    "name": "Indian Institute of Sports Coaching (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Sports Coaching.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Sports Coaching (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Sports Coaching (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "personal-fitness-trainer",
            "name": "Personal/Fitness Trainer",
            "interest_tags": [
                "Coaching & Training"
            ],
            "short_description": "Professional role working in the field of Personal/Fitness Trainer to design, implement, or manage solutions.",
            "about": "A Personal/Fitness Trainer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Personal/Fitness Trainer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "yoga-instructor",
            "name": "Yoga Instructor",
            "interest_tags": [
                "Coaching & Training"
            ],
            "short_description": "Teaches yoga postures (asanas), breathing methods (pranayama), and meditation to clients.",
            "about": "Yoga teachers lead classes, adjust posture alignments, consult on holistic lifestyles, and run corporate wellness retreats.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "B.Sc. or Diploma in Yoga Sciences or complete QCI certification courses (1-3 years)."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "High growth, massive global interest in wellness",
            "colleges": [
                {
                    "name": "Indian Institute of Yoga Sciences (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Yoga Sciences.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Yoga Sciences (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Yoga Sciences (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "strength-and-conditioning-coach",
            "name": "Strength & Conditioning Coach",
            "interest_tags": [
                "Coaching & Training"
            ],
            "short_description": "Professional role working in the field of Strength & Conditioning Coach to design, implement, or manage solutions.",
            "about": "A Strength & Conditioning Coach applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Strength & Conditioning Coach."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sports-physiotherapist",
            "name": "Sports Physiotherapist",
            "interest_tags": [
                "Sports Science & Health"
            ],
            "short_description": "Treats athletic muscle tears, runs joint rehab drills, and designs injury-prevention stretch grids.",
            "about": "Physiotherapists apply muscle tapes, perform manual massage therapy, oversee recovery runs, and check joint mobilities.",
            "educational_roadmap": [
                "Class 12 with Physics, Chemistry, and Biology (PCB) background.",
                "Complete a Bachelor of Physiotherapy (BPT) course (4.5 years).",
                "Complete specialized master's degree (MPT) in Sports Physiotherapy (2 years)."
            ],
            "entrance_exams": [
                "NEET",
                "CUET-UG"
            ],
            "salary_range": "₹4–12 LPA",
            "growth_outlook": "High growth, crucial role in professional teams",
            "colleges": [
                {
                    "name": "Indian Institute of Physiotherapy (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Physiotherapy.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Physiotherapy (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Physiotherapy (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "sports-nutritionist",
            "name": "Sports Nutritionist",
            "interest_tags": [
                "Sports Science & Health"
            ],
            "short_description": "Designs calorie and macro targets, supplement guides, and hydration protocols for professional athletes.",
            "about": "Nutritionists calculate client energy expenditures, plan pre-match meals, audit body fat percentages, and manage supplement logs.",
            "educational_roadmap": [
                "Class 12 with PCB background.",
                "B.Sc. in Nutrition & Dietetics (3 years).",
                "M.Sc. or PG Diploma in Sports Nutrition (1-2 years)."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Strong demand as athletes focus on science-based diets",
            "colleges": [
                {
                    "name": "Indian Institute of Sports Nutrition (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Sports Nutrition.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Sports Nutrition (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Sports Nutrition (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "sports-psychologist",
            "name": "Sports Psychologist",
            "interest_tags": [
                "Sports Science & Health"
            ],
            "short_description": "Helps athletes handle performance anxiety, recover from mental burnout, and build focus.",
            "about": "Psychologists run breathing drills, consult on goal setting, build team trust, and counsel players returning from injuries.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "B.Sc./B.A. in Psychology (3 years).",
                "M.Sc. in Sports Psychology or Clinical Psychology (2 years)."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹5–13 LPA",
            "growth_outlook": "Growing recognition of mental health in sports",
            "colleges": [
                {
                    "name": "Indian Institute of Sports Psychology (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Sports Psychology.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Sports Psychology (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Sports Psychology (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "exercise-physiologist",
            "name": "Exercise Physiologist",
            "interest_tags": [
                "Sports Science & Health"
            ],
            "short_description": "Professional role working in the field of Exercise Physiologist to design, implement, or manage solutions.",
            "about": "A Exercise Physiologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Exercise Physiologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sports-management-professional",
            "name": "Sports Management Professional",
            "interest_tags": [
                "Sports Business & Media"
            ],
            "short_description": "Professional role working in the field of Sports Management Professional to design, implement, or manage solutions.",
            "about": "A Sports Management Professional applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Sports Management Professional."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sports-analyst-commentator",
            "name": "Sports Analyst/Commentator",
            "interest_tags": [
                "Sports Business & Media"
            ],
            "short_description": "Professional role working in the field of Sports Analyst/Commentator to design, implement, or manage solutions.",
            "about": "A Sports Analyst/Commentator applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Sports Analyst/Commentator."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sports-journalist",
            "name": "Sports Journalist",
            "interest_tags": [
                "Sports Business & Media"
            ],
            "short_description": "Reports match results, interviews players, writes match columns, and runs sports radio or video shows.",
            "about": "Sports journalists attend matches, write commentary files, edit video reels, and host panel debates on channel networks.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "B.A. in Journalism or Mass Media (3 years).",
                "Build a portfolio writing sports columns and reels."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Stable growth, high options in independent digital media channels",
            "colleges": [
                {
                    "name": "Indian Institute of Sports Journalism (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Sports Journalism.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Sports Journalism (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Sports Journalism (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "sports-marketing-manager",
            "name": "Sports Marketing Manager",
            "interest_tags": [
                "Sports Business & Media"
            ],
            "short_description": "Professional role working in the field of Sports Marketing Manager to design, implement, or manage solutions.",
            "about": "A Sports Marketing Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Sports Marketing Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "referee-umpire",
            "name": "Referee/Umpire",
            "interest_tags": [
                "Officiating & Design"
            ],
            "short_description": "Professional role working in the field of Referee/Umpire to design, implement, or manage solutions.",
            "about": "A Referee/Umpire applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Referee/Umpire."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sports-equipment-designer",
            "name": "Sports Equipment Designer",
            "interest_tags": [
                "Officiating & Design"
            ],
            "short_description": "Professional role working in the field of Sports Equipment Designer to design, implement, or manage solutions.",
            "about": "A Sports Equipment Designer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Obtain a Bachelor of Physical Education (B.P.Ed) or B.Sc. in Sports Science, Physiology, or Nutrition (3-4 years).",
                "Compete in university, district, or national tournaments to build competitive athletic stats.",
                "Acquire recognized professional coaching, personal training, or officiating certificates (e.g., SAI, NIS, ACE).",
                "Join sports academies, gym franchises, or professional athletic teams as a certified Sports Equipment Designer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Performing Arts": [
        {
            "id": "musician",
            "name": "Musician",
            "interest_tags": [
                "Music"
            ],
            "short_description": "Plays musical instruments in recording studios, live bands, orchestras, or solo stage shows.",
            "about": "Musicians practice instrument techniques, read musical sheets, record audio tracks, and collaborate on band tours.",
            "educational_roadmap": [
                "Class 12 pass.",
                "B.Mus or acquire professional grading certifications from music boards (e.g. Trinity College London)."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3–12 LPA",
            "growth_outlook": "Highly competitive, high freelance options",
            "colleges": [
                {
                    "name": "Indian Institute of Instrumental Music (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Instrumental Music.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Instrumental Music (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Instrumental Music (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "music-composer-producer",
            "name": "Music Composer/Producer",
            "interest_tags": [
                "Music"
            ],
            "short_description": "Professional role working in the field of Music Composer/Producer to design, implement, or manage solutions.",
            "about": "A Music Composer/Producer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Music Composer/Producer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "music-teacher",
            "name": "Music Teacher",
            "interest_tags": [
                "Music"
            ],
            "short_description": "Professional role working in the field of Music Teacher to design, implement, or manage solutions.",
            "about": "A Music Teacher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Music Teacher."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "actor",
            "name": "Actor",
            "interest_tags": [
                "Acting & Theatre"
            ],
            "short_description": "Interprets script roles, rehearsals scenes, and performs characters in films, TV, theatre, or web series.",
            "about": "Actors study scripts, analyze character psychology, practice voice modulations, attend auditions, and perform in theatre plays or film sets. It requires creative empathy, physical flexibility, and resilience.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Complete a B.A. or Diploma in Dramatic Arts from a design or drama institute (3 years).",
                "Join local theatre groups and build audition portfolios."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–15 LPA",
            "growth_outlook": "Highly competitive, freelance flexibility",
            "colleges": [
                {
                    "name": "Indian Institute of Drama & Theatre (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Drama & Theatre.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Drama & Theatre (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Drama & Theatre (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "theatre-director",
            "name": "Theatre Director",
            "interest_tags": [
                "Acting & Theatre"
            ],
            "short_description": "Oversees the artistic vision, casting, blockings, and rehearsals of live stage plays.",
            "about": "Theatre directors adapt script plays, audition actors, direct scenic blockings, design stage sets with technicians, and lead rehearsals.",
            "educational_roadmap": [
                "Class 12 pass.",
                "B.A. in Dramatic Arts (3 years).",
                "Join professional theatre troupes as assistant director."
            ],
            "entrance_exams": [],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "Niche sector, highly collaborative",
            "colleges": [
                {
                    "name": "Indian Institute of Theatre Arts (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Theatre Arts.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Theatre Arts (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Theatre Arts (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "voice-dubbing-artist",
            "name": "Voice/Dubbing Artist",
            "interest_tags": [
                "Acting & Theatre"
            ],
            "short_description": "Professional role working in the field of Voice/Dubbing Artist to design, implement, or manage solutions.",
            "about": "A Voice/Dubbing Artist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Voice/Dubbing Artist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "playwright",
            "name": "Playwright",
            "interest_tags": [
                "Acting & Theatre"
            ],
            "short_description": "Writes dialogues, story actions, and script logs for movies, theatre plays, and digital web channels.",
            "about": "Scriptwriters outline plots, write dialogue logs, consult with directors on revisions, and pitch scripts to production houses.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "B.A. in Creative Writing, Literature, or Cinema Studies (3 years).",
                "Publish short stories or scripts to build a profile."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹4–12 LPA",
            "growth_outlook": "Strong demand, fueled by digital web series",
            "colleges": [
                {
                    "name": "Indian Institute of Screenwriting (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Screenwriting.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Screenwriting (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Screenwriting (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "dancer",
            "name": "Dancer",
            "interest_tags": [
                "Dance"
            ],
            "short_description": "Performs classical or contemporary dance forms, choreographs routines, and teaches dance groups.",
            "about": "Dancers practice daily routines, learn historical movements, perform on stages, design choreography plans, and run class studios.",
            "educational_roadmap": [
                "Class 12 pass.",
                "Bachelor of Performing Arts (BPA) in Dance (3 years) or train under a master guru.",
                "Perform in local festivals and build stage records."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3–9 LPA",
            "growth_outlook": "Competitive sector, steady teaching options",
            "colleges": [
                {
                    "name": "Indian Institute of Dance & Choreography (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Dance & Choreography.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Dance & Choreography (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Dance & Choreography (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "choreographer",
            "name": "Choreographer",
            "interest_tags": [
                "Dance"
            ],
            "short_description": "Designs dance movements, directs stage alignments, and teaches dance routines to actors and dance teams.",
            "about": "Choreographers adapt scripts into dance steps, run cast training drills, map stage blockings, and direct dance ensembles.",
            "educational_roadmap": [
                "Class 12 pass.",
                "Gather extensive experience dancing in professional groups.",
                "Complete basic dance grading or diploma courses."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–14 LPA",
            "growth_outlook": "Stable demand in music videos and movies",
            "colleges": [
                {
                    "name": "Indian Institute of Dance Education (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Dance Education.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Dance Education (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Dance Education (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "dance-instructor",
            "name": "Dance Instructor",
            "interest_tags": [
                "Dance"
            ],
            "short_description": "Professional role working in the field of Dance Instructor to design, implement, or manage solutions.",
            "about": "A Dance Instructor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Dance Instructor."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "film-director",
            "name": "Film Director",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Directs the visual style, acting performances, and creative storytelling flow of movies, TV shows, and advertisements.",
            "about": "Directors decode script actions, guide camera angles, direct actors, review lighting setups, and supervise film editing sequences.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear FTII or SRFTI Entrance Exam.",
                "B.A. in Film Direction / Cinematography (3 years).",
                "Assist senior directors and make independent short films."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–25 LPA",
            "growth_outlook": "Highly competitive, expanding options in streaming platforms",
            "colleges": [
                {
                    "name": "Indian Institute of Filmmaking (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Filmmaking.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Filmmaking (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Filmmaking (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "cinematographer",
            "name": "Cinematographer",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Professional role working in the field of Cinematographer to design, implement, or manage solutions.",
            "about": "A Cinematographer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Cinematographer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "film-editor",
            "name": "Film Editor",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Professional role working in the field of Film Editor to design, implement, or manage solutions.",
            "about": "A Film Editor applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Film Editor."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "screenwriter",
            "name": "Screenwriter",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Professional role working in the field of Screenwriter to design, implement, or manage solutions.",
            "about": "A Screenwriter applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Screenwriter."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "sound-engineer",
            "name": "Sound Engineer",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Professional role working in the field of Sound Engineer to design, implement, or manage solutions.",
            "about": "A Sound Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Sound Engineer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "stage-set-designer",
            "name": "Stage/Set Designer",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Professional role working in the field of Stage/Set Designer to design, implement, or manage solutions.",
            "about": "A Stage/Set Designer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Stage/Set Designer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "costume-designer",
            "name": "Costume Designer",
            "interest_tags": [
                "Film Production"
            ],
            "short_description": "Professional role working in the field of Costume Designer to design, implement, or manage solutions.",
            "about": "A Costume Designer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Join a recognized music academy, dance academy, or film institute (e.g., FTII, NSD) for a BPA or specialized diploma (3 years).",
                "Build a creative portfolio (e.g., upload music demos, act in theater plays, script short films).",
                "Do apprenticeships, internships, or shadow established industry professionals.",
                "Register with artist guilds and take freelance projects, cast calls, or commercial contracts to work as Costume Designer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Agriculture & Allied Sciences": [
        {
            "id": "agricultural-scientist",
            "name": "Agricultural Scientist",
            "interest_tags": [
                "Crop & Soil Science"
            ],
            "short_description": "Professional role working in the field of Agricultural Scientist to design, implement, or manage solutions.",
            "about": "A Agricultural Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Agricultural Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "agronomist",
            "name": "Agronomist",
            "interest_tags": [
                "Crop & Soil Science"
            ],
            "short_description": "Conducts research to improve crop yields, soil health, and farming techniques to ensure food security.",
            "about": "Agronomists study soil biology, plant breeding, and pest control to make agriculture efficient and climate-resilient. You'll spend time in lab facilities testing plant DNA, as well as on test farms advising growers on fertilizer combinations, crop rotation, and water conservation technologies.",
            "educational_roadmap": [
                "Class 12 with Biology or Agriculture as major subject.",
                "Clear ICAR-AIEEA or state-level agriculture entrance tests.",
                "Obtain B.Sc. (Hons) in Agriculture (4 years).",
                "Complete M.Sc. in Agronomy, Genetics, or Soil Science (2 years).",
                "Join a government research center like ICAR, or private agritech firm."
            ],
            "entrance_exams": [
                "ICAR-AIEEA"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Stable growth, expanding tech-driven agritech startups",
            "colleges": [
                {
                    "name": "Indian Agricultural Research Institute (IARI), New Delhi",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.iari.res.in/",
                    "short_description": "India's apex institute for agricultural education and research.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Punjab Agricultural University (PAU), Ludhiana",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.pau.edu/",
                    "short_description": "Pioneered the Green Revolution in India; top agricultural university.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Cornell University, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.cornell.edu/",
                    "short_description": "Top-tier Ivy League university renowned for agricultural sciences.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "soil-scientist",
            "name": "Soil Scientist",
            "interest_tags": [
                "Crop & Soil Science"
            ],
            "short_description": "Professional role working in the field of Soil Scientist to design, implement, or manage solutions.",
            "about": "A Soil Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Soil Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "horticulturist",
            "name": "Horticulturist",
            "interest_tags": [
                "Crop & Soil Science"
            ],
            "short_description": "Manages commercial greenhouses, breeds ornamental plants, and consults on urban rooftop gardens.",
            "about": "Horticulturists configure greenhouse hydroponics, monitor nursery yields, breed flower variants, and design urban landscape gardens.",
            "educational_roadmap": [
                "Class 12 with Biology background.",
                "B.Sc. in Horticulture (4 years).",
                "complete internships at commercial plant nurseries."
            ],
            "entrance_exams": [
                "ICAR-AIEEA"
            ],
            "salary_range": "₹4–9 LPA",
            "growth_outlook": "Steady growth in urban floriculture and greenhouses",
            "colleges": [
                {
                    "name": "Indian Institute of Horticulture (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Horticulture.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Horticulture (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Horticulture (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "organic-farming-advisor",
            "name": "Organic Farming Consultant",
            "interest_tags": [
                "Crop & Soil Science"
            ],
            "short_description": "Helps farms transition to chemical-free agriculture, manages compost pits, and manages organic certification audits.",
            "about": "Organic consultants audit pesticide levels, design companion planting layouts, manage bio-pest controls, and write organic audit logs.",
            "educational_roadmap": [
                "Class 12 with PCB/Agriculture.",
                "B.Sc. in Agriculture or Horticulture (4 years).",
                "Obtain certifications in Organic Farm Standards."
            ],
            "entrance_exams": [
                "ICAR-AIEEA"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "High growth, driven by consumer demands for organic foods",
            "colleges": [
                {
                    "name": "Indian Institute of Organic Agriculture (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Organic Agriculture.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Organic Agriculture (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Organic Agriculture (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "veterinarian",
            "name": "Veterinarian",
            "interest_tags": [
                "Animal & Fisheries Science"
            ],
            "short_description": "Diagnoses and treats diseases, injuries, and health disorders in domestic and wild animals.",
            "about": "Veterinarians care for animals, performing surgeries, dispensing therapeutics, checking farm livestock health, and managing pet vaccination campaigns.",
            "educational_roadmap": [
                "Class 12 with PCB.",
                "Clear NEET-UG or state veterinary tests.",
                "Bachelor of Veterinary Science & Animal Husbandry (B.V.Sc & AH) (5.5 years).",
                "Register with Veterinary Council of India."
            ],
            "entrance_exams": [
                "NEET"
            ],
            "salary_range": "₹4–11 LPA",
            "growth_outlook": "Steady demand in pet clinics, livestock panels, and forest sanctuaries",
            "colleges": [
                {
                    "name": "Indian Institute of Veterinary Surgeon (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Veterinary Surgeon.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Veterinary Surgeon (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Veterinary Surgeon (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "fisheries-scientist",
            "name": "Fisheries Scientist",
            "interest_tags": [
                "Animal & Fisheries Science"
            ],
            "short_description": "Professional role working in the field of Fisheries Scientist to design, implement, or manage solutions.",
            "about": "A Fisheries Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Fisheries Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "dairy-technologist",
            "name": "Dairy Technologist",
            "interest_tags": [
                "Animal & Fisheries Science"
            ],
            "short_description": "Oversees processing pasteurization, milk packing, quality testing, and product development in dairy processing plants.",
            "about": "Dairy technologists test milk purity, configure cream separators, manage pasteurizer controls, and design dairy products like cheeses.",
            "educational_roadmap": [
                "Class 12 with PCM/PCB background.",
                "Clear ICAR-AIEEA or state tests.",
                "B.Tech in Dairy Technology (4 years)."
            ],
            "entrance_exams": [
                "ICAR-AIEEA"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable, India has a massive dairy cooperative network",
            "colleges": [
                {
                    "name": "Indian Institute of Dairy Technology (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Dairy Technology.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Dairy Technology (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Dairy Technology (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "poultry-scientist",
            "name": "Poultry Scientist",
            "interest_tags": [
                "Animal & Fisheries Science"
            ],
            "short_description": "Professional role working in the field of Poultry Scientist to design, implement, or manage solutions.",
            "about": "A Poultry Scientist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Poultry Scientist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "agritech-specialist",
            "name": "AgriTech Specialist",
            "interest_tags": [
                "AgriTech & Engineering"
            ],
            "short_description": "Professional role working in the field of AgriTech Specialist to design, implement, or manage solutions.",
            "about": "A AgriTech Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified AgriTech Specialist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "agri-engineer",
            "name": "Agricultural Engineer",
            "interest_tags": [
                "AgriTech & Engineering"
            ],
            "short_description": "Designs machinery like harvesters, automated drip systems, and food processing lines for farms.",
            "about": "Engineers draw tractor frames on CAD, design low water drip valves, test grain sorters, and build bio-compost silos.",
            "educational_roadmap": [
                "Class 12 with PCM background.",
                "Clear JEE-Main or state engineering tests.",
                "B.Tech in Agricultural Engineering (4 years)."
            ],
            "entrance_exams": [
                "JEE-Main"
            ],
            "salary_range": "₹5–13 LPA",
            "growth_outlook": "Steady demand, agritech automation is rising",
            "colleges": [
                {
                    "name": "Indian Institute of Agricultural Engineering (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Agricultural Engineering.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Agricultural Engineering (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Agricultural Engineering (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "irrigation-engineer",
            "name": "Irrigation Engineer",
            "interest_tags": [
                "AgriTech & Engineering"
            ],
            "short_description": "Professional role working in the field of Irrigation Engineer to design, implement, or manage solutions.",
            "about": "A Irrigation Engineer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Irrigation Engineer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "food-technologist",
            "name": "Food Technologist",
            "interest_tags": [
                "Food & Forestry"
            ],
            "short_description": "Professional role working in the field of Food Technologist to design, implement, or manage solutions.",
            "about": "A Food Technologist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Food Technologist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "forest-officer",
            "name": "Forest Officer",
            "interest_tags": [
                "Food & Forestry"
            ],
            "short_description": "Professional role working in the field of Forest Officer to design, implement, or manage solutions.",
            "about": "A Forest Officer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 with Science stream (PCB or PCM).",
                "Clear state-level agricultural entrance tests or ICAR AIEEA examination.",
                "Obtain B.Sc. (Hons) in Agriculture, Horticulture, Forestry, or Agricultural Engineering (4 years).",
                "Complete hands-on training under the Rural Agricultural Work Experience (RAWE) program.",
                "Obtain M.Sc. in specialized field (e.g., Agronomy, Soil Science, Dairy Tech) (2 years).",
                "Join agribusinesses, seed companies, forest ranges, or research centers as a certified Forest Officer."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "agri-extension-officer",
            "name": "Agricultural Extension Officer",
            "interest_tags": [
                "Food & Forestry"
            ],
            "short_description": "Translates laboratory research on soil and seeds into practical farming guidelines for rural village growers.",
            "about": "Extension officers run crop field demonstrations, explain seed packaging guides, distribute government subsidies, and advise on pest cures.",
            "educational_roadmap": [
                "Class 12 with Agriculture or Science.",
                "B.Sc. in Agriculture (4 years).",
                "Clear state agricultural department exam."
            ],
            "entrance_exams": [
                "ICAR-AIEEA"
            ],
            "salary_range": "₹4–9 LPA",
            "growth_outlook": "Stable government public pathway",
            "colleges": [
                {
                    "name": "Indian Institute of Agricultural Extension (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Agricultural Extension.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Agricultural Extension (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Agricultural Extension (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "wildlife-biologist",
            "name": "Wildlife Biologist",
            "interest_tags": [
                "Food & Forestry"
            ],
            "short_description": "Studies the habits, genetics, and environment of animal species to consult on forest reserves and conservation.",
            "about": "Wildlife biologists track animal populations, study zoonotic diseases, consult on reserve plans, and write environmental impact logs.",
            "educational_roadmap": [
                "Class 12 with PCB.",
                "B.Sc. in Zoology, Life Sciences, or Forestry (3 years).",
                "M.Sc. in Wildlife Biology / Conservation (2 years).",
                "Join forest research organizations, reserve commissions, or wildlife NGOs."
            ],
            "entrance_exams": [
                "CUET-UG"
            ],
            "salary_range": "₹3.5–9 LPA",
            "growth_outlook": "Stable growth, linked to government forestry and conservation initiatives",
            "colleges": [
                {
                    "name": "Indian Institute of Wildlife Biologist / Zoologist (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Wildlife Biologist / Zoologist.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Wildlife Biologist / Zoologist (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Wildlife Biologist / Zoologist (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        }
    ],
    "Hospitality": [
        {
            "id": "hotel-manager",
            "name": "Hotel Manager",
            "interest_tags": [
                "Hotel Operations"
            ],
            "short_description": "Professional role working in the field of Hotel Manager to design, implement, or manage solutions.",
            "about": "A Hotel Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Hotel Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "front-office-manager",
            "name": "Front Office Manager (Hotel)",
            "interest_tags": [
                "Hotel Operations"
            ],
            "short_description": "Coordinates lobby guest check-ins, guest requests, room key assignments, and reviews front-desk staff operations.",
            "about": "Front Office Managers resolve VIP requests, train counter staff, check room availability files, and coordinate arrivals with housekeeping.",
            "educational_roadmap": [
                "Class 12 pass in any stream.",
                "B.Sc. or BHM in Hospitality Management (3 years).",
                "Gain experience as receptionist in premium hotels."
            ],
            "entrance_exams": [
                "NCHMCT-JEE"
            ],
            "salary_range": "₹4–9 LPA",
            "growth_outlook": "Steady demand, hotel room volumes are rising",
            "colleges": [
                {
                    "name": "Indian Institute of Front Desk Operations (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Front Desk Operations.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Front Desk Operations (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Front Desk Operations (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "housekeeping-manager",
            "name": "Housekeeping Manager",
            "interest_tags": [
                "Hotel Operations"
            ],
            "short_description": "Professional role working in the field of Housekeeping Manager to design, implement, or manage solutions.",
            "about": "A Housekeeping Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Housekeeping Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "hotel-sales-manager",
            "name": "Hotel Sales Manager",
            "interest_tags": [
                "Hotel Operations"
            ],
            "short_description": "Professional role working in the field of Hotel Sales Manager to design, implement, or manage solutions.",
            "about": "A Hotel Sales Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Hotel Sales Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "chef-culinary-artist",
            "name": "Chef/Culinary Artist",
            "interest_tags": [
                "Culinary Arts"
            ],
            "short_description": "Professional role working in the field of Chef/Culinary Artist to design, implement, or manage solutions.",
            "about": "A Chef/Culinary Artist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Chef/Culinary Artist."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "catering-manager",
            "name": "Catering Manager",
            "interest_tags": [
                "Culinary Arts"
            ],
            "short_description": "Manages food safety, counts food quantities, and sets up buffet service tables for large banquets.",
            "about": "Catering managers compute kitchen bulk orders, hire helper cooks, oversee server logs, and manage table decors.",
            "educational_roadmap": [
                "Class 12 pass.",
                "Diploma or BHM in Catering Technology (3 years)."
            ],
            "entrance_exams": [
                "NCHMCT-JEE"
            ],
            "salary_range": "₹4–9 LPA",
            "growth_outlook": "Stable, linked to corporate meeting and wedding sectors",
            "colleges": [
                {
                    "name": "Indian Institute of Catering Operations (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Catering Operations.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Catering Operations (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Catering Operations (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "tourism-manager",
            "name": "Tourism Manager",
            "interest_tags": [
                "Travel & Tourism"
            ],
            "short_description": "Professional role working in the field of Tourism Manager to design, implement, or manage solutions.",
            "about": "A Tourism Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Tourism Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "travel-agent",
            "name": "Travel Agent",
            "interest_tags": [
                "Travel & Tourism"
            ],
            "short_description": "Professional role working in the field of Travel Agent to design, implement, or manage solutions.",
            "about": "A Travel Agent applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Travel Agent."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "tour-guide",
            "name": "Tour Guide",
            "interest_tags": [
                "Travel & Tourism"
            ],
            "short_description": "Professional role working in the field of Tour Guide to design, implement, or manage solutions.",
            "about": "A Tour Guide applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Tour Guide."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "cruise-ship-staff",
            "name": "Cruise Ship Staff",
            "interest_tags": [
                "Travel & Tourism"
            ],
            "short_description": "Professional role working in the field of Cruise Ship Staff to design, implement, or manage solutions.",
            "about": "A Cruise Ship Staff applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Cruise Ship Staff."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "event-manager",
            "name": "Event Manager",
            "interest_tags": [
                "Events & Dining"
            ],
            "short_description": "Professional role working in the field of Event Manager to design, implement, or manage solutions.",
            "about": "A Event Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Event Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "restaurant-manager",
            "name": "Restaurant Manager",
            "interest_tags": [
                "Events & Dining"
            ],
            "short_description": "Professional role working in the field of Restaurant Manager to design, implement, or manage solutions.",
            "about": "A Restaurant Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Restaurant Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "banquet-manager",
            "name": "Banquet Manager",
            "interest_tags": [
                "Events & Dining"
            ],
            "short_description": "Professional role working in the field of Banquet Manager to design, implement, or manage solutions.",
            "about": "A Banquet Manager applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear NCHMCT JEE or college-specific hospitality admission tests.",
                "Obtain Bachelor of Hotel Management (BHM) or B.Sc. in Hospitality & Hotel Administration (3-4 years).",
                "Complete compulsory industrial training (6 months) in kitchen, front office, housekeeping, or sales.",
                "Join hospitality management trainee programs of premium hotel chains.",
                "Enter guest relations, restaurant setups, or event operations to work as Banquet Manager."
            ],
            "entrance_exams": [],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        }
    ],
    "Law": [
        {
            "id": "corporate-lawyer",
            "name": "Corporate Lawyer",
            "interest_tags": [
                "Litigation & Advocacy"
            ],
            "short_description": "Advises companies on their legal rights and duties, structures deals, and ensures business practices comply with regulations.",
            "about": "Corporate lawyers handle corporate restructuring, write contracts, advise on mergers, protect intellectual property, and represent businesses in legal disputes. You'll spend a lot of time reading, researching legal precedents, drafting agreements, and participating in negotiation meetings.",
            "educational_roadmap": [
                "Class 12 in any stream (Commerce or Humanities preferred).",
                "Clear CLAT, AILET, or LSAT-India.",
                "Join an integrated 5-year B.A. LL.B / B.Com LL.B program.",
                "Complete internships in corporate firms and courts.",
                "Pass the All India Bar Examination (AIBE) to register as an advocate."
            ],
            "entrance_exams": [
                "CLAT",
                "AILET",
                "LSAT-India",
                "LSAT"
            ],
            "salary_range": "₹8–24 LPA",
            "growth_outlook": "Strong growth, driven by growing corporate ecosystems",
            "colleges": [
                {
                    "name": "National Law School of India University (NLSIU), Bengaluru",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.nls.ac.in/",
                    "short_description": "India's highest-ranked university for law education.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "NALSAR University of Law, Hyderabad",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.nalsar.ac.in/",
                    "short_description": "Outstanding national law university with corporate law focus.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Harvard Law School, USA",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://hls.harvard.edu/",
                    "short_description": "Globally renowned ivy league law school.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "criminal-lawyer",
            "name": "Criminal Lawyer",
            "interest_tags": [
                "Litigation & Advocacy"
            ],
            "short_description": "Professional role working in the field of Criminal Lawyer to design, implement, or manage solutions.",
            "about": "A Criminal Lawyer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Criminal Lawyer."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "public-prosecutor",
            "name": "Public Prosecutor",
            "interest_tags": [
                "Litigation & Advocacy"
            ],
            "short_description": "Conducts criminal trials on behalf of the state, coordinates with police officers, and presents cases against defendants.",
            "about": "Prosecutors lead criminal cases, interview crime investigators, present physical evidence, and make final case pleas in sessions courts.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Complete LL.B (3 or 5 years).",
                "Gain minimum 7 years court practice and clear Assistant Public Prosecutor (APP) exams."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–11 LPA",
            "growth_outlook": "Stable government judiciary career",
            "colleges": [
                {
                    "name": "Indian Institute of Criminal Justice (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Criminal Justice.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Criminal Justice (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Criminal Justice (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "human-rights-lawyer",
            "name": "Human Rights Lawyer",
            "interest_tags": [
                "Litigation & Advocacy"
            ],
            "short_description": "Defends marginalized groups, opposes illegal detentions, and advocates for civil liberties in courts.",
            "about": "Human Rights advocates represent poor litigants, write legal reviews for human rights commissions, and file cases against state excesses.",
            "educational_roadmap": [
                "Class 12 in Humanities/Arts.",
                "Complete 5-year B.A. LL.B course.",
                "Complete internships at NGOs, legal aid cells, and supreme court chambers."
            ],
            "entrance_exams": [
                "CLAT",
                "CUET-UG"
            ],
            "salary_range": "₹3–8 LPA",
            "growth_outlook": "Niche social sector, relies heavily on NGO grants",
            "colleges": [
                {
                    "name": "Indian Institute of Human Rights Law (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Human Rights Law.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Human Rights Law (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Human Rights Law (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "civil-litigation-lawyer",
            "name": "Civil Litigation Lawyer",
            "interest_tags": [
                "Litigation & Advocacy"
            ],
            "short_description": "Professional role working in the field of Civil Litigation Lawyer to design, implement, or manage solutions.",
            "about": "A Civil Litigation Lawyer applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Civil Litigation Lawyer."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "judge-judiciary-services",
            "name": "Judge/Judiciary Services",
            "interest_tags": [
                "Judiciary"
            ],
            "short_description": "Professional role working in the field of Judge/Judiciary Services to design, implement, or manage solutions.",
            "about": "A Judge/Judiciary Services applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Judge/Judiciary Services."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "magistrate",
            "name": "Magistrate",
            "interest_tags": [
                "Judiciary"
            ],
            "short_description": "Professional role working in the field of Magistrate to design, implement, or manage solutions.",
            "about": "A Magistrate applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Magistrate."
            ],
            "entrance_exams": [],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "patent-attorney",
            "name": "Patent Attorney",
            "interest_tags": [
                "Specialized Legal Practice"
            ],
            "short_description": "Professional role working in the field of Patent Attorney to design, implement, or manage solutions.",
            "about": "A Patent Attorney applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Patent Attorney."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "cyber-law-specialist",
            "name": "Cyber Law Specialist",
            "interest_tags": [
                "Specialized Legal Practice"
            ],
            "short_description": "Professional role working in the field of Cyber Law Specialist to design, implement, or manage solutions.",
            "about": "A Cyber Law Specialist applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Cyber Law Specialist."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "notary",
            "name": "Notary",
            "interest_tags": [
                "Specialized Legal Practice"
            ],
            "short_description": "Professional role working in the field of Notary to design, implement, or manage solutions.",
            "about": "A Notary applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Notary."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "tax-lawyer",
            "name": "Tax Lawyer",
            "interest_tags": [
                "Specialized Legal Practice"
            ],
            "short_description": "Represents clients in corporate tax audits, appeals GST rulings, and designs legal tax avoidance structures.",
            "about": "Tax lawyers write tax appeal arguments, represent clients in excise tribunals, check GST records, and draft tax shelter deeds.",
            "educational_roadmap": [
                "Class 12 in Commerce.",
                "Clear CLAT or LSAT-India.",
                "B.Com LL.B or B.B.A. LL.B (5 years).",
                "Complete Chartered Accountant (CA) or LL.M in Taxation."
            ],
            "entrance_exams": [
                "CLAT",
                "LSAT-India"
            ],
            "salary_range": "₹7–20 LPA",
            "growth_outlook": "Stable demand, tax laws are highly complex",
            "colleges": [
                {
                    "name": "Indian Institute of Tax Law (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Tax Law.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Tax Law (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Tax Law (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "legal-consultant",
            "name": "Legal Consultant",
            "interest_tags": [
                "Legal Research & Compliance"
            ],
            "short_description": "Professional role working in the field of Legal Consultant to design, implement, or manage solutions.",
            "about": "A Legal Consultant applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Legal Consultant."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "legal-researcher",
            "name": "Legal Researcher",
            "interest_tags": [
                "Legal Research & Compliance"
            ],
            "short_description": "Professional role working in the field of Legal Researcher to design, implement, or manage solutions.",
            "about": "A Legal Researcher applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Legal Researcher."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "company-secretary",
            "name": "Company Secretary",
            "interest_tags": [
                "Legal Research & Compliance"
            ],
            "short_description": "Professional role working in the field of Company Secretary to design, implement, or manage solutions.",
            "about": "A Company Secretary applies industry best practices, analytical methods, and specialized tools to resolve domain-specific problems. You will collaborate in multidisciplinary teams, drive strategic objectives, and continuously update your skill set to adapt to market trends.",
            "educational_roadmap": [
                "Class 12 in any stream.",
                "Clear the Common Law Admission Test (CLAT) or state law CETs.",
                "Complete a 5-year integrated law degree (BA LLB, BBA LLB, B.Com LLB), or a 3-year LLB after graduation.",
                "Intern under senior advocates, law firms, corporate legal rooms, or judicial offices (minimum 12-20 weeks).",
                "Pass the All India Bar Examination (AIBE) to obtain a Certificate of Practice.",
                "Enroll with the State Bar Council and join litigation chambers or corporate offices as Company Secretary."
            ],
            "entrance_exams": [
                "CLAT"
            ],
            "salary_range": "₹5–12 LPA",
            "growth_outlook": "Stable growth, robust hiring trends",
            "colleges": []
        },
        {
            "id": "legal-journalist",
            "name": "Legal Journalist",
            "interest_tags": [
                "Legal Research & Compliance"
            ],
            "short_description": "Reports on supreme court hearings, summarizes landmark judgments, and writes reviews on legal issues.",
            "about": "Legal journalists write court blogs, interview legal scholars, translate legal terms for public media, and record podcasts.",
            "educational_roadmap": [
                "Class 12 pass.",
                "B.A. LL.B or B.A. in Journalism (3-5 years).",
                "Intern at legal news portals and publishing houses."
            ],
            "entrance_exams": [
                "CLAT",
                "CUET-UG"
            ],
            "salary_range": "₹4–10 LPA",
            "growth_outlook": "Stable growth, driven by digital legal media portals",
            "colleges": [
                {
                    "name": "Indian Institute of Legal Journalism (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Legal Journalism.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Legal Journalism (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Legal Journalism (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        },
        {
            "id": "compliance-officer",
            "name": "Compliance Officer",
            "interest_tags": [
                "Legal Research & Compliance"
            ],
            "short_description": "Audits corporate activities, ensures environmental compliance, and implements corporate anti-bribery rules.",
            "about": "Compliance officers run employee training, check corporate accounting filings, manage whistleblower reports, and write audit charts.",
            "educational_roadmap": [
                "Class 12 in Commerce or Humanities.",
                "B.B.A. LL.B or Company Secretary (CS) course (3-5 years).",
                "Obtain certifications in corporate compliance."
            ],
            "entrance_exams": [
                "CLAT",
                "CUET-UG"
            ],
            "salary_range": "₹5–14 LPA",
            "growth_outlook": "Stable demand, driven by rising corporate standards",
            "colleges": [
                {
                    "name": "Indian Institute of Corporate Governance (Example Top)",
                    "location": "India",
                    "tier": "Top",
                    "website_url": "https://www.example.edu/",
                    "short_description": "Premier national institute for training and advanced research in Corporate Governance.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "National Academy of Corporate Governance (Example Tier 2)",
                    "location": "India",
                    "tier": "Tier 2",
                    "website_url": "https://www.example-academy.edu.in/",
                    "short_description": "Highly respected institute offering vocational and undergraduate courses.",
                    "// TODO: verify": "Verify college credentials and details."
                },
                {
                    "name": "Global School of Corporate Governance (Example Abroad)",
                    "location": "Abroad",
                    "tier": "Top",
                    "website_url": "https://www.example-abroad.edu/",
                    "short_description": "Renowned worldwide for offering cutting-edge courses and industry placements.",
                    "// TODO: verify": "Verify college credentials and details."
                }
            ]
        }
    ]
}

    # Flatten and assign Path name to each career
    careers = []
    for path_name, career_list in raw_paths_careers.items():
        for car in career_list:
            car["path"] = path_name
            # Deduplicate interest tags to prevent db unique constraint issues
            car["interest_tags"] = list(dict.fromkeys(car.get("interest_tags", [])))
            # If colleges list is empty, build it
            if not car.get("colleges"):
                car["colleges"] = build_colleges(car["name"], path_name)
            # Insert TODO check marker in college objects
            for col in car["colleges"]:
                col["// TODO: verify"] = "Verify college credentials and details."
            car["// TODO: verify"] = "Verify salary range, details and exams."
            careers.append(car)

    output_data = {
        "careers": careers,
        "exams": exams
    }

    # Save to the paths
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "data"))
    if not os.path.exists(frontend_dir):
        os.makedirs(frontend_dir)
        
    frontend_path = os.path.join(frontend_dir, "careers.json")
    with open(frontend_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(careers)} careers and wrote to {frontend_path}")

    backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
    if not os.path.exists(backend_dir):
        os.makedirs(backend_dir)
    backend_path = os.path.join(backend_dir, "careers.json")
    with open(backend_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(careers)} careers and wrote to {backend_path}")

if __name__ == "__main__":
    generate_careers_json()
