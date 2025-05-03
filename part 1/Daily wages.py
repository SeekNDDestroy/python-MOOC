hourlyWage = float(input("Hourly wage:"));
hoursWorked = int(input("Hours worked:"));
day = input("Day of the week:")
if day == "Sunday":
    hourlyWage *= 2;
print(f"Daily wages: {hourlyWage * hoursWorked} euros")
