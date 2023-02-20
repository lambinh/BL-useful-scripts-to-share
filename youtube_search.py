import googleapiclient.discovery
import argparse
from prettytable import PrettyTable
import locale

#Youtube API Document: https://developers.google.com/youtube/v3/docs/?apix=true 

# Set the locale for comma separators
locale.setlocale(locale.LC_ALL, '')

# Define argument parser to accept user input
parser = argparse.ArgumentParser(description='Search for YouTube videos')
parser.add_argument('--query', type=str, help='Search query')
args = parser.parse_args()

# Prompt user to enter search query if not provided as an argument
if not args.query:
    query = input("Enter search query: ")
else:
    query = args.query

# Prompt user to choose between sorting by view count or by relevance
sort_by_view_count = None
while sort_by_view_count not in ('y', 'n'):
    sort_by_view_count = input("Sort by view count? (y/n): ")
sort_by_view_count = sort_by_view_count == 'y'

# Read API key from file
with open('youtube.api', 'r') as f:
    api_key = f.read().strip()

# Set up YouTube Data API client
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

# Execute search request
search_response = youtube.search().list(
    q=query,
    type='video',
    order='viewCount' if sort_by_view_count else 'relevance',
    part='id,snippet',
    maxResults=10
).execute()

# Retrieve video details for each search result
videos = []
for search_result in search_response.get('items', []):
    video_id = search_result['id']['videoId']
    video_title = search_result['snippet']['title']
    video_response = youtube.videos().list(
        id=video_id,
        part='contentDetails'
    ).execute()
    video_duration = video_response['items'][0]['contentDetails']['duration'][2:]
    videos.append((video_id, video_title, video_duration))

# Retrieve video statistics for each search result
video_stats_response = youtube.videos().list(
    id=','.join([video[0] for video in videos]),
    part='statistics'
).execute()

# Process search results and create table
table = PrettyTable(['Video Title', 'View Count', 'Duration', 'URL'])
for video, video_stats in zip(videos, video_stats_response.get('items', [])):
    video_title = video[1]
    if 'statistics' in video_stats:
        view_count = int(video_stats['statistics']['viewCount'])
        view_count_str = locale.format_string("%d", view_count, grouping=True)
    else:
        view_count_str = 'N/A'
    video_duration = video[2]
    url = f"https://www.youtube.com/watch?v={video[0]}"
    table.add_row([video_title, view_count_str, video_duration, url])

# Print table
if sort_by_view_count:
    print(f'Search results for "{query}" sorted by view count:')
else:
    print(f'Search results for "{query}" sorted by relevance:')
print(table)

