import music21

s = music21.converter.parse('searle_mydayofcarnage.xml')

p = s.parts[1].flat

for thing in p:
    if isinstance(thing, music21.note.Note):
        print thing
