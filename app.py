import yt_dlp
import os
from selenium import webdriver
import pickle
import time

browser_profile = os.path.expanduser('~/.config/google-chrome/Default/Cookies')  # Adjust path for your OS

# Path to your browser's webdriver (e.g., ChromeDriver)
driver_path = '/path/to/chromedriver'

# Create a new instance of Chrome (or any browser you prefer)
driver = webdriver.Chrome(driver_path)

# Open YouTube and login
driver.get('https://www.youtube.com')

# Add your login steps here (using your credentials, manual login, etc.)

# Wait for login to finish
time.sleep(10)  # Adjust time as needed for login to complete

# Save cookies to a file
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

driver.quit()
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
