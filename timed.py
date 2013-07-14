import json
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin1 = 7
pin2 = 11
pin3 = 15

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)

input = open('searle_mydayofcarnage.json', 'rb')
struct = json.load(input)
input.close()

input = open('searle_mydayofcarnage_conf.json', 'rb')
conf = json.load(input)
input.close()

times = {}
maxim = {}

for part in struct:
    partCase = part
    part = part.lower()
    #i know this is wrong
    section = ''
    for key in conf['sections']:
        if key in part:
            section = conf['sections'][key]
    if (section == ''):
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

tempo = conf['tempo']
wait = float((1/float(int(tempo)))*60.0)

print "tempo ",tempo," pause of ",wait

#test digi leds
GPIO.output(pin1,True)
GPIO.output(pin2,True)
GPIO.output(pin3,True)
time.sleep(3)
GPIO.output(pin1,False)
GPIO.output(pin2,False)
GPIO.output(pin3,False)

#pwn stuff
r = GPIO.PWM(pin1,50)
g = GPIO.PWM(pin2,50)
b = GPIO.PWM(pin3,50)
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

leng = max(times.keys(),key=int)

#loop
for i in xrange(0,leng):
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
