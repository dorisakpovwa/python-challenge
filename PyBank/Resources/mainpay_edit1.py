import os
import csv
#set the variables
bankdata = 'budget_data.csv'

totalmonths = 0
netprofit = 0
greatestI = ["", 0]
greatestD = ["", 9999999999999999999]

#set path to read file
with open(bankdata, "r") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
#initialize list
    firstrow = next(csvreader)
    totalmonths += 1
    netprofit += int(firstrow[1])
    prev_net = int(firstrow[1])
    pl = [int(firstrow[1])]
    changes = []
    monthofchange = []
 #loop through rows and columns and perform iterations
    for row in csvreader:
        totalmonths += 1
        netprofit += int(row[1])
        monthofchange += [row[0]]   

        ch = int(row[1]) - prev_net
        prev_net = int(row[1])

        changes += [ch]

 # Calculate the greatest increase and greatest decrease
        if ch > greatestI[1]:
            greatestI[0] = row[0]
            greatestI[1] = ch

        if ch < greatestD[1]:
            greatestD[0] = row[0]
            greatestD[1] = ch  

    avg = sum(changes)/len(changes)
  
    print(totalmonths)
    print(avg)
    print(netprofit)
    print(greatestI)
    print(greatestD)

#set path to write changes to csv
output_file = os.path.join("final_analysis.csv")
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % totalmonths)
    file.write("Total Profit: $%d\n" % netprofit)
    file.write("Average Change $%d\n" % avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatestI[0], greatestI[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatestD[0], greatestD[1]))



  

