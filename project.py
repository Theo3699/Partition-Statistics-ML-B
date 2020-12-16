import os
import pathlib
import wx
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import os.path
from os import path


# def get_size(start_path = '.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             # skip if it is symbolic link
#             if not os.path.islink(fp):
#                 total_size += os.path.getsize(fp)
#
#     return total_size


def checkifPartition(path):
    count=0
    for letter in path:
        if letter.isalpha():
            count+=1
    if (count!=1):
        return False
    return True

def percentage(part, whole):
    return 100 * float(part)/float(whole)


def folders_files_count(path):
    countDirs = 0
    countFiles = 0
    myDict = dict()
    print(path)
    os.chdir(path)
    for root, dirs, files in os.walk("."):
        print(root)
        for directory in dirs:
            countDirs += 1
        for filenames in files:
            countFiles += 1
    auxList=list()
    auxList.append(countFiles)
    auxList.append(countDirs)
    myDict["files"]=countFiles
    myDict["folders"]=countDirs
    print("Sunt ", countFiles, " fisiere si ", countDirs, " foldere")
    fig, ax = plt.subplots(1, 1)
    ax.bar(myDict.keys(), auxList)
    plt.ylabel("procentaje")
    plt.xlabel("extensii")
    title="Numarul de fisiere si directoare din "+path
    plt.title(title)
    plt.show()


def statisticsCount(path):
    countDirs=0
    countFiles=0
    myDict=dict()
    print(path)
    os.chdir(path)
    for root, dirs, files in os.walk("."):
        print(root)
        for directory in dirs:
            countDirs+=1
        for filenames in files:
            countFiles+=1
            extension=pathlib.Path(filenames).suffix
            if extension:
                print(filenames)
                if extension in myDict:
                    myDict[extension]+=1
                else:
                    myDict[extension]=1
    print("Exista ", countDirs, " directoare si ", countFiles, " fisiere in ", path)
    sortedDict=dict()
    count=0
    for keys in sorted(myDict, key=myDict.get, reverse=True):
        if (count<10):
            sortedDict[keys]=percentage(myDict[keys], countFiles)
            count+=1
    print("Aici incepe dictionarul sortat")
    percs = list()
    for keys in sortedDict:
        print(keys, sortedDict[keys], "%")
        percs.append(sortedDict[keys])
    fig,ax=plt.subplots(1, 1)
    ax.bar(sortedDict.keys(), percs)
    plt.ylabel("procentaje")
    plt.xlabel("extensii")
    title = "Procentajul extensiilor din " + path
    plt.title(title)
    plt.show()


def statisticsSize(way):
    countDirs = 0
    countFiles = 0
    countSize = 0
    myDict = dict()
    print(path)
    os.chdir(way)
    for root, dirs, files in os.walk("."):
        print(root)
        for directory in dirs:
            countDirs += 1
        for filenames in files:
            countFiles += 1
            extension = pathlib.Path(filenames).suffix
            pathFile=root+"\\"+filenames
            sizeOfFile=os.stat(pathFile).st_size
            countSize+=sizeOfFile
            if extension:
                print(filenames)
                if extension in myDict:
                    myDict[extension] += sizeOfFile
                else:
                    myDict[extension] = sizeOfFile
    print(way, " are ", countSize, " bytes")
    sortedDict = dict()
    count = 0
    for keys in sorted(myDict, key=myDict.get, reverse=True):
        if (count < 10):
            sortedDict[keys] = percentage(myDict[keys], countSize)
            count += 1
    print("Aici incepe dictionarul sortat")
    percs = list()
    for keys in sortedDict:
        print(keys, sortedDict[keys], "%")
        percs.append(sortedDict[keys])
    fig, ax = plt.subplots(1, 1)
    ax.bar(sortedDict.keys(), percs)
    plt.ylabel("procentaje")
    plt.xlabel("extensii")
    title="Procentajele de bytes din "+way
    plt.title(title)
    plt.show()


app = wx.PySimpleApp()
dialog = wx.DirDialog(None, "Selectati o partitie",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
if dialog.ShowModal() == wx.ID_OK:
    statisticsCount(dialog.GetPath())
    statisticsSize(dialog.GetPath())
    folders_files_count(dialog.GetPath())
    #print(get_size(dialog.GetPath()), 'bytes')
    checkifPartition(dialog.GetPath())
dialog.Destroy()

