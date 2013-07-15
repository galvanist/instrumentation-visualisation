import music21

s = music21.converter.parse('searle_mydayofcarnage.xml')

t = {}

for part in s.parts:
    p = part.flat
    name = p.id
    t[name] = []
    for n in p.getElementsByClass(music21.note.Note):
        print name, n.duration.quarterLength, n.offset
        t[name].append([n.offset,n.duration.quarterLength])

print t