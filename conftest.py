import os
import pytest
from dotenv import load_dotenv
from api.yandex_disk import YandexDisk

load_dotenv()


@pytest.fixture(scope="session")
def disk_client():
    token = os.getenv("YANDEX_DISK_TOKEN")
    if not token:
        raise ValueError("Токен или .env файл не найден.")
    return YandexDisk(token)