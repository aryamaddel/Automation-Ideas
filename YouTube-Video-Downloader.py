from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=0tUqIHwHDEc")  # Video URL
print(video.thumbnail_url)
print(video.length + " seconds")

print(video.title)
print("downloading...")

stream = video.streams.get_highest_resolution()
stream.download(output_path='/Users/aryamaddel/Downloads')

print('Downloaded successfully!')
