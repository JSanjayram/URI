import yt_dlp
import itertools
import time

# List of proxy servers
proxies = [
    'http://89.116.34.113:80',
    'http://219.65.73.81:80',
    'http://103.163.244.212:82',
    'http://14.143.130.210:80'
]

# Create an iterator to cycle through the proxies
proxy_pool = itertools.cycle(proxies)

def get_audio_url(video_id):
    for _ in range(len(proxies)):
        proxy = next(proxy_pool)
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'proxy': proxy,
            'socket_timeout': 30,  # Increase timeout to 30 seconds

        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                result = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
                if 'formats' in result:
                    audio_url = result['formats'][0]['url']
                    return audio_url
            except Exception as e:
                print(f"Error with proxy {proxy}: {e}")
                time.sleep(5)  # Wait before trying the next proxy

    raise Exception("All proxies failed.")

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
