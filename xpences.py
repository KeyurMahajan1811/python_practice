no_of_xpen = int(input('How many expences you have in month ?'))
xpen = []

for i in range(no_of_xpen):
    xpen.append(float(input('Enter the Expence:')))

print('Total Xpences $', sum(xpen), sep='')
