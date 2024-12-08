# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26276229"))
API_HASH = getenv("API_HASH", "13aa2e24b15711f6a2213bf8cae0dfdd")
BOT_TOKEN = getenv("BOT_TOKEN", "7880590069:AAHskWwL-Xh8lUCc6_LmAS0ifJkAcFAdrkg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6492395259").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://varmaabhishek97:IhsVfeCDv96pIJD5@cluster0.a6eid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002478829559")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002478829559"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
