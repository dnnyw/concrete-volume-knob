import time
import board
# from digitalio import DigitalInOut, Direction
import rotaryio
import board
import digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)


# timing parameters
short_press = .25
longer_press = 1


# NEW Action Params
long_press_action = ConsumerControlCode.SCAN_PREVIOUS_TRACK
short_press_action = ConsumerControlCode.SCAN_NEXT_TRACK
single_click_action = ConsumerControlCode.PLAY_PAUSE

right = ConsumerControlCode.VOLUME_INCREMENT
left = ConsumerControlCode.VOLUME_DECREMENT

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

for i in (range(5)):

	led.value = False
	time.sleep(0.1)
	led.value = True
	time.sleep(0.1)


button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(board.D0, board.D1)

cc = ConsumerControl(usb_hid.devices)

button_state = None
last_position = encoder.position

last_click_time = None

while True:
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
        	cc.send(right)
        print(current_position)
    elif position_change < 0:
        for _ in range(-position_change):
        	cc.send(left)
        print(current_position)

    last_position = current_position
    #pressed button = false button.value

    if not button.value and button_state is None:
    	button_state = "pressed"
    	pressed_time = time.monotonic()
    	print("pressed down at ", pressed_time)

    if button.value and button_state == "pressed":
        # released button
        current_time = time.monotonic()
        print("released button at ", current_time)
        print("last_click_time is ", last_click_time)



        #check if was short press
        if current_time - pressed_time > short_press and current_time - pressed_time <= longer_press:
        	print("short press")
        	cc.send(short_press_action)



       	# check if long press
        elif current_time - pressed_time > longer_press:
        	print("long press")
        	cc.send(long_press_action)


        # if not short or long, then single click
        else:
        	print("single click")
    		cc.send(single_click_action)

       	button_state = None

    #checking that we clicked one and we haven't done any other clicks yet
    # OLD CODE
    # if click_once == True and time.monotonic() - last_click_time > double_click_wait:
    # 	print("single click")
    # 	cc.send(single_click_action)
    # 	last_click_time = time.monotonic()
    # 	click_once = False
