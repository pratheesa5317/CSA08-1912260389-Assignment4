
data = [
    "101,Arun,1500",
    "102,Bala,1800",
    "103,Charan,1200",
    "104,David,invalid",
    "105,Eswar,2000"
]

total = 0
valid = 0
rejected = 0

print("MESS BILL REPORT")
print("-------------------------")

for line in data:
    try:
        reg, name, amount = line.split(",")
        amount = float(amount)

        print(reg, name, "Rs.", amount)
        total += amount
        valid += 1

    except ValueError:
        print("Rejected Record:", line)
        rejected += 1

print("-------------------------")
print("Valid Records:", valid)
print("Rejected Records:", rejected)
print("Total Bill: Rs.", total)
print("Report Generated Successfully")
