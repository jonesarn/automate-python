# Netmiko Network Automation Project
By Armond Jones
## Project Goal
I am building a python script that uses netmiko to connect to a lab router or switch over SSH and check which interfaces are up or down
## Setup
Create a Python virtual environment and install Netmiko:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install netmiko
```

## How It Will Work

1. Enter the lab device's IP address, username, and device type.
2. Enter the SSH password when the script prompts for it.
3. Connect to the device and run a read-only command. On Cisco IOS,
   the first command will be `show ip interface brief`.
4. Print the interface status and close the SSH session.

## Test Plan

- [ ] Connect to one lab device over SSH.
- [ ] Compare the script output with the command run manually.
- [ ] Check that an unreachable host and incorrect credentials produce
      distinct error messages.
- [ ] Add a sample output with private device details removed.

## Next Milestone

After the single-device check works, run it against a small lab
inventory and summarize which devices response