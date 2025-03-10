from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Flask app
app = Flask(__name__)
from selenium.webdriver.chrome.options import Options

def extract_audio_streaming_uri(video_id):
    """
    Use Selenium to extract the audio streaming URI from a YouTube video.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        str: The extracted audio streaming URI or None if not found.
    """
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Configure ChromeDriver options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")

    # Set up Selenium WebDriver with headless Chrome
    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
    try:
        driver.get(video_url)

        # Wait for the network requests and video element to load
        wait = WebDriverWait(driver, 10)  # Wait for 10 seconds
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))

        # Access the audio stream URI through the video tag if available
        video_element = driver.find_element(By.TAG_NAME, "video")
        audio_streaming_uri = video_element.get_attribute("src")

        if audio_streaming_uri:
            return audio_streaming_uri
        else:
            return None

    except Exception as e:
        print(f"Error extracting audio streaming URI: {e}")
        return None

    finally:
        driver.quit()

# Define the API endpoint
@app.route('/extract-audio-uri', methods=['GET'])
def api_extract_audio_uri():
    video_id = request.args.get('video_id')
    
    if not video_id:
        return jsonify({"error": "Video ID is required"}), 400

    # Call the helper function to extract the audio URI
    audio_uri = extract_audio_streaming_uri(video_id)

    if audio_uri:
        return jsonify({"audio_streaming_uri": audio_uri})
    else:
        return jsonify({"error": "Audio streaming URI could not be extracted"}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
video_id = "QqEarYb0Uaw"  # Example video ID
audio_url = get_audio_url(video_id)
print(audio_url)
"""

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
