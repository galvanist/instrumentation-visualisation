import music21

s = music21.converter.parse('searle_mydayofcarnage.xml')

def flatPrint(myList):
    for thing in myList:
        if isinstance(thing, list):
            flatPrint(thing)
        else:
            print(thing)

flatPrint(s.parts[1])
