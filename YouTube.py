from pytube import YouTube

link = "https://www.youtube.com/watch?v=your_video_id"
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download Complete!")
