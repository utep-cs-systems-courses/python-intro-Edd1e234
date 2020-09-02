
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
    words = re.split("[\W+\s]", open(input_text_file, "r").read())
    for word in words:
        if word.lower() in dic:
            dic[word.lower()] += 1
        else:
            dic[word.lower()] = 1
    dic.pop('', None)
    return dic

def write_to_output_file(dic, output_file):
    output_file = open(output_file, "w")
    for word in sorted(dic.keys()):
        output_file.write(word.lower() + " " + str(dic[word.lower()]) + "\n")
    output_file.close()


def main():
    input_text_file, output_text_file = check_if_files_are_present()
    write_to_output_file(
                open_file_and_count_words(input_text_file), output_text_file)

main()
