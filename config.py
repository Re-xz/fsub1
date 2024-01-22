
import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6325594724:AAH-2SZRoxVdpbirNhXlyG5-uwlE7HU43CQ")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29486311"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001950756152"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1707380693"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "skandal")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://tlmyyost:P2inlcCa4QcIWDD0QvlleYEkGsjBAX2I@flora.db.elephantsql.com/tlmyyost")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "BokepTV21")
GROUP = os.environ.get("GROUP", "NegativeRoom")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002037994205"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1002018123667"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "📣<b> Viral Information Channel</b>\n  ├  🔞 @SitusLink\n  ├  🔞 @InfoColmek\n  ├  🔞 @NegativeRoom\n └  🔞 @VCSTELEGRAM\n\n⁉️  ✘   〘☏〙Contact Admin :〘☏〙\n<a href='https://t.me/BLVCKCARD'></a>  ├  ✘     ║▌│█║▌│ █║▌│█│║▌║\n  └  ✘                  SCANNING",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1707380693").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(2144447234)
ADMINS.append(5058850419)
ADMINS.append(2050266793)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
