
import sys
import re
import os


def check_if_files_are_present():
    if len(sys.argv) is not 2:
        print("Correct usage: wordCount.py <input text file>")

    textFname = sys.argv[1]

    if not os.path.exists(textFname):
        print ("text file input %s doesn't exist! Exiting" % textFname)
        exit()

    return textFname

def open_file_and_count_words():
    textFname = check_if_files_are_present()
    open_text_file = open(textFname, "r")
    lines = open_text_file.read().split("\n")

    dic = {}

    # Spliting by line, then by sentence, then by comma, then finally by space.
    for line in lines:
        sentences = line.split(".")
        for sentence in sentences:
            statements = sentence.split(",")
            for statement in statements:
                words = statement.split(" ")
                for word in words:
                    if word in dic:
                        dic[word] = dic.get(word) + 1
                    else:
                        dic[word] = 1
    return dic

def write_to_output_file(dic):
    output_file = open("output.txt", "w")
    for word in dic.keys():
        output_file.write(word + " " + str(dic[word]) + "\n")
    output_file.close()


def main():
    write_to_output_file(open_file_and_count_words())

    # Read and count file.
    print("Hello World")

main()
