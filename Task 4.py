
daily_returns = {
    "Day1": ["Python", "Java"],
    "Day2": ["C Programming", "Data Science"],
    "Day3": ["Machine Learning", "DBMS"]
}

return_log = []
error_log = []

print("LIBRARY BOOK RETURN SYSTEM")
print("---------------------------")

for day, books in daily_returns.items():
    try:
        print("Processing:", day)

        for book in books:
            if book == "":
                raise ValueError("Empty book name")

            return_log.append(book)
            print("Returned:", book)

    except ValueError as e:
        error_log.append(str(e))
        print("Error:", e)

print("---------------------------")
print("FINAL RETURN LOG")

for book in return_log:
    print(book)

print("---------------------------")
print("Total Returned Books:", len(return_log))
print("Total Errors:", len(error_log))
print("Processing Completed Successfully")
