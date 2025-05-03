# Write your solution here
daysAtCafe = int(input("How many times a week do you eat at the student cafeteria?"));
price = float(input("The price of a typical student lunch"))
moneyOnGroceries = float(input("How much money do you spend on groceries in a week?"));

print("Avergage food expenditure");
print(f"Daily: {(moneyOnGroceries + (daysAtCafe * price)) / 7} euros");
print(f"Weekly: {moneyOnGroceries + (daysAtCafe * price)} euros");
