import pytest


@pytest.fixture
def test_folder(disk_client):
    """Создание тестовой папки и ее удаление после теста."""
    path = "/test_folder"
    disk_client.delete_resource(path) 
    disk_client.create_folder(path)
    yield path
    disk_client.delete_resource(path)


def test_get_resource_info(disk_client, test_folder):
    """GET запрос о существующей папке."""
    response = disk_client.get_resource_info(test_folder)
    assert response.status_code == 200
    assert response.json()["name"] == "test_folder"


def test_get_nonexistent_resource(disk_client):
    """GET запрос о несуществующей папке (негативный)."""
    response = disk_client.get_resource_info("/nonexistent_folder_12345")
    assert response.status_code == 404


def test_create_folder(disk_client):
    """PUT создание папки."""
    path = "/created_folder"
    disk_client.delete_resource(path)

    response = disk_client.create_folder(path)
    assert response.status_code == 201

    info = disk_client.get_resource_info(path)
    assert info.status_code == 200
    assert info.json()["type"] == "dir"

    disk_client.delete_resource(path)


def test_create_folder_invalid_name(disk_client):
    """PUT создание папки с невалидным именем (негативный)."""
    path = "/invalid/folder///!№;%name"
    response = disk_client.create_folder(path)
    assert response.status_code == 404


def test_delete_folder(disk_client):
    """DELETE удаление папки."""
    path = "/folder_to_delete"
    disk_client.delete_resource(path)
    disk_client.create_folder(path)

    response = disk_client.delete_resource(path)
    assert response.status_code == 204

    info = disk_client.get_resource_info(path)
    assert info.status_code == 404


def test_delete_nonexistent(disk_client):
    """DELETE удаление несуществующего ресурса (негативный)."""
    response = disk_client.delete_resource("/nonexistent_to_delete")
    assert response.status_code == 404