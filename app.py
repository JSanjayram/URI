from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route('/get-stream-url', methods=['GET'])
def get_stream_url():
    video_id = request.args.get('QqEarYb0Uaw')  # Pass video_id as a query parameter
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        stream_url = info.get('url')
        return jsonify({'stream_url': stream_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

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
