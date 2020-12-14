import os
import pathlib
import wx
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)


def statistics(path):
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
    plt.title("statistica")
    plt.show()

app = wx.PySimpleApp()
dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
if dialog.ShowModal() == wx.ID_OK:
    statistics(dialog.GetPath())
dialog.Destroy()
