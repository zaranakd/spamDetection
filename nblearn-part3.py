import sys
import os
import re

spam_cnt = 0
ham_cnt = 0
spam_word_count = 0
ham_word_count = 0
spam_dict = {}
ham_dict = {}
full_dict = {}
stop_words = ["a","the","an","is","was","and","or","are","i"]

def main(filepath):
    global ham_cnt, ham_dict, ham_word_count, spam_cnt, spam_dict, spam_word_count, full_dict
    for folder, dirs, files in os.walk(filepath):
        for train_file in files:
            path = os.path.join(folder,train_file)
            if path.find("/spam/") != -1:
                spam_file(path)
            else:
                ham_file(path)
    change_to_probability(spam_dict,spam_word_count)
    change_to_probability(ham_dict,ham_word_count)
    file = open("nbmodel.txt","w")
    file.write(str(spam_cnt))
    file.write("\n")
    file.write(str(ham_cnt))
    file.write("\n")
    file.write(str(spam_word_count))
    file.write("\n")
    file.write(str(ham_word_count))
    file.write("\n")
    file.write(str(spam_dict))
    file.write("\n")
    file.write(str(ham_dict))
    file.write("\n")
    file.write(str((spam_cnt)/(spam_cnt+ham_cnt)))
    file.write("\n")
    file.write(str((ham_cnt)/(spam_cnt+ham_cnt)))
    file.write("\n")
    file.write(str(len(full_dict)))
    file.write("\n")
    file.close();
    

def ham_file(path):
    global ham_cnt, ham_dict, ham_word_count, full_dict
    if path.find(".txt") != -1:
        ham_cnt = ham_cnt + 1
        file = open(path, "r", encoding = "latin1")
        email = file.read()
        email = email.lower()
        email = re.sub(r'[^\w\s]','',email)
        words = email.split()
        ham_word_count = ham_word_count + len(words)
        count_words(words,ham_dict)   
        count_words(words,full_dict)   
        file.close()
        

def spam_file(path):  
    global spam_cnt, spam_dict, spam_word_count, full_dict    
    if path.find(".txt") != -1:
        spam_cnt = spam_cnt + 1 
        file = open(path, "r", encoding = "latin1")
        email = file.read()
        email = email.lower()
        email = re.sub(r'[^\w\s]','',email)
        words = email.split()
        spam_word_count = spam_word_count + len(words)
        count_words(words,spam_dict)
        count_words(words,full_dict)
        file.close()
        

def count_words(word_list,dict):
    for word in word_list:
        if chk_word(word):
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

def chk_word(word):
    global stop_words
    if word in stop_words:
        return False
    return True

def change_to_probability(dict,count):
    for word,cnt in dict.items():
        dict[word] = (cnt+1)/(count+len(full_dict))


if __name__ == '__main__':
    main(sys.argv[1])