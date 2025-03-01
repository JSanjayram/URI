import os
import yt_dlp
from flask import Flask

app = Flask(__name__)

@app.route('/download/<video_id>')
def download(video_id):
    ydl_opts = {
          'format': 'bestaudio/best',
          'quiet': True,
          'proxy': 'http://your_proxy_address:port',  # Replace with your proxy details
          'socket_timeout': 60,
      }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
            if 'formats' in result:
                audio_url = result['formats'][0]['url']
            return audio_url
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


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
