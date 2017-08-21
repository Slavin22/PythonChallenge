import os
import csv

txtpath = os.path.join('Resources', 'TextFile.txt')
letters = 0

with open(txtpath, newline = "") as textfile:
	text = textfile.read()
	sentences = text.split(". ")
	words = text.split(" ")

	for word in words:
		ltrs = list(word)
		letters = letters + len(ltrs)

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(len(sentences)))
print("Approximate Sentence Count: " + str(len(words)))
print("Average Letter Count: " + str(letters / len(words)))
print("Average Sentence Length: " + str(len(words) / len(sentences)))
