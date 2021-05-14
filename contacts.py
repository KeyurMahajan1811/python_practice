
variable = {
    "no": 4,
    "students": [
        {"name": "sarah", "email": "sarah@gmail.com"},
        {"name": "harry", "email": "harry@gmail.com"},
        {"name": "hermione", "email": "hermione@gmail.com"},
        {"name": "ron", "email": "rons@gmail.com"}
    ]
}

print(variable)

for student in variable['students']:
    print(student["name"], "and", student["email"])
