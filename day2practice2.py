students = ["Amal", "Kamal", "Nimali", "Sajith"]

print("Student List:")
for s in students:
    print("-", s)

# Add new student
students.append("Thamal")

print("\nUpdated Student List:")
for s in students:
    print("-", s)

# Dictionary example
student_details = {
    "name": "Thamal",
    "course": "AI Engineering",
    "duration": "12 weeks"
}

print("\nStudent Details:")
for key, value in student_details.items():
    print(key, ":", value)
