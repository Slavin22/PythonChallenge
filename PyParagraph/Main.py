import os
import csv

txtpath = os.path.join('Resources', 'paragraph_1.txt')
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

outpath = os.path.join('Resources', 'ParagraphOutFile.txt')

out = open(outpath, 'w')
out.write("Paragraph Analysis" + "\n")
out.write("-----------------" + "\n")
out.write("Approximate Word Count: " + str(len(sentences)) + "\n")
out.write("Approximate Sentence Count: " + str(len(words)) + "\n")
out.write("Average Letter Count: " + str(letters / len(words)) + "\n")
out.write("Average Sentence Length: " + str(len(words) / len(sentences)))
