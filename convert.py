import music21

s = music21.converter.parse('searle_mydayofcarnage.xml')

def printNotes(myList):
    for thing in myList:
        try:
            iterator = iter(thing)
        except TypeError:
            if isinstance(thing, music21.note.Note):
                print(thing)
        else:
            printNotes(thing)

printNotes(s.parts[1])
