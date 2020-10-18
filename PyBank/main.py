import os
import csv

filepath = os.path.join('Resources', 'budget_data.csv')

# Identify my tile with spacing
print('''
Financial Analysis''')
print('''......................................
''')

# open and read csv file, then create a variable for the number of rows within the file
# number of rows within the file has the same value as number of months
with open(filepath, 'r') as file:
    reader1 = csv.reader(file, delimiter= ',')
    title = next(reader1)
    num_month = len(list(reader1))
    num_month = str(num_month)
    print(f' Total Months: {num_month}')


 # open and read csv file, then create a empty list and a variable with 0 for later use
with open(filepath, 'r') as file:
    reader2 = csv.reader(file, delimiter= ',')
    title = next(reader2)
    total = 0
    li = []

# create a loop within the csv file, then create a variable to save the loop within the second column
# chaged the format of the number to include dollar sign
# then using the empty list to store my total
    for i in reader2:
        amount = int(i[1])
        total = total + amount
        t = '${}'.format(total)
        li.append(t)
    print(f' total: {li[-1]}')


# open and read csv file, then create a empty list and a variable with 0 for later use
with open(filepath, 'r') as file:
    reader3 = csv.reader(file, delimiter= ',')
    title = next(reader3)
    av = 0
    avli = []

# created a loop within the csv file and pulled my loop within row 1 into my empty list above
    for row in reader3:
        value = int(row[1])
        avli.append(value)

# created a nested loop to analyze the changes in profit
# change format to include 2 decimal places 
    avli2 = ([x - avli[j - 1] for j, x in enumerate(avli)][1:])
    length = len(avli2)
    
    flo_num = sum(avli2) / length
    av_format = '{:.2f}'.format(flo_num)
    print(f' Average change: $ {av_format}')

# open and read csv file, then create 2 empty list for later use
with open(filepath, 'r') as file:
    reader4 = csv.reader(file, delimiter = ',')
    title = next(reader4)
    profit = []
    date_profit = []
    
# created a for loop to go through Profit/Losses as well as entire csv file
# use max and min function to find the values of the maximum and minimum Profit/losses 
# use index to reference correct result
    for i in reader4:
        record = int(i[1])
        drecord = i
        profit.append(record)
        date_profit.append(drecord)
        _max = max(profit)
        _min = min(profit)
        dex = profit.index(_min)
        dex2 = profit.index(_max)
        min_date = date_profit[dex]
        max_date = date_profit[dex2]

print(f' Greatest Increase in profits: {max_date}')
print(f' Greatest Decrease in profits: {min_date}')

print(''' 
''')

# converting variables into strings so that it can be saved in a txt file
t = str(t)
av_format = str(av_format)
min_date = str(min_date)
max_date = str(max_date)


# opening a txt file with content for Financial Analysis 
file = open('Output.txt', 'a')
file.writelines('Financial Analysis' '\n' '..........................' 
                '\n' ' ' '\n' 'Total Months: ' + num_month + 
                '\n' + 'Total: ' + t + '\n' + 'Average Change: ' + av_format + 
                '\n' + 'Greatest Increase in Profits: ' + max_date + 
                '\n' + 'Greatest Decrease in Profits: ' + min_date) 
file.close()
