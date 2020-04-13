#PyPoll

#imports
import pathlib
import csv

#input/output paths
input_path = pathlib.Path("Resources/election_data.csv")
output_path = pathlib.Path("Analysis/results.txt")

#result values
total_votes = 0
vote_nums = {
            "Khan" : 0,
            "Correy" : 0,
            "Li" : 0,
            "OTooley" : 0,
            "other" : 0,
            }

#helper vars

#open input file
with open(input_path, 'r') as election_data_file:

    #create reader cursor and skip the header
    reader_cursor = csv.reader(election_data_file, delimiter=',')
    header = next(reader_cursor)
    profit_change = 0
    for row in reader_cursor:
        
        total_votes += 1

        if row[2] == 'Khan':
            vote_nums["Khan"] += 1
        elif row[2] == 'Correy':
            vote_nums["Correy"] += 1
        elif row[2] == 'Li':
            vote_nums["Li"] += 1
        elif row[2] == "O'Tooley":
            vote_nums["OTooley"] += 1
        else:
            vote_nums["other"] += 1


vote_percents = {
                 "Khan" : 0.0,
                "Correy" : 0.0,
                "Li" : 0.0,
                "OTooley" : 0.0,
                "other" : 0.0,
                }

for key in vote_percents:
    vote_percents[key] = round(100 * (float(vote_nums[key]) / float(total_votes)), 3)
        
#calculate winner
winner = ''
for key in vote_nums:
    if winner == '':
        winner = key
    if vote_nums[key] > vote_nums[winner]:
        winner = key

#result in lines
result_lines = [
                "Election Results", 
                "-------------------------",
                f'Total Votes: {total_votes}',
                "-------------------------",
                f'Khan: {vote_percents["Khan"]}% ({vote_nums["Khan"]})',
                f'Correy: {vote_percents["Correy"]}% ({vote_nums["Correy"]})',
                f'Li: {vote_percents["Li"]}% ({vote_nums["Li"]})',
                f'O\'Tooley: {vote_percents["OTooley"]}% ({vote_nums["OTooley"]})',
                f'Other: {vote_percents["other"]}% ({vote_nums["other"]})',
                "-------------------------",
                f"Winner: {winner}",
                "-------------------------",
                ]

#print results to terminal
for result in result_lines:
    print(result)

# write results to file
result_file = open(output_path, 'w')

for line in result_lines:
    result_file.write(line)
    result_file.write('\n')

result_file.close()


