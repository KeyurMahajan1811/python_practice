expences = [2000, 300, 600, 1000, 10000, 9000]
addition = 0

for expence in expences:
    addition = addition+expence

print('Total Expence', addition)  # Comma will add space
print('Total Expence $', addition)  # Comma will add space


# To remove extra space of comma pass sep='' as argument
print('Total Expence $', addition, sep='')


# we can use built in sum function of lists

total = sum(expences)
print('Total Expence $', total, sep='')
