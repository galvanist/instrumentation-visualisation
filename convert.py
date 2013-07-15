import music21
import json

s = music21.converter.parse('searle_mydayofcarnage.xml')

struct = {}
for part in s.parts:
    p = part.flat
    name = p.id
    struct[name] = []
    for n in p.getElementsByClass(music21.note.Note):
        print name, n.duration.quarterLength, n.offset
        struct[name].append([n.offset,n.duration.quarterLength])

output = open('searle_mydayofcarnage.json', 'wb')
json.dump(struct,output)
output.close()
