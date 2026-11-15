
def read_attendance():
    return [
        ("101", "P"),
        ("101", "P"),
        ("101", "A"),
        ("102", "P"),
        ("102", "A"),
        ("102", "A"),
        ("103", "P"),
        ("103", "P"),
        ("103", "P")
    ]


def calculate_attendance(records):
    result = {}

    for reg, status in records:
        if reg not in result:
            result[reg] = [0, 0]

        if status == "P":
            result[reg][0] += 1
        elif status == "A":
            result[reg][1] += 1

    return result


def generate_report(result):
    print("STUDENT ATTENDANCE REPORT")
    print("--------------------------")

    for reg, values in result.items():
        present = values[0]
        absent = values[1]
        total = present + absent

        percentage = present / total * 100

        print("Student:", reg)
        print("Attendance:", round(percentage, 2), "%")

        if percentage < 75:
            print("Warning: Low Attendance")
        else:
            print("Status: Eligible")

        print("--------------------------")


def main():
    records = read_attendance()
    result = calculate_attendance(records)
    generate_report(result)
    print("Report Generated Successfully")


main()
