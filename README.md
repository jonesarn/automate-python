# Netmiko Configuration Backup

By Armond Jones

## Project Goal

I'm building a Python tool that connects to Cisco IOS lab devices over SSH, saves their running configurations, and uses Git to flag changes between backups. Git history will show which lines were added or removed.

## Current Progress

I installed Netmiko and tested the prompts for the device IP address, username, and password. The next step is to collect a sample running configuration through a mock connection.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install netmiko
```

## Planned Workflow

1. `main.py` collects the device details and opens an SSH session.
2. `config_backup.py` runs `show running-config` and returns the output.
3. Save the output to a separate `.cfg` file for each device.
4. Commit the first backup to a private local Git repository as the baseline.
5. Compare later backups with the last committed version. Report whether each backup is new, changed, unchanged, or failed. Commit new or changed backups.

## Test Plan

- [ ] Use a mock connection to return a sample running configuration.
- [ ] Save and commit the first sample as the baseline.
- [ ] Run with identical output and verify that no new commit is created.
- [ ] Change one line and verify that Git shows the difference.
- [ ] Simulate a failed connection and verify that the previous backup is preserved.
- [ ] Test against one Cisco IOS lab device before expanding to multiple devices.

## Config Storage

This public repository uses fictional sample configurations. Real backups stay in a separate local Git repository because running configurations can contain secrets and internal network details.