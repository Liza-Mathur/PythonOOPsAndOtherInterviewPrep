import os 

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

if __name__=="__main__":
    filepathText = "./PythonText.txt"
    numberOfWords(filepathText)