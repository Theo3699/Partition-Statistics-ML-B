import os
import pathlib

def percentage(part, whole):
    return 100 * float(part)/float(whole)


def statistics(path):
    countDirs=0
    countFiles=0
    myDict=dict()
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            countDirs+=1
        for filenames in files:
            countFiles+=1
            extension=pathlib.Path(filenames).suffix
            if not extension:
                print(os.path.abspath(filenames))
                print(filenames)
            if extension in myDict:
                myDict[extension]+=1
            else:
                myDict[extension]=1
    print("Exista ", countDirs, " directoare si ", countFiles, " fisiere")
    for keys in myDict:
        print(keys, percentage(myDict[keys], countFiles), "%")

statistics("D:\\")
