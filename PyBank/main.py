import os
import csv
csvpath = os.path.join('Resources', 'budget_data_1.csv')

months = 0
total = 0
revenues = []
comp = 0
increase = 0
decrease = 0
incmonth = ""
decmonth = ""

with open(csvpath, newline = "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	next(csvreader, None)

	for row in csvreader:
		if int(row[1]) - comp > increase:
			increase = int(row[1]) - comp
			incmonth = row[0]
		elif int(row[1]) - comp < decrease:
			decrease = int(row[1]) - comp
			decmonth = row[0]
		months = months + 1
		total = total + int(row[1])
		revenues.append(int(row[1]))
		comp = int(row[1])

average = int((revenues[months - 1] - revenues[0]) / (months - 1))

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total Revenue: $" + str(total))
print("Average Revenue Change: $" + str(average))
print("Greatest Increase in Revenue: " + incmonth + " ($" + str(increase) + ")")
print("Greatest Decrease in Revenue: " + decmonth + " ($" + str(decrease) + ")")

txtpath = os.path.join('Resources', 'BudgetDataTextFile.txt')

text = open(txtpath, 'w')
text.write("Financial Analysis" + "\n")
text.write("----------------------------" + "\n")
text.write("Total Months: " + str(months) + "\n")
text.write("Total Revenue: $" + str(total) + "\n")
text.write("Average Revenue Change: $" + str(average) + "\n")
text.write("Greatest Increase in Revenue: " + incmonth + " ($" + str(increase) + ")" + "\n")
text.write("Greatest Decrease in Revenue: " + decmonth + " ($" + str(decrease) + ")" + "\n")
