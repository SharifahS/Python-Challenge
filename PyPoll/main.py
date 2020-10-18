import os 
import csv

filepath = os.path.join('Resources', 'election_data.csv')

# identify my title
print('''
Election Results''')
print('''........................''')

# open and read csv file, then create a variable for the number of votes
with open(filepath, 'r') as file:
    reader1 = csv.reader(file, delimiter = ',')
    header = next(reader1)
    total_votes = len(list(reader1))
    
# open and read csv file, then create an empty list for later use
with open(filepath, 'r') as file:
    reader2 = csv.reader(file, delimiter = ',')
    header = next(reader2)
    candidates = []

# created a loop to go through all the votes and pull the candidate names 
    for i in reader2: 
        name = i[2]
        if name not in candidates: 
            candidates.append(name) 

# assigning a variable to each candidate name pulled 
candidate1 = candidates[0]
candidate2 = candidates[1]
candidate3 = candidates[2]
candidate4 = candidates[3]

# open and read csv file, then create a variable with value 0 for future use 
with open(filepath, 'r') as file:
    reader3 = csv.reader(file, delimiter = ',')
    header = next(reader3)
    vote = 0

#empty list for future use 
    list_of_c1 = []
    list_of_c2 = []
    list_of_c3 = []
    list_of_c4 = []

    # create individual list for all the votes each candidate had
    for i in reader3: 
        name = i[2]

        if name == candidate1:
            list_of_c1.append(name)

        elif name == candidate2:
            list_of_c2.append(name)

        elif name == candidate3:
            list_of_c3.append(name)

        elif name == candidate4:
            list_of_c4.append(name)

# assigning a variable to the number of votes for each candidate
vote1 = len(list(list_of_c1))
vote2 = len(list(list_of_c2))
vote3 = len(list(list_of_c3))
vote4 = len(list(list_of_c4))

# calculating the percent of votes each candidate received
# then formating the percent to include 3 decimal places
pct_vote1 = vote1/total_votes * 100
pv1 = '{:.3f}'.format(pct_vote1)

pct_vote2 = vote2/total_votes * 100
pv2 = '{:.3f}'.format(pct_vote2)

pct_vote3 = vote3/total_votes * 100
pv3 = '{:.3f}'.format(pct_vote3)

pct_vote4 = vote4/total_votes * 100
pv4 = '{:.3f}'.format(pct_vote4)

# printing all results
print(f"Total Votes: {total_votes}")
print('''....................................
''')
print(f'{candidate1}: {pv1}% ({vote1})')
print(f'{candidate2}: {pv2}% ({vote2})')
print(f'{candidate3}: {pv3}% ({vote3})')
print(f'{candidate4}: {pv4}% ({vote4})')
print('''.................................
''')

# if statement to evaluate information and provide winner
if vote1 > vote2 and vote1 > vote3 and vote1 > vote4:
    print('Winner: ' + candidate1)
    winner = candidate1

elif vote2 > vote1 and vote2 > vote3 and vote2 > vote4:
    print('Winner: ' + candidate2)
    winner = candidate2

elif vote3 > vote1 and vote3 > vote1 and vote3 > vote4:
    print('Winner: ' + candidate3)
    winner = candidate3

elif vote4 > vote1 and vote4 > vote3 and vote4 > vote2:
    print('Winner: ' + candidate4)
    winner = candidate4

print('...............................................')

# converting variables into strings so that it can be saved in a txt file
candidate1 = str(candidate1)
candidate2 = str(candidate2)
candidate3 = str(candidate3)
candidate4 = str(candidate4)

pv1 = str(pv1)
pv2 = str(pv2)
pv3 = str(pv3)
pv4 = str(pv4)

vote1 = str(vote1)
vote2 = str(vote2)
vote3 = str(vote3)
vote4 = str(vote4)
total_votes = str(total_votes)

# opening a txt file with content for Election Results 
file = open("Output.txt", "a")
file.writelines("Election Results" + 
                "\n" + '.................................'
                "\n" + "Total Votes: " + total_votes + 
                "\n" + '.................................' +
                "\n" + candidate1 + ": " + pv1 + "%" + " (" + vote1 + ")" + 
                "\n" + candidate2 + ": " + pv2 + "%" + " (" + vote2 + ")" + 
                "\n" + candidate3 + ": " + pv3 + "%" + " (" + vote3 + ")" + 
                "\n" + candidate4 + ": " + pv4 + "%" + " (" + vote4 + ")" + 
                '\n' + '.................................'
                "\n" + "\n" + "Winner: " + winner + '\n' + '.................................')                
file.close()