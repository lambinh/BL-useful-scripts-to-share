import requests
import socket
import whois
import subprocess

# Function to extract domain information such as WHOIS information and IP address
def get_domain_info(url):
    # Splitting the URL to extract the domain
    domain = url.split("/")[2]
    # Using the "whois" library to retrieve WHOIS information for the domain
    whois_info = whois.whois(domain)
    # Using the "socket" library to retrieve the IP address for the domain
    ip_address = socket.gethostbyname(domain)
    # Return the extracted information
    return domain, whois_info, ip_address

# Function to extract information about the URL
def get_url_info(url):
    # Using the "requests" library to retrieve information about the URL
    response = requests.head(url, allow_redirects=True)
    # Extracting the full URL after following any redirects
    full_url = response.url
    # Checking if the URL is safe (returns a status code of 200)
    is_safe = True if requests.get(full_url).status_code == 200 else False
    # Extracting domain information using the "get_domain_info" function
    domain, whois_info, ip_address = get_domain_info(full_url)
    # Using the "subprocess" library to run a whois command on the IP route object
    ip_ro = subprocess.run(["whois", "-h", "rr.ntt.net", ip_address], stdout=subprocess.PIPE).stdout.decode("utf-8")
    # Extracting the headers of the response
    headers = response.headers
    # Return all the extracted information
    return full_url, is_safe, domain, whois_info, ip_address, ip_ro, headers

# Getting the input URL from the user
short_url = input("Enter a shorten URL: ")
# Extracting information about the URL using the "get_url_info" function
full_url, is_safe, domain, whois_info, ip_address, ip_ro, headers = get_url_info(short_url)

# Printing all the extracted information
print("The full URL is:", full_url)
print("The URL is safe:", is_safe)
print("The domain is:", domain)
print("The WHOIS information for the domain is:", whois_info)
print("The IP address of the host is:", ip_address)
print("The IP route object is:")
print(ip_ro)
print("The headers of the response are:")
print("Header Name".ljust(20, " ") + "Value")
print("-" * 40)
for header, value in headers.items():
    print(header.ljust(20, " ") + value)
