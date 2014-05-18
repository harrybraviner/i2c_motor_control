#! /usr/bin/python

"""Command line based robot controller."""

from motorControl import motorControlBoard

# Setup
mb = motorControlBoard(0xa0)
quit = False

helpString = "Commands are:\nfore [time]\t-\tDrive forward for [time] seconds.\nstop\t-\tStop."

while(not quit):
    instruction = raw_input(">> ")  # Get a command string from the user
    instruction = instruction.lower().split()
    if len(instruction) > 0:
        if instruction[0] == 'help':
            print helpString
        if instruction[0] == 'stop':
            mb.set_speeds(0x00, 0x00)
    elif len(instruction) > 1:
        if instruction[0] == 'fore':
            mb.set_speeds(0xff, 0xff)
