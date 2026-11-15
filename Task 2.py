
data = [
    "101,Monday,P",
    "101,Tuesday,P",
    "101,Wednesday,A",
    "102,Monday,P",
    "102,Tuesday,A",
    "102,Wednesday,A",
    "103,Monday,P",
    "103,Tuesday,P",
    "103,Wednesday,P"
]

attendance = {}

for line in data:
    try:
        reg, day, status = line.split(",")

        if status not in ("P", "A"):
            raise ValueError("Invalid status")

        if reg not in attendance:
            attendance[reg] = [0, 0]

        if status == "P":
            attendance[reg][0] += 1
        else:
            attendance[reg][1] += 1

    except ValueError as e:
        print("Error:", e)

print("BIOMETRIC ATTENDANCE REPORT")
print("----------------------------")

for reg, counts in attendance.items():
    present = counts[0]
    absent = counts[1]
    total = present + absent

    percentage = present / total * 100

    print("Register Number:", reg)
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance:", round(percentage, 2), "%")

    if percentage < 75:
        print("Status: Below 75%")
    else:
        print("Status: Eligible")

    print("----------------------------")

print("Attendance Processing Completed")
