import music21

s = music21.converter.parse('searle_mydayofcarnage.xml')

for part in s.parts:
    p = part.flat
    print p.id
    for n in p.getElementsByClass(music21.note.Note):
        print n.duration, n.offset
