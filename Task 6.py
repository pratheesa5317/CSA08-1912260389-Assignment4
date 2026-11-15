
registrations = [
    "101,Arun,EEE,arun@gmail.com,Dance;Music",
    "102,Bala,CSE,bala@gmail.com,Coding",
    "103,Charan,ECE,charan@gmail.com,Dance",
    "104,David,MECH,invalidemail,Music",
    "101,Arun,EEE,arun@gmail.com,Coding",
    "105,Eswar,EEE,eswar@gmail.com,Music"
]

students = set()
master_list = []
events = {}
errors = []

print("COLLEGE FEST REGISTRATION")
print("--------------------------")

for line in registrations:
    try:
        parts = line.split(",")

        if len(parts) != 5:
            raise ValueError("Invalid fields")

        reg, name, dept, email, event_names = parts

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email")

        if reg in students:
            raise ValueError("Duplicate registration")

        students.add(reg)
        master_list.append((reg, name, dept))

        for event in event_names.split(";"):
            if event not in events:
                events[event] = []

            events[event].append(name)

        print(name, "- Registered Successfully")

    except ValueError as e:
        errors.append(str(e))
        print("Rejected:", e)

print("--------------------------")
print("MASTER STUDENT LIST")

for reg, name, dept in master_list:
    print(reg, name, dept)

print("--------------------------")
print("EVENT PARTICIPANTS")

for event, names in events.items():
    print(event, ":", ", ".join(names))

print("--------------------------")
print("Total Students:", len(students))
print("Total Events:", len(events))
print("Rejected Records:", len(errors))
print("Fest Report Generated Successfully")
