#Matteo Luleich
import urllib.request
from inscriptis import get_text
import wx
import wx.grid
import requests
out=open("output.txt","w+")
csv=open("table.csv","w+")
filepath=input("Filepath(.txt/url): ")
if filepath=="":
    filepath="http://www.google.com"
#filepath="http://www.informationscience.ch"
if filepath.startswith("https://") or filepath.startswith("http://") or filepath.startswith("www"):
    #uf = urllib.request.urlopen(filepath)
    #lread = uf.read()
    #print(lread)
    #exit(1)
    #html = lread.decode("utf-8")
    #file=get_text(html)
    #fl=file.lower()
    resp = requests.get(filepath)
    html = resp.text
    file=get_text(html)
    fl=file.lower()
else:
    file=open(filepath,"r")
    fl=file.read().lower()

wordlist = []
count = []
numandword=[]
counter=0
fl.replace("^|"," ")
fr=fl.replace("."," ").replace("|"," ").replace("â€¢"," ").replace("»"," ").replace("▼"," ").replace("{"," ").replace("}"," ").replace("+"," ").replace("'"," ").replace("="," ").replace("*"," ").replace("â€™"," ").replace("â­"," ").replace(":"," ").replace("ã–","ö").replace("\\","").replace("/","").replace("&"," und ").replace("<"," ").replace(">"," ").replace("ã„","ä").replace("â€˜"," ").replace("â€š"," ").replace("â€¦"," ").replace("["," ").replace("]"," ").replace(";"," ").replace("â€ž"," ").replace("â€œ"," ").replace("â€“"," ").replace("ã©","e").replace("\n"," ").replace("ã¶","ö").replace("ã¼","ü").replace("ã¤","ä").replace("ãÿ","ß").replace("â€ž"," ").replace("("," ").replace(")"," ").replace(","," ").replace("-"," ").replace("\""," ").replace("?"," ").replace("!"," ").replace("  "," ")
fs=fr.split()

for e in fs:
    #counter=counter+1
    if e not in wordlist:
        wordlist.append(e)
        count.append(fs.count(e))
        warsch=round((100*fs.count(e))/len(fs),3)
        #print(warsch)
        numandword.append([e,fs.count(e),warsch])

def sortSecond(val):
    return val[1]


numandword.sort(key=sortSecond,reverse=True)
numandword.insert(0,["Wort","Anzahl des Worts","Anteil am Text"])
#

class GridFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent)

        grid= wx.grid.Grid(self,-1)
        grid.CreateGrid(len(numandword),3)
        grid.SetColSize(1,90)
        grid.SetCellValue(0,0,"Wort")
        grid.SetCellValue(0,1,"Anzahl des Worts")
        grid.SetCellValue(0,2,"Anteil am Text")

        for s in range(len(numandword)):
            for r in range(0,3):
                if r==0:
                    grid.SetCellValue(s,0,str(numandword[s][0]))
                if r==1:
                    grid.SetCellValue(s, 1, str(numandword[s][1]))
                if r==2:
                    grid.SetCellValue(s, 2, str(numandword[s][2]))
        self.Show()


if __name__=='__main__':

    app=wx.App(0)
    frame=GridFrame(None)
    app.MainLoop()



for i in range(len(numandword)):
    out.write(str(numandword[i][0])+"\t\t"+str(numandword[i][1])+"\t\t"+str(numandword[i][2])+"\n")
    csv.write(str(numandword[i][0])+";"+str(numandword[i][1])+";"+str(numandword[i][2])+"\n")
    print(str(numandword[i][0])+"\t\t"+str(numandword[i][1])+"\t\t"+str(numandword[i][2])+"\n")