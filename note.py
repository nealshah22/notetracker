import json
from datetime import datetime

def readNotes(f):
    return json.load(f)

def printNotes(notes):
    for note in notes:
        print("-"*25, "\n")
        print("id: ", note["id"], "\n")
        print("Title: ","\n"," ", note["title"], "\n")
        print("Date: ","\n"," ", datetime.fromtimestamp(note["date"] / 1e9).strftime("%m-%d-%Y %H:%M:%S"), "\n")
        print("Category: ", "\n"," ", ", ".join(note["categories"]), "\n")
        print("Body: ", "\n"," ", note["body"], "\n")

def sortNotes(notes,key,order):

    for i in range(len(notes)):
        min_idx = i
        for j in range(i+1, len(notes)):
            if order == "asc":
                if notes[min_idx][key] > notes[j][key]:
                    min_idx = j
            else:
                if notes[min_idx][key] < notes[j][key]:
                    min_idx = j


        notes[i], notes[min_idx] = notes[min_idx], notes[i]

    return notes
