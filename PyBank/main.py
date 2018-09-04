import os
import csv

bank_csv_path = os.path.join("..","Resources","budget_data.csv")
results_txt_path = os.path.join("..","Output","budget_data_result.txt")

with open (bank_csv_path,"r",newline = "") as bankfile:
    bankreader = csv.reader(bankfile,delimiter = ",")
    bankheader = next(bankreader)                #read header
    row = next(bankreader)                       #read first row
    profit_loss = float(row[1])
    tot_months = 1                                 #set initial values
    tot_profit_loss = profit_loss
    sum_of_change = 0
    if profit_loss >0 :
        greatest_profit=profit_loss
        great_profit_date = row[0]
        greatest_loss=0
        great_loss_date = " "    
    elif profit_loss <0 :
        greatest_profit = 0
        great_profit_date = " "          
        greatest_loss=profit_loss
        great_loss_date = row[0]

    for row in bankreader:                          # loop through rows
        change = float(row[1]) - profit_loss       # calculate change from previous month
        sum_of_change += change
        tot_months += 1
        profit_loss = float(row[1])                 #set new values for running totals
        tot_profit_loss = tot_profit_loss + profit_loss
        if profit_loss > greatest_profit:
                greatest_profit=profit_loss
                great_profit_date = row[0]
        if profit_loss < greatest_loss:
                greatest_loss=profit_loss
                great_loss_date = row[0]
result=[]                                                   #prepare results
result.append("    Financial Analysis")
result.append("-----------------------------")

result.append(f"    Total Months :{tot_months}")
result.append("    Total Net Profit/Loss: ${:0,.0f}".format(tot_profit_loss))
result.append("    Average Change: ${:>#11,.2f}".format(sum_of_change / (tot_months - 1)))
result.append("    Greatest Increase in Profits: {0} (${1:>#13,.0f})".format(great_profit_date,greatest_profit))
result.append("    Greatest Decrease in Profits: {0} (${1:>#13,.0f})".format(great_loss_date,greatest_loss))


for line in result:                                         #send results to terminal
    print (line)

with open (results_txt_path,"w") as resultfile:             #send results to txt file
    for line in result:
        resultfile.write(line +"\n")