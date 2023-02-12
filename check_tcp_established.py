import os
import re
import json
import urllib.request
import platform
from prettytable import PrettyTable

# Function to get the geolocation information of an IP address
def get_ip_geo(ip):
    # Make a request to the IP info API
    url = 'http://ipinfo.io/' + ip + '/json'
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)
        org = data['org']
        city = data['city']
        country = data['country']
        region = data['region']

        # Return the organization, city, country, and region of the IP
        return org, city, country, region
    except:
        # Return None if the request fails
        return None, None, None, None

# Function to get the established connections from the system
def get_established_connections():
    # Get the netstat command based on the platform
    if platform.system() == 'Windows':
        netstat_command = "netstat -na | findstr ESTABLISHED"
    else:
        netstat_command = "netstat -na | grep ESTABLISHED"

    # Run the netstat command and retrieve its output
    netstat_output = os.popen(netstat_command).read()

    # Split the output into lines
    lines = netstat_output.split("\n")

    # Create a list to store the established connections
    connections = []

    # Parse the output to extract the foreign host IP and application port
    for line in lines:
        # Use regular expression to match the foreign host IP and port
        match = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d+) +(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d+) +.*", line)
        if match:
            foreign_ip = match.group(3)
            port = match.group(4)
            connections.append((foreign_ip, port))

    # Remove duplicate IP addresses
    unique_connections = set(connections)

    # Return the unique connections
    return unique_connections

# Get the established connections
connections = get_established_connections()

# Create the table using the PrettyTable library
table = PrettyTable()
table.field_names = ["Foreign Host", "Application Port", "Organization", "City", "Country"]

# Add each connection's information to the table
for connection in connections:
    foreign_ip, port = connection
    org, city, country, region = get_ip_geo(foreign_ip)
    table.add_row([foreign_ip, port, org if org else "", city if city else "", country if country else ""])

# Print the table
print(table)
