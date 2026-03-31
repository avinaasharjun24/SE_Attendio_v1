import os

file_path = "c:\\Users\\avina\\Downloads\\attendio\\static\\js\\dashboard.js"
with open(file_path, "r") as f:
    content = f.read()

content = content.replace("classFilter", "departmentFilter")
content = content.replace("item.class", "item.department")
content = content.replace('class=', 'department=')

with open(file_path, "w") as f:
    f.write(content)
print("done")
