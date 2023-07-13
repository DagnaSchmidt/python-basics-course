# Get details for loan
money_owed = float(input('How much money do you owe?\n'))
annual_percentage = float(input('What is the annual percentage of the loan?\n'))
payment = float(input('How much will you pay back each month in dolars?\n'))
months = int(input('How many months do you want to see the results for?\n'))

monthly_rate = annual_percentage/100/12

for i in range(months):
    # count interest
    interest_to_pay = money_owed*monthly_rate
    # add interest
    money_owed = money_owed+interest_to_pay

    if (money_owed-payment < 0):
        print('The last payment is:', money_owed)
        print('You will pay off the loan in', i+1, 'months')
        break

    # make payment
    money_owed = money_owed-payment

print('Paid', payment, 'of which', interest_to_pay, 'was interested', end=' ')
print('Now I owe', money_owed)
