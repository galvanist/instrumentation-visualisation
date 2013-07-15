from xml.dom.minidom import parse, parseString

def get_step(note):
    stepNode = note.getElementsByTagName("step")[0]
    #get the text from the Text Node within the <step>,
    #and convert it from unicode to ascii
    return str(stepNode.childNodes[0].nodeValue)

def get_alter(note):
    alters = note.getElementsByTagName("alter")
    if len(alters) == 0:
        return None
    return alters[0]

def is_rest(note):
    return len(note.getElementsByTagName("rest")) > 0

def is_accidental(note):
    return get_alter(note) != None

dom = parse("searle_mydayofcarnage.xml")

notes = dom.getElementsByTagName("note")

print len(notes)

rests = filter(lambda note: is_rest(note), notes)
print len(rests)

notes = filter(lambda note: not is_rest(note), notes)
print len(notes)

accidentals = filter(lambda note: is_accidental(note), notes)
print len(accidentals)

non_accidentals = filter(lambda note: not is_accidental(note), notes)
print len(non_accidentals)
