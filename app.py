import yt_dlp
import os

browser_profile = os.path.expanduser('~/.config/google-chrome/Default/Cookies')  # Adjust path for your OS

video_url = 'https://www.youtube.com/watch?v=QqEarYb0Uaw'
ydl_opts = {
        'format': 'bestaudio/best',
        'nocheckcertificate': True,
        'disable_throttling': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'geo_bypass': True,
        'cookies_from_browser': browser_profile,  # Path to browser cookies



    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    audio_url = info_dict.get('url', None)
    print({"audio_url": audio_url})
