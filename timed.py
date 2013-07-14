import json

input = open('searle_mydayofcarnage.json', 'rb')
struct = json.load(input)
input.close()

times = {}
maxim = {}

for part in struct:
    partCase = part
    part = part.lower()
    if 'flute' in part:
        section = 'woodwind'
    elif 'piccolo' in part:
        section = 'woodwind'
    elif 'clarinet' in part:
        section = 'woodwind'
    elif 'oboe' in part:
        section = 'woodwind'
    elif 'bassoon' in part:
        section = 'woodwind'
    elif 'trumpet' in part:
        section = 'brass'
    elif 'trombone' in part:
        section = 'brass'
    elif 'tuba' in part:
        section = 'brass'
    elif 'trumpet' in part:
        section = 'brass'
    elif 'violin' in part:
        section = 'strings'
    elif 'chello' in part:
        section = 'strings'
    elif 'violo' in part:
        section = 'strings'
    elif 'bass' in part:
        section = 'strings'
    elif 'horn' in part:
        section = 'brass'
    else:
        section = 'generic'
        print part
    
    if not section in maxim:
        maxim[section] = 0
    
    for note in struct[partCase]:
        offset = int(note[0])
        duration = int(note[1])
        for i in xrange(0,duration):
            pos = offset+i
            try:
                times[pos][section] += 1
            except:
                try:
                    times[pos][section] = 1
                except:
                    times[pos] = {}
                    times[pos][section] = 1
            if times[pos][section] > maxim[section]:
                maxim[section] = times[pos][section]

print maxim

print max(times.keys(),key=int)
