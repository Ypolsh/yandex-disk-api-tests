# Яндекс.Диск API — автотесты

**Проект:** Автоматизированные тесты для REST API Яндекс.Диска  
**Стек:** Python + pytest + requests  
**API:** https://cloud-api.yandex.net

---

## О проекте

Данный репозиторий содержит набор API-тестов, покрывающих основные методы Яндекс.Диска: GET, POST, PUT, DELETE.

Тесты проверяют:
- Получение информации о Диске и ресурсах
- Создание папок
- Загрузку файлов
- Удаление ресурсов
- Негативные сценарии

---

## Требования

- Python 3.11+
- Токен Яндекс.Диска (OAuth)

---

## Получение токена

1. Создайте OAuth-приложение с правами:
   - `cloud_api:disk.read`
   - `cloud_api:disk.write`
   - `cloud_api:disk.info`
   - `cloud_api:disk.app_folder`
   Инструкция: [Регистрация приложения для доступа к API](https://yandex.ru/dev/id/doc/ru/register-api)
2. Получите токен по инструкции: [Доступ к API Яндекс.Диска](https://yandex.ru/dev/disk-api/doc/ru/concepts/quickstart)
3. Создайте в корне проекта файл `.env`:

```
YANDEX_DISK_TOKEN=ваш_токен
```
---

## Установка

```bash
pip install -r requirements.txt
```

---

## Запуск тестов

```bash
pytest
```

Просмотреть отчет:

```bash
start report.html
```

---