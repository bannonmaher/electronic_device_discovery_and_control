# Copyright and Patents Pending Jonathan Bannon Maher Corporation
# Inventor and author Jonathan Bannon Maher
# This software provides for the autonomous discover of electronic devices,
# along with their available commands, through network and device scanning.


# import the libraries to connect to devices through popular protocols including telnet, ssh, http, and https

import telnetlib
import ssh
import urllib


# specify devices username and password

username = "admin"
password = "admin"

# open the commands file for overwriting

commands_file = open("commands","w+")

# create a variable holding the base of the IP address for the local area network

ip_base = "192.168.0."

# create an array to hold all possible IP addresses on the local network

ips = []

# generate all possible local network IP address and add them to the IP address array

index = 1
while index <= 255:
    ips.append(ip_base + str(index))
    index+=1

# iterate through each local IP address

for ip in ips:

    # try to retrieve a list of commands for each through each http, https, telnet, ssh,
    # and record which protocol worked

    protocol = ""
    commands = ""
    url = "https:" + "//" + ip + "/?" + username + "=" + username + "&password=" + password
    commands = urllib.open(url)
    if commands:
        protocol = "https"
    if not commands:
        commands = urllib.open(url.replace("https","http"))
        commands = urllib.open(url)
    if commands:
        protocol = "http"
    if not commands:
        connection = telnetlib.Telnet(ip, 23)
    if connection:
        protocol = "telnet"
    if not connection:
        connection = telnetlib.Telnet(ip, 556)
    if connection:
        protocol = "ssh"
    if connection:
        connection.read_until(b"User Name: ") 
        connection.write(
            username.encode('ascii') + b"\n")
        connection.read_until(b"Password: ") 
        connection.write(
            password.encode('ascii') + b"\n")
        command = "automation commands"
        commands = connection.write(
            command.encode('ascii') + b"\n")

        # if commands were provided by the device, write each commands to the commands file

        commands_entry = ""
        commands = commands.split("\n")
        for command in commands:
            available_commands = protocol + " " + ip + " " + command

        # write the available commands to the commands file

        commands_file.write(commands_entry)
        commands_file.close()

