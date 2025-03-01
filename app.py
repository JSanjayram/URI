import yt_dlp
video_url = 'https://www.youtube.com/watch?v=QqEarYb0Uaw'
ydl_opts = {
        'format': 'bestaudio/best',
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    audio_url = info_dict.get('url', None)
    print({"audio_url": audio_url})
