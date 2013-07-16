Creative Carnage
================
Visualisation of musical instrumentation via Raspberry Pi from a Sibelius/MusicXML file via Python/Music21

Built with:
- Python
- MusicXML
- Music21
- JSON
- Raspberry Pi
- RPi.GPIO/PWM

Process:
1. Export MusicXML from Sibelius via Dolet plugin
2. convert.py with Python and Music21
3. timed.py on Raspberry Pi with RPi.GPIO PWM
4. Play performance audio as the LEDs perform (3 seconds after lights out)

![Prototype](/photos/prototype.jpg)

Hardware Setup:
Raspberry Pi GPIO; 3 LEDs on pins 7, 11, 15 paired with ~150 Ohm resistors

Thoughts:
1. Should parse MusicXML for tempo (but keep base units in JSON as quarter lengths for nicest resolution).
   How can we visualise the differences between music as written and as performed ("My Day of Carnage" tempo was marked as 80 but performance works out at 84).
2. Could account for musical dynamics (need to parse more parts of the MusicXML with Music21).
   The code counts instruments and rhythm within each beat and visualises this as LED intensity.

Credits:
- Chris Glasgow @scottishmusic
- Gavin Leake @galvanist
- Gillian Easson @GillianEasson

Thanks:
- Flux Laser Studio @fluxlaserstudio
- Oliver Searle of @scottishmusic
- Team Sync @synchq
- The Whisky Bond @WhiskyBond
- Chris Scott @chrisdonia http://www.flickr.com/photos/chrisdonia/sets/72157634618539409/

Detailed Process:
1. Export MusicXML from Sibelius via Dolet plugin
2. convert.py with Python and Music21
2.1. Import MusicXML file into Python via Music21 (some files with percussion elements are not supported)
2.2. Parse the tree/structue for note elements (be sure to exclude rests)
2.3. Get the duration (in quarterLengths) and offset (again in quarterLengths) into structure
2.4. Save structure to JSON
3. timed.py on Raspberry Pi with RPi.GPIO PWM
3.1. Load JSON
3.2. Group tracks into sections (defined in _conf.json)
3.3. For each beat save number of instruments and notes
3.3. Save maximum number of previous per section for any beat in track (used to fade/scale LED)
3.4. Figure wait time (in seconds) from tempo
3.5. Test LEDs (on/off/fade, like a orchestra would warming up pre performance)
3.6. Fade the LEDs and pause after each beat as appropriate
4. Play performance audio as the LEDs perform (3 seconds after lights out)