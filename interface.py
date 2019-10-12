# Copyright and patents pending Jonathan Bannon Maher Corporation
# Inventor and author Jonathan Bannon Maher
# User interface for the control of autonomously discovered consumer electronics.


# import libraries enabling a http server

from flask import Flask
from flask import request
from flask import Response


# define a function that handles server requests

@application.route('/*', methods=['GET'])
def display():

    # define the default usernames and passwords for the devices

    username = "admin"
    password = "admin"

    # create variables holding any command and IP address provided by the user

    command = request.parameters("command")
    ip_address = request.parameters("ip_address")

    # proceed if a command was executed by the user

    if command:

        # if the command is to refresh the list of devices and their available commands,
        # execute a command line call to execute the device discovery script

        if command == "refresh":
            os.execute("python device_scanner.py")

        # proceed if the command is not to refresh

        if not command == "refresh":

            # if the request protocol is http or https, compile a url to make the request

            request = ""
            if protocol == "http" or protocol == "https":
                request = "http://" + ip_address + "/?command=" + command
                if protocol == "https":
                    request = request.replace("http:","https:")
                urllib.open(url)

            # if protocol is telnet or ssh connect and execute the command line call

            if protocol == "telnet" or protocol == "ssh":
                port = 23
                request = "automation " + command
                if protocol == "ssh":
                    port = 22
                connection = telnetlib.Telnet(ip, port)
                connection.read_until(b"User Name: ") 
                connection.write(
                    username.encode('ascii') + b"\n")
                connection.read_until(b"Password: ") 
                connection.write(
                    password.encode('ascii') + b"\n")
                connection.write(
                    request.encode('ascii') + b"\n")

    # read the list of all available commands from all devices from the text file created by the
    # device discovery script

    commands = open("commands.txt").split("\n")

    # create a variable storing the output display and building the header

    output = "<html><head><title>Device Controller</title></head><body>"

    # iterate through each command

    for command in commands:

        # build a button to execute the command and add it to the display

        output += '<table><tr style=\"background:black\" onclick=\"javascript('
        output += 'http://localhost/api/?ip_address=' + ip_address + '&'
        output += 'command=' + command_code + ')\"><td>$command_name</td></tr></table>'

    # display the output screen to the user

    return output

    
