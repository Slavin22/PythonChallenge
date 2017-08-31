# Import Dependencies + load file-path
import os
import csv
txtpath = os.path.join('Resources', 'paragraph_1.txt')

# Establish variables
letters = 0

# Read in CSV file, then split data into sentences + words
with open(txtpath, newline = "") as textfile:
	text = textfile.read()
	sentences = text.split(". ")
	words = text.split(" ")

	# Get letter count
	for word in words:
		ltrs = list(word)
		letters = letters + len(ltrs)

# Print results
print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(len(sentences)))
print("Approximate Sentence Count: " + str(len(words)))
print("Average Letter Count: " + str(letters / len(words)))
print("Average Sentence Length: " + str(len(words) / len(sentences)))

# Print results to output file
outpath = os.path.join('Resources', 'ParagraphOutFile.txt')

out = open(outpath, 'w')
out.write("Paragraph Analysis" + "\n")
out.write("-----------------" + "\n")
out.write("Approximate Word Count: " + str(len(sentences)) + "\n")
out.write("Approximate Sentence Count: " + str(len(words)) + "\n")
out.write("Average Letter Count: " + str(letters / len(words)) + "\n")
out.write("Average Sentence Length: " + str(len(words) / len(sentences)))
