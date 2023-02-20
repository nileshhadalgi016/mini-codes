from pytube import YouTube

# Replace the URL with the YouTube video you want to download
url = 'https://www.youtube.com/watch?v=xxxxxxx'

# Create a YouTube object
video = YouTube(url)

# Get the audio stream with the highest bitrate
audio_stream = video.streams.filter(only_audio=True).order_by('bitrate').desc().first()

# Download the audio to the current working directory
audio_stream.download()

"""
Additionally, if you want to download only the audio of the YouTube video,
you can use the audio_streams attribute of the YouTube object and choose
a specific audio stream to download.

In this case, we're using the filter() method to select only audio streams, 
then we're ordering the results by bitrate in descending order (so the highest
bitrate audio stream is first), and finally we're selecting the first audio
stream in the list.

"""