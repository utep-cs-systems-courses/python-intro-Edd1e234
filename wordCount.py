
import sys
import re
import os


def check_if_files_are_present():
    if len(sys.argv) is not 3:
        print("Correct usage: wordCount.py <input text file> " \
            "<output text file>")

    input_text_file = sys.argv[1]
    output_text_file = sys.argv[2]

    if not os.path.exists(input_text_file):
        print ("text file input %s doesn't exist! Exiting" % input_text_file)
        exit()
    if not os.path.exists(output_text_file):
        print ("text file output %s doesn't exist! Exiting" % output_text_file)
        exit()

    return input_text_file, output_text_file

def open_file_and_count_words(input_text_file):
    dic = {}

    # Open and split by line.
    for line in open(input_text_file, "r").read().split("\n"):
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

def write_to_output_file(dic, output_file):
    output_file = open(output_file, "w")
    for word in dic.keys():
        output_file.write(word + " " + str(dic[word]) + "\n")
    output_file.close()


def main():
    input_text_file, output_text_file = check_if_files_are_present()
    write_to_output_file(
                open_file_and_count_words(input_text_file), output_text_file)

    # Read and count file.
    print("Success!")

main()
