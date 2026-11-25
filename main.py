from netmiko import ConnectHandler 
from getpass import getpass # this will hide the password as you type it
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


