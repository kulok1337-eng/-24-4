import os

# Токен бота берётся из переменной окружения BOT_TOKEN (задаётся на хостинге)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ID администраторов: Артём (диспетчер) и владелец
ARTEM_ID = 5742960391
OWNER_ID = 1979046241

ADMIN_IDS = [ARTEM_ID, OWNER_ID]

# Процент комиссии мастерам по умолчанию
DEFAULT_COMMISSION_PERCENT = float(os.getenv("DEFAULT_COMMISSION_PERCENT", "10.0"))
