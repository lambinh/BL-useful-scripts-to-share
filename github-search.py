import requests
from tabulate import tabulate

def search_github(search_string):
    # Set the headers for the request
    headers = {'Accept': 'application/vnd.github+json'}
    # Construct the URL for the search request with the user's input
    url = 'https://api.github.com/search/repositories?q=' + search_string
    # Send the GET request to the GitHub API
    r = requests.get(url, headers=headers)
    # Get the list of repositories from the JSON response
    repos = r.json()['items']
    table = []
    # Iterate through the repositories and add the name, html_url, and forks to the table
    for repo in repos:
        table.append([repo['name'], repo['html_url'], repo['forks']])
    # Sort the table by the number of forks in descending order
    table = sorted(table, key=lambda x: x[2], reverse=True)
    # Print the table in a readable format using the tabulate library
    print(tabulate(table, headers=["Name", "html_url", "forks"],tablefmt="pretty"))

if __name__ == "__main__":
    # Prompt the user to enter a search string
    search_string = input("Enter a search string: ")
    # Call the search_github function with the user's input
    search_github(search_string)
