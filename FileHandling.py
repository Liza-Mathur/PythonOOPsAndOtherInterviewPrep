import os 
import pandas as pd
import csv
import re

def numberOfWords(filepath):
    with open(filepath) as f:
        countLines = 0
        wordsCount = 0
        charCount = 0
        while(True):
            l = f.readline()
            if l == "":
                break
            else: 
                strArray = l.split(" ")
                wordsCount += len(strArray)
                l = l.replace(" ", "")
                charCount += len(l)
                countLines += 1
        print("Lines - ", countLines)
        print("Words - ", wordsCount)
        print("Characters - ", charCount)

        f.seek(0)
        countLines = 0
        wordsCount = 0
        charCount = 0

        for line in f:
            countLines += 1
            wordsCount += len(line.split())   # Handles any space/tab
            charCount += len(line.replace(" ", ""))
        print("Lines - ", countLines)
        print("Words - ", wordsCount)
        print("Characters - ", charCount)

def csvFileToDict(filepath):
    # option one to use pandas to read file
    file = pd.read_csv(filepath)
    # print(file.to_dict())
    # print(file.to_dict(orient="split"))
    # print(file.to_dict(orient="index"))
    print(file.to_dict(orient="records"))

    print("App 2")
    # another approach
    with open(filepath) as f:
        t = csv.DictReader(f)
        data = []
        for i in t:
            data.append(i)
        print(data)

def extractEmailsFromFile(filepath):
    emails = []
    with open(filepath) as f:
        r = f.readlines()
        for k in r:
            s = re.findall("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", k)
            for j in s:
                emails.append(j)
    print(emails)

if __name__=="__main__":
    filepathText = "./PythonText.txt"
    numberOfWords(filepathText)

    # 2
    csvFileToDict("L:\PythonInterviewPrep\MethodsOOPsErrorsFilesPython\StudentDetails.csv")

    # 3
    extractEmailsFromFile('./emails.txt')