import os
import csv
csvpath = os.path.join('Resources', 'election_data_2.csv')

total = 0
candidates = []
numcand = 0
votes = []

with open(csvpath, newline = "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	next(csvreader, None)

	for row in csvreader:
		total = total + 1
		if row[2] in candidates:
			votes[candidates.index(row[2])] = votes[candidates.index(row[2])] + 1
		else:
			candidates.append(row[2])
			votes.append(1)
			numcand = numcand + 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
winningvotes = 0
winner = ""
for num in range(0, numcand):
	if votes[num] > winningvotes:
		winningvotes = votes[num]
		winner = candidates[num]
	print(candidates[num] + ": " + str(int((votes[num] / total) * 100)) + "% (" + str(votes[num]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

txtpath = os.path.join('Resources', 'ElectionDataTextFile.txt')

text = open(txtpath, 'w')
text.write("Election Results" + "\n")
text.write("-------------------------" + "\n")
text.write("Total Votes: " + str(total) + "\n")
text.write("-------------------------" + "\n")
for num in range(0, numcand):
	text.write(candidates[num] + ": " + str(int((votes[num] / total) * 100)) + "% (" + str(votes[num]) + ")" + "\n")
text.write("-------------------------" + "\n")
text.write("Winner: " + winner + "\n")
text.write("-------------------------")

