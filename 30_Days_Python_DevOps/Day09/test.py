student_info = {
    "name": "Samiran Samanta",
    "Roll": 17700122042,
    "Year": "4th",
    "Department": "Computer Science & Engineering"
}

print(student_info.get("Roll"))


students_info = [
    {
        "name": "Samiran Samanta",
        "Roll": 17700122042,
        "Year": "4th",
        "Department": "Computer Science & Engineering"
    },
    {
        "name": "Zephyrus",
        "Roll": 17700122043,
        "Year": "4th",
        "Department": "Computer Science & Engineering"
    },
    {
        "name": "Guddu Samanta",
        "Roll": 177001220423,
        "Year": "4th",
        "Department": "Computer Science & Engineering"
    }
]

print(students_info[0].get("name"))