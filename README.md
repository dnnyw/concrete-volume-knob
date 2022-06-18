# Concrete Volume Knob with Seeeduino XIAO with samd21g18
 
## Instructions
1. Connect Seeeduino to computer
2. Short the RST pins on the diagram twice
3. Orange light should flicker and device will open up on computer
4. Copy CircuitPython code onto bootloader
5. Copy `adafruit_hid` into `lib` folder
6. Copy `main.py` into base directory

## Configuring Python Code 
* Change `# timing parameters` for the time in which presses are registered 
* Anything before `short_press` is considered click
* Between `short_press` and `long_press` is a short press actions
* Longer than `long_press` is a long press.
* Change action params to change what long press, short press, and click are 

