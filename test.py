from inputs import get_gamepad
import re

button_re = re.compile('BTN*')
dpad_re = re.compile('ABS_HAT*')

def decode_button_input(button, state):
    output = ""
    if(button == "BTN_SOUTH"):
        output = "A button "
    elif(button == "BTN_WEST"):
        output = "X button "
    elif(button == "BTN_NORTH"):
        output = "Y button "
    elif(button == "BTN_EAST"):
        output = "B button "
    elif(button == "BTN_TR"):
        output = "Right bumper "
    elif(button == "BTN_TL"):
        output = "Left bumper "
    elif(button == "BTN_THUMBL"):
        output = "Left stick "
    elif(button == "BTN_THUMBR"):
        output = "Right stick "
    elif(button == "BTN_START"):
        output = "Start button "
    elif(button == "BTN_SELECT"):
        output = "Select button "
    else:
        output = button + " "

    if(state == 1):
        output += "pressed"
    else:
        output += "released"

    print(output)

def decode_dpad_input(button, state):
    output = ""
    if(button == "ABS_HAT0X"):
        if(state == 1):
            output = "D-PAD right pressed"
        elif(state == -1):
            output = "D-PAD left pressed"
        else:
            output = "D-PAD released"
    elif(button == "ABS_HAT0Y"):
        if(state == 1):
            output = "D-PAD down pressed"
        elif(state == -1):
            output = "D-PAD up pressed"
        else:
            output = "D-PAD released"

    print(output)


exclude = re.compile('ABS_[R]?[XYZ]')
ex = re.compile('SYN_*')

while True:
    events = get_gamepad()
    for event in events:
        stick = exclude.match(event.code)
        sync = ex.match(event.code)

        button_match = button_re.match(event.code)
        dpad_match = dpad_re.match(event.code)

        # if stick == None and sync == None:
        # if(event.code == "BTN_THUMBL" or event.code == "BTN_THUMBR"):

        if button_match != None:
            decode_button_input(event.code, event.state)

        if dpad_match != None:
            decode_dpad_input(event.code, event.state)

        if event.code == "ABS_X":
            if event.state == 2**15 - 1:
                print("LEFT STICK MAX RIGHT")
            elif event.state == -(2**15):
                print("LEFT STICK MAX LEFT")

        elif event.code == "ABS_Y":
            if event.state == 2**15 - 1:
                print("LEFT STICK MAX UP")
            elif event.state == -(2**15):
                print("LEFT STICK MAX DOWN")

        if event.code == "ABS_RX":
            if event.state == 2**15 - 1:
                print("RIGHT STICK MAX RIGHT")
            elif event.state == -(2**15):
                print("RIGHT STICK MAX LEFT")

        elif event.code == "ABS_RY":
            if event.state == 2**15 - 1:
                print("RIGHT STICK MAX UP")
            elif event.state == -(2**15):
                print("RIGHT STICK MAX DOWN")

        if event.code == "ABS_Z":
            if event.state == 2**8 - 1:
                print("LEFT TRIGGER MAX")
        elif event.code == "ABS_RZ":
            if event.state == 2**8 - 1:
                print("RIGHT TRIGGER MAX")

            # if event.state != 0:
            #     print(f"EVENT CODE {event.code}")
            #     print(event.state)
