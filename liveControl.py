#! /usr/bin/python

"""Command line based robot controller."""

from motorControl import motorControlBoard
import signal

# Function to be called on interrupt, stops motors
def interruptStop(signal_number, stack_frame):
    mb.set_speeds(0x00, 0x00)

# Setup
mb = motorControlBoard(0x0a)
quit = False

helpString = "Commands are:\nfore [time]\t-\tDrive forward for [time] seconds.\nstop\t-\tStop."

while(not quit):
    instruction = raw_input(">> ")  # Get a command string from the user
    instruction = instruction.lower().split()
    if len(instruction) > 1:
        # Check that the time is valid
        try:
            run_time = abs(float(instruction[1]))
        except:
            print instruction[1] + ' is not a valid time.' 
        else:
            if instruction[0] == 'fore' or instruction[0] == 'f':
                mb.set_speeds(0xff, 0xff)
                signal.setitimer(signal.ITIMER_REAL, run_time)
            if instruction[0] == 'back' or instruction[0] == 'b':
                mb.set_speeds(-0xff, -0xff)
                signal.setitimer(signal.ITIMER_REAL, run_time)
            if instruction[0] == 'left' or instruction[0] == 'l':
                mb.set_speeds(-0xff, 0xff)
                signal.setitimer(signal.ITIMER_REAL, run_time)
            if instruction[0] == 'right' or instruction[0] == 'r':
                mb.set_speeds(0xff, -0xff)
                signal.setitimer(signal.ITIMER_REAL, run_time)
    elif len(instruction) > 0:
        if instruction[0] == 'help':
            print helpString
        if instruction[0] == 'stop':
            mb.set_speeds(0x00, 0x00)
        if instruction[0] == 'quit':
            quit = True

# Stop the motors before we quit
mb.set_speeds(0x00, 0x00)
