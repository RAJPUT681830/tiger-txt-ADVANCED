import os

API_ID = API_ID = 23435751

API_HASH = os.environ.get("API_HASH", "2345de86dfb7ec6ef52ee0c16dd11dea")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6693068734:AAFqThIBhnYV4YeYpE_VgQ_-QOxT58_3ZZ8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6795199928))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6795199928").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


