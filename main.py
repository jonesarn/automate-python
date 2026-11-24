import netmiko
import os
from getpass import getpass # since I dont have a router
# 1. Enter the lab device's IP address, username, and device type.

host = input("Enter the lab device's IP address: ")
username = input("Enter the username: ")
password = getpass("Enter the password: ")   

cisco_device ={
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password
}

# Next step
print(f'Ready to connect:{cisco_device['host']} as {cisco_device["username"]}')
