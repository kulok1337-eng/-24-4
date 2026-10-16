import os

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "8991440368:AAEe5iSnY94xAfK71RsZs3zZQ6WcKc2q2j8")

# ID администраторов: Артём (диспетчер) и владелец
ARTEM_ID = 5742960391
OWNER_ID = 1979046241

ADMIN_IDS = [ARTEM_ID, OWNER_ID]

# Процент комиссии мастерам по умолчанию
DEFAULT_COMMISSION_PERCENT = float(os.getenv("DEFAULT_COMMISSION_PERCENT", "10.0"))
