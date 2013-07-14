import json
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

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
wait = float((1/float(tempo))*60.0)

print "tempo ",tempo,"; seconds gap ",wait

#test digi leds
GPIO.output(7,True)
GPIO.output(11,True)
GPIO.output(15,True)
time.sleep(3)
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(15,False)

#pwn stuff
r = GPIO.PWM(7,50)
g = GPIO.PWM(11,50)
b = GPIO.PWM(15,50)
r.start(0)
g.start(0)
b.start(0)

#test leds
for dc in range(0, 101, 5):
    r.ChangeDutyCycle(dc)
    g.ChangeDutyCycle(dc)
    b.ChangeDutyCycle(dc)
    time.sleep(0.5)
    print dc

r.ChangeDutyCycle(0)
g.ChangeDutyCycle(0)
b.ChangeDutyCycle(0)

time.sleep(3)

#loop
for i in xrange(0,max(times.keys(),key=int)):
    if i in times:
        if 'strings' in times[i]:
            duty = float(times[i]['strings'])/float(maxim['strings'])
            print times[i]['strings'], maxim['strings'], duty
            r.ChangeDutyCycle(duty*100.0)
        else:
            print 0
            r.ChangeDutyCycle(0.0)

        if 'woodwind' in times[i]:
            duty = float(times[i]['woodwind'])/float(maxim['woodwind'])
            print times[i]['woodwind'], maxim['woodwind'], duty
            g.ChangeDutyCycle(duty*100.0)
        else:
            print 0
            g.ChangeDutyCycle(0.0)

        if 'brass' in times[i]:
            duty = float(times[i]['brass'])/float(maxim['brass'])
            print times[i]['brass'], maxim['brass'], duty
            b.ChangeDutyCycle(duty*100.0)
        else:
            print 0
            b.ChangeDutyCycle(0.0)

    else:
        r.ChangeDutyCycle(0.0)
        g.ChangeDutyCycle(0.0)
        b.ChangeDutyCycle(0.0)

    time.sleep(wait)
    print "..."

GPIO.cleanup()
