from os import environ

API_ID = int(environ.get("API_ID", "5466820"))
API_HASH = environ.get("API_HASH", "d0ba91990e9ccb9a53885a71564bf11c")
BOT_TOKEN = environ.get("BOT_TOKEN", "8294653330:AAHpdL78zTn_82p-iyESlU6mpYspgXs-T_M")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002602280579"))
ADMINS = int(environ.get("ADMINS", "1786851907"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
