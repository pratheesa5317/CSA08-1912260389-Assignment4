
class InvalidRecord(Exception):
    pass


def validate_record(line):
    parts = line.split(",")

    if len(parts) != 3:
        raise InvalidRecord("Missing fields")

    reg, date, status = parts

    if status not in ("P", "A"):
        raise InvalidRecord("Invalid status")

    return reg, date, status


records = [
    "101,2026-10-08,P",
    "102,2026-10-08,A",
    "103,2026-10-08",
    "104,2026-10-08,X",
    "105,2026-10-08,P"
]

present = 0
absent = 0
errors = 0

print("ATTENDANCE VALIDATION REPORT")
print("-----------------------------")

for number, record in enumerate(records, 1):
    try:
        reg, date, status = validate_record(record)

        if status == "P":
            present += 1
        else:
            absent += 1

        print("Line", number, ": Valid")

    except InvalidRecord as e:
        errors += 1
        print("Line", number, ": Error -", e)

print("-----------------------------")
print("Present:", present)
print("Absent:", absent)
print("Invalid Records:", errors)
print("Valid Records:", present + absent)
print("Program Completed Successfully")
