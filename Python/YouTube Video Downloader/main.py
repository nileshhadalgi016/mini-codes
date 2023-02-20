from pytube import YouTube

# Replace the URL with the YouTube video you want to download
url = 'https://www.youtube.com/watch?v=xxxxxxx'

# Create a YouTube object
video = YouTube(url)

# Get the first stream (usually the highest quality video)
stream = video.streams.first()

# Download the video to the current working directory
stream.download()

"""
Note that the above code downloads the video to the current working directory.
You can also specify a different download directory by passing a file path
to the download() method.
"""