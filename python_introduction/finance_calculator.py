monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = float(monthly_income) - float(monthly_expenses)

an_interests = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

don = "{:.0f}".format(an_interests)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${don}.")
