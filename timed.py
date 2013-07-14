import json
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

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
        #print part
    
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

tempo = 80

for i in xrange(0,max(times.keys(),key=int)):
    if i in times:
        if 'strings' in times[i]:
            print times[i]['strings'], maxim['strings'], float(times[i]['strings'])/float(maxim['strings'])
            GPIO.output(7,True)
        else:
            print 0
            GPIO.output(7,False)
        if 'woodwind' in times[i]:
            print times[i]['woodwind'], maxim['woodwind'], float(times[i]['woodwind'])/float(maxim['woodwind'])
            GPIO.output(11,True)
        else:
            print 0
            GPIO.output(11,False)
        if 'brass' in times[i]:
            print times[i]['brass'], maxim['brass'], float(times[i]['brass'])/float(maxim['brass'])
            GPIO.output(15,True)
        else:
            print 0
            GPIO.output(15,False)
    wait = float((1/float(tempo))*60.0)
    time.sleep(wait)
    print "...",wait

GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(15,False)

