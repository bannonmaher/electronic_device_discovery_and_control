# Copyright and patents pending Jonathan Bannon Maher Corporation
# Inventor and author Jonathan Bannon Maher
# This software responds to scans of available functionality for an electronic device,
# and in conjunction with a relay board, and executes commands on an electronic device.


# Import the library for connecting to the relay board

import serial

# create variables defining the value of relay on off states, and variables holding the relay states

on = 1
off = 0
relay_1_light_1 = off
relay_2_light_2 = off
relay_3_light_3 = off
relay_4_light_4 = off

# create a variable to hold a connection to the relay board

relay = None

# create a function to update the relay board, creating a connection first if one has not been initialized or it has been dropped, where the state of each relay in sequence is posted as a string to the relay board

def update_relays():

    if not relay:
        relay = serial.Serial()
        relay.baudrate = 9600
        relay.timeout = 0
        relay.port = "/dev/ttyUSB0"
        relay.open()

    command = str(relay_1_light_1)
    command+= str(relay_2_light_2)
    command+= str(relay_3_light_3)
    command+= str(relay_4_light_4)
    relay.write(command.encode('ascii') + b"\n")


# create a function to execute commands sent to the script on the relay control board

def main():

    # read in commands provided to the script through the command line

    arguments = sys.argv

    # print a list of available commands

    print "0 off\n1 on"

    # Set the relay states according to the provided commands and call the function to update the relay board

    relay_1_light_1 = off
    relay_2_light_2 = off
    relay_3_light_3 = off
    relay_4_light_4 = off
    update_relays()

