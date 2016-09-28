import sys
import os
import math

ham_cnt = 0
spam_cnt = 0
spam_word_count = 0
ham_word_count = 0
ham_dict = {}
spam_dict = {}
ham_prob = 0
spam_prob = 0
distinct_words = 0

def main(filepath):
    global ham_cnt,spam_cnt, spam_word_count, ham_word_count, spam_dict, ham_dict, ham_prob, spam_prob, distinct_words
    file = open("nbmodel.txt")
    spam_cnt = int(file.readline())
    ham_cnt = int(file.readline())
    spam_word_count = int(file.readline())
    ham_word_count = int(file.readline())
    spam_dict = eval(file.readline())
    ham_dict = eval(file.readline())
    spam_prob = float(file.readline())
    ham_prob = float(file.readline())
    distinct_words = int(file.readline())
    file.close()
    output = open("nboutput.txt","w")
    for folder, dirs, files in os.walk(filepath):
        for train_file in files:
            path = os.path.join(folder,train_file)
            if path.find(".txt") != -1:
                evaluate(path, output)
    output.close()


def evaluate(file, output):
    global spam_dict, ham_dict, spam_prob, ham_prob, spam_word_count, ham_word_count, distinct_words
    filedata = open(file, "r", encoding = "latin1")
    email = filedata.read()
    filedata.close()
    words = email.split()
    spam = 0
    ham = 0
    for word in words:
        if word in spam_dict and word in ham_dict:
            spam = spam + math.log(spam_dict[word])
            ham = ham + math.log(ham_dict[word])
        elif word in spam_dict:
            spam = spam + math.log(spam_dict[word])
            ham = ham + math.log(1/(ham_word_count+distinct_words))
        elif word in ham_dict:
        	spam = spam + math.log(1/(spam_word_count+distinct_words))
        	ham = ham + math.log(ham_dict[word])
    if spam_prob == 0:
        spam = 0
    else:
        spam = spam + math.log(spam_prob)
    if ham_prob == 0:
        ham = 0
    else:
        ham = ham + math.log(ham_prob)
    if float(spam) > float(ham):
        output.write("spam ")
        output.write(file)
    else:
        output.write("ham ")
        output.write(file)	
    output.write("\n")


if __name__ == '__main__':
    main(sys.argv[1])