# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each of you
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Print the total expenses for each of you
print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Determine who spent more money overall
if your_total > partner_total:
    print("You spent more money overall.")
elif your_total < partner_total:
    print("Your partner spent more money overall.")
else:
    print("You and your partner spent the same amount of money overall.")

# Find out the expense category with significant difference in spending
significant_difference = max(your_expenses, key=lambda x: abs(your_expenses[x] - partner_expenses[x]))
difference = abs(your_expenses[significant_difference] - partner_expenses[significant_difference])

# Print the category and the difference
print("Expense category with significant difference:", significant_difference)
print("Difference:", difference)
