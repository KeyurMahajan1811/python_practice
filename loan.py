# Get the loan Amount
money_owed = float(input('How much amount you owed from bank\n'))
# Get the anual interest percentage
interest_rate = float(input('On how much interest rate ?\n'))
# Monthly charges
payment = float(input('How much amount you will give monthly\n'))
# For how much month we want see details
months = int(
    input('Till how much month we need to calculate loan amount ?\n'))


# Calculate monthly interest rate
for i in range(months):
    monthly_interest_rate = interest_rate/100/12

    #Add in interest
    if(money_owed - payment < 0):
        print('Loan will be completelly paid after', i+1, "month's")
        print('last payment will be', money_owed)
        break
    interest_paid = money_owed * monthly_interest_rate
    money_owed = money_owed + interest_paid

    # Make Payment
    money_owed = money_owed - payment

    # print the result
    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('now I owed', money_owed)
