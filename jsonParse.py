#import json
#import urllib.parse
import requests
import csv
import isbnlib as il
import progressbar

errorList = []
errorList2 = []
bar = progressbar.ProgressBar()
api = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

# read isbn data

with open('books.csv', 'r') as f:
    fin = csv.reader(f)
    isbnList = []
    for row in fin:
        if len(row) != 0:
            isbnList = isbnList + [row]
f.close()
with open("output.csv", "w") as f:
    fout = csv.writer(f)
    fout.writerow(["Title","Author","ISBN","Pages","Subject"])
f.close()
# google books api

for i in bar(range(len(isbnList))):
    url = api + isbnList[i][0]
    #print('\n \n \n ')
    #print(url)
    #print('\n ')
    res = requests.get(url).json()
    # print(res)
    # print('\n \n \n ')
    try:
        items = res["items"]
        bookInfo = items[0]["volumeInfo"]
        #print(bookInfo)
        with open("output.csv", "a") as f:
            fout = csv.writer(f)
            fout.writerow(
                [bookInfo["title"], bookInfo["authors"][0], isbnList[i][0], bookInfo["pageCount"], isbnList[i][1]])
        f.close()
    except Exception:
        try:
            sec = il.meta(isbnList[i][0])
            with open("output.csv","a") as f:
                fout = csv.writer(f)
                fout.writerow([sec["Title"],sec["Authors"][0],sec["ISBN-13"],'', isbnList[i][1]])
                f.close()
        except Exception:
            pass
        #print("Secondary System Engaged for: ")
        #print(isbnList[i][0])
        errorList.append([isbnList[i][0], isbnList[i][1]])
    continue

print("\nOutput is in current folder and is named output.csv \n")