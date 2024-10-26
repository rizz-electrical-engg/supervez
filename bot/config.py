from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

try:
    APP_ID = int(os.getenv("APP_ID", "21857983"))
    API_HASH = os.getenv("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7637275116:AAH7rLUqCTJJHv_FXwNdZKlPxt5FiOjZtik")
    OWNER = os.getenv("OWNER", "833465134").split()
    FILE_CHANNEL = os.getenv("FILE_CHANNEL", "-1002297251125")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title= 𝙏𝙂: 𝘼𝙣𝙞𝙢𝙚 𝙊𝙧𝙗𝙞𝙩𝙨 (https://t.me/AnimeOrbits)' -pix_fmt yuv420p -crf 26 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = os.getenv("THUMBNAIL", "https://envs.sh/A3M.jpg")
    DEV = "1664850827"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
