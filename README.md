Creative Carnage
================
Visualisation of musical instrumentation via Raspberry Pi from a Sibelius/MusicXML file via Python/Music21

![Final](/photos/finalSmall.jpg)

Components
----------
- Python
- MusicXML
- Music21
- JSON
- Raspberry Pi
- RPi.GPIO/PWM

![Instruments Laser Template](/laser/instrumentsSmall.png)

![Prototype](/photos/prototype.jpg)

Process
-------
1. Export MusicXML from Sibelius via Dolet plugin
2. convert.py with Python and Music21
3. timed.py on Raspberry Pi with RPi.GPIO PWM
4. Play performance audio as the LEDs perform (3 seconds after lights out)

![Score](/photos/score.png)

Hardware Setup
--------------
Red, Green, Blue LEDs with standard series resistors on Raspberry Pi pins 7, 11, 15

![Genesis](/photos/genesis.jpg)

Thoughts
--------
1. Should parse MusicXML for tempo (but keep base units in JSON as quarter lengths for nicest resolution).
   How can we visualise the differences between music as written and as performed ("My Day of Carnage" tempo was marked as 80 but performance works out at 84).
2. Could account for musical dynamics (need to parse more parts of the MusicXML with Music21).
   The code counts instruments and notes/rhythm within each beat and visualises this as LED intensity.

Credits
-------
- Chris Glasgow @scottishmusic
- Gavin Leake @galvanist
- Gillian Easson @GillianEasson

![Cleaning](/photos/cleaning.jpg)

Thanks
------
- Flux Laser Studio @fluxlaserstudio
- Oliver Searle of @scottishmusic
- Team Sync @synchq
- The Whisky Bond @WhiskyBond
- Chris Scott @chrisdonia http://www.flickr.com/photos/chrisdonia/sets/72157634618539409/

Detailed Process
----------------
1. Export MusicXML from Sibelius via Dolet plugin
2. convert.py with Python and Music21
    1. Import MusicXML file into Python via Music21 (some files with percussion elements are not supported)
    2. Parse the tree/structure for note elements (be sure to exclude rests)
    3. Get the duration (in quarter lengths) and offset (again in quarter lengths) into structure
    4. Save structure to JSON
3. timed.py on Raspberry Pi with RPi.GPIO PWM
    1. Load JSON
    2. Group tracks into sections (defined in _conf.json)
    3. For each beat save number of instruments and notes
    4. Save maximum number of previous per section for any beat in track (used to fade/scale LED)
    5. Figure wait time (in seconds) from tempo
    6. Test LEDs (on/off/fade, like a orchestra would warming up pre performance)
    7. Fade the LEDs and pause after each beat as appropriate
4. Play performance audio as the LEDs perform (3 seconds after lights out)
