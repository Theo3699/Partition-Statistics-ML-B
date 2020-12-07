import os

countDirs=0
countFiles=0
for root, dirs, files in os.walk("D:\\"):
    for directory in dirs:
        print(directory)
        countDirs+=1
    for filenames in files:
        print(filenames)
        countFiles+=1
print("Exista ", countDirs, " directoare si ", countFiles, " fisiere")