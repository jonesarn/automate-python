import main
from netmiko import ConnectHandler 

with ConnectHandler(**main.cisco_device) as conn:
    # Run the vendor-specific CLI status command
    output = conn.send_command("show interfaces status")
    print(output)