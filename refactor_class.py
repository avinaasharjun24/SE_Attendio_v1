import os
import re

directories = ["c:\\Users\\avina\\Downloads\\attendio\\services", "c:\\Users\\avina\\Downloads\\attendio\\routes", "c:\\Users\\avina\\Downloads\\attendio\\app.py"]

for d in directories:
    if os.path.isfile(d):
        files = [d]
    else:
        files = [os.path.join(d, f) for f in os.listdir(d) if f.endswith(".py")]
        
    for file in files:
        with open(file, "r") as f:
            content = f.read()
            
        old_content = content
        
        # We replace specific strings intelligently
        content = content.replace('payload["class"]', 'payload["department"]')
        content = content.replace('payload.get("class")', 'payload.get("department")')
        content = content.replace('class_name', 'department')
        content = content.replace('class_students', 'department_students')
        content = content.replace('class_filter', 'department_filter')
        content = content.replace('matched_student["class"]', 'matched_student["department"]')
        content = content.replace('row["class"]', 'row["department"]')
        content = content.replace('"class"', '"department"')
        content = content.replace('StudentModel.get_students_by_class', 'StudentModel.get_students_by_department')
        
        if content != old_content:
            with open(file, "w") as f:
                f.write(content)
            print("Updated", file)
