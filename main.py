from netmiko import ConnectHandler
from getpass import getpass

ip = input("Enter the IP address of the WLC: ")
username = input("Enter your SSH username: ")
password = getpass("Enter your SSH password: ")

wlc = {
    "device_type" : "cisco_ios",
    "ip" : ip,
    "username" : username,
    "password" : password,
    "port" : 22
}

net_connect = ConnectHandler(**wlc)
ap_sum = net_connect.send_command("show ap summary")

#save the output of the first column beginning with the seventh line to a list called aps.

aps = []
ap_sum = ap_sum.split("\n")
for line in ap_sum[7:]:
    words = line.split()
    if words:  # Check if the list is not empty
        aps.append(words[0])

# Loop through the list of APs and check the fabric status of each AP
for ap in aps:
    output = net_connect.send_command(f"show ap name {ap} config general | i Fabric")
    # the following line will print the AP name and the output of the command in a pretty table
    status = output.split()
    print("{:18} {:15} {:8}".format(ap, "Fabric Status:",status[3]))

net_connect.disconnect()

