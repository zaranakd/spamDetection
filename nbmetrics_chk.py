import sys
import os

dict = {}
classified_spam = 0
classified_ham = 0
corr_classified_spam = 0
corr_classified_ham = 0
is_spam = 0
is_ham = 0


def chk_classification(file):
    global dict, classified_spam, classified_ham
    for line in file:
        temp = line.index(" ")
        dict[line[temp+1:-1]] = line[:temp]
        if line[:temp] == "spam":
            classified_spam = classified_spam + 1
        else:
            classified_ham = classified_ham + 1


def spam_file(train_file):
    global dict, corr_classified_spam, is_spam
    is_spam = is_spam + 1
    if dict[train_file] == "spam":
        corr_classified_spam = corr_classified_spam + 1


def ham_file(train_file):
    global dict, corr_classified_ham, is_ham
    is_ham = is_ham + 1
    if dict[train_file] == "ham":
        corr_classified_ham = corr_classified_ham + 1

    
def chk_correct(filepath):
    for folder, dirs, files in os.walk(filepath):
        for train_file in files:
            path = os.path.join(folder,train_file)
            if path.find(".txt") != -1:
                if path.find("/spam/") != -1:
                    spam_file(path)
                else:
                    ham_file(path)


def main(filepath):
    global corr_classified_spam,corr_classified_ham, classified_spam, classified_ham, is_spam, is_ham
    file = open("nboutput.txt","r")
    chk_classification(file)
    file.close()
    chk_correct(filepath)
    spam_prec = corr_classified_spam / classified_spam
    spam_recall = corr_classified_spam / is_spam
    spam_f1 = (2*spam_prec*spam_recall) / (spam_prec + spam_recall)
    print("spam precision: %.2f" % round(spam_prec,2))
    print("spam recall: %.2f" % round(spam_recall,2))
    print("spam F1: %.2f" % round(spam_f1,2))
    ham_prec = corr_classified_ham / classified_ham
    ham_recall = corr_classified_ham / is_ham
    ham_f1 = (2*ham_prec*ham_recall) / (ham_prec + ham_recall)
    print("ham precision: %.2f" % round(ham_prec,2))
    print("ham recall: %.2f" % round(ham_recall,2))
    print("ham F1: %.2f" % round(ham_f1,2))
    


if __name__ == '__main__':
    main(sys.argv[1])