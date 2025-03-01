import yt_dlp

def get_audio_url(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',  # Prefer audio format
        'quiet': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',
        'socket_timeout': 60,


    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
        if 'formats' in result:
            # Extract the best audio stream URL
            audio_url = result['formats'][0]['url']
            return audio_url

video_id = "QqEarYb0Uaw"  # Example video ID
audio_url = get_audio_url(video_id)
print(audio_url)


"""from flask import Flask, jsonify
import yt_dlp
video_url = 'https://www.youtube.com/watch?v=QqEarYb0Uaw'
ydl_opts = {
        'format': 'bestaudio/best',
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    audio_url = info_dict.get('url', None)
    print({"audio_url": audio_url})"""
