#PyBank

#imports
import pathlib
import csv

#input/output paths
input_path = pathlib.Path("Resources/budget_data.csv")
output_path = pathlib.Path("Analysis/results.txt")

#make dictionary for result values
result_values = {
                "total_months": 0, 
                "total": 0, 
                "average_change": None, 
                "greatest_increase_in_profits": 0,
                "greatest_decrease_in_profits": 0,
                
                }
#helper vars
prev_profit = None
total_profit_change = 0
greatest_increase_month = ""
greatest_decrease_month = ""

#open input file
with open(input_path, 'r') as budget_file:

    #create reader cursor and skip the header
    reader_cursor = csv.reader(budget_file, delimiter=',')
    header = next(reader_cursor)
    profit_change = 0
    for row in reader_cursor:
        


        #count each month
        result_values["total_months"] += 1

        #calculate change in profit
        current_profit = int(row[1])
        
        #if prev_profit has been recorded
        if prev_profit != None:
            profit_change = current_profit - prev_profit
            total_profit_change += profit_change

        #record prev_profit for next loop
        prev_profit = int(row[1])


        #add money to total
        result_values["total"] += int(row[1])

        #update greatest/least change in profit
        if result_values["greatest_increase_in_profits"] < profit_change:
            result_values["greatest_increase_in_profits"] = profit_change
            greatest_increase_month = row[0]
        if result_values["greatest_decrease_in_profits"] > profit_change:
            result_values["greatest_decrease_in_profits"] = profit_change
            greatest_decrease_month = row[0]

       
        

#calculate average change in profit
result_values["average_change"] = round(total_profit_change / (result_values["total_months"] - 1), 2)

#result in lines
result_lines = [
                "Financial Analysis", 
                "-------------------------",
                f'Total Months: {result_values["total_months"]}',
                f'Total: ${result_values["total"]}',
                f'Average Change: ${result_values["average_change"]}',
                f'Greatest Increase in Profits: {greatest_increase_month} ${result_values["greatest_increase_in_profits"]}',
                f'Greatest Decrease in Profits: {greatest_decrease_month} ${result_values["greatest_decrease_in_profits"]}',
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


