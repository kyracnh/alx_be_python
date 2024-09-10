mincome = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))

m_savings = mincome - total_expenses

an_interests = m_savings * 12 + (m_savings * 12 * 0.05)

don = "{:.0f}".format(an_interests)

print(f"Your monthly savings are ${m_savings}.")
print(f"Projected savings after one year, with interest, is: ${don}.")
