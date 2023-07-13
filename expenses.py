expenses = []

number_of_expenses = int(input('Enter # of expenses:\n'))

for i in range(number_of_expenses):
    expenses.append(float(input('Enter an expense:\n')))

total = sum(expenses)

print('You spend: $', total, sep='')