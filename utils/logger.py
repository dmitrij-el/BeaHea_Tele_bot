# app/utils/logger.py

import logging

# Простая настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Создаем логгер для использования в проекте
logger = logging.getLogger("app")
