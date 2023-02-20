import argparse
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Define argument parser to accept user input
parser = argparse.ArgumentParser(description='Download YouTube video and/or transcript')
parser.add_argument('--url', type=str, help='YouTube video URL')
args = parser.parse_args()

# Prompt user to enter URL if not provided as an argument
if not args.url:
    url = input('Paste YouTube video URL: ')
else:
    url = args.url

# Parse video ID from URL
video_id = url.split('v=')[1]

# Prompt user to choose what to download
print('Select download option:')
print('1. Video')
print('2. Transcript')
print('3. Video and transcript')
choice = int(input('Enter choice (1/2/3): '))

# Download video
if choice in (1, 3):
    # Get highest resolution stream
    stream = YouTube(url).streams.get_highest_resolution()

    # Download video
    video_filename = f'{video_id}.mp4'
    stream.download(output_path='.', filename=video_filename)
    print(f'Video saved to {video_filename}')

# Download transcript
if choice in (2, 3):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_filename = f'{video_id}.txt'
        with open(transcript_filename, 'w', encoding='utf-8') as f:
            for line in transcript:
                f.write(line['text'] + '\n')
        print(f'Transcript saved to {transcript_filename}')
    except:
        print('Automatic captions are not available for this video.')

