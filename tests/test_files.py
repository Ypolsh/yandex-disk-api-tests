import os
import tempfile
import pytest


@pytest.fixture
def test_file():
    """Создание временного тестового файла для загрузки."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Я хочу попасть на стажировку в Яндекс!")
        return f.name


def test_upload_file_from_disk(disk_client, test_file):
    """PUT загрузка локального файла на Диск."""
    path = "/test_file.txt"
    disk_client.delete_resource(path)

    response = disk_client.upload_file_from_disk(path, test_file)
    assert response.status_code == 201

    info = disk_client.get_resource_info(path)
    assert info.status_code == 200
    assert info.json()["type"] == "file"

    disk_client.delete_resource(path)
    os.unlink(test_file)


def test_upload_file_to_invalid_path(disk_client):
    """PUT загрузка в несуществующую папку (негативный)."""
    response = disk_client.upload_file_from_disk("/nonexistent_folder/file.txt", "test_file.txt")
    assert response.status_code == 409


def test_upload_file_from_url(disk_client):
    """POST загрузка файла на Диск по URL."""
    path = "/file_from_url.txt"
    url = "https://example.com/file.txt"
    disk_client.delete_resource(path)

    response = disk_client.upload_file_from_url(path, url)
    assert response.status_code == 202

    disk_client.delete_resource(path)


def test_upload_file_invalid_url(disk_client):
    """POST загрузка файл с невалидным URL (негативный)."""
    path = "/file_bad_url.txt"
    url = "not-a-valid-url"

    response = disk_client.upload_file_from_url(path, url)
    assert response.status_code == 400


def test_get_disk_info(disk_client):
    """GET получение информации о Диске."""
    response = disk_client.get_disk_info()
    assert response.status_code == 200
    assert "total_space" in response.json()


def test_get_nonexistent_file_info(disk_client):
    """GET получение информации о несуществующем файле (негативный)."""
    response = disk_client.get_resource_info("/nonexistent_file_12345.txt")
    assert response.status_code == 404


