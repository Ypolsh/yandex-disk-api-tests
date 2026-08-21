import requests


class YandexDisk:
    BASE_URL = "https://cloud-api.yandex.net"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"OAuth {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_resource_info(self, path):
        return requests.get(
            f"{self.BASE_URL}/v1/disk/resources",
            headers=self.headers,
            params={"path": path},
        )

    def create_folder(self, path):
        return requests.put(
            f"{self.BASE_URL}/v1/disk/resources",
            headers=self.headers,
            params={"path": path},
        )

    def delete_resource(self, path):
        return requests.delete(
            f"{self.BASE_URL}/v1/disk/resources",
            headers=self.headers,
            params={"path": path},
        )

    def upload_file_from_url(self, path, url):
        return requests.post(
            f"{self.BASE_URL}/v1/disk/resources/upload",
            headers=self.headers,
            params={"path": path, "url": url},
        )

    def upload_file_from_disk(self, path, file_path):
        response = requests.get(
            f"{self.BASE_URL}/v1/disk/resources/upload",
            headers=self.headers,
            params={"path": path},
        )

        if response.status_code != 200:
            return response

        upload_url = response.json()["href"]

        with open(file_path, "rb") as f:
            return requests.put(upload_url, files={"file": f})

    def get_disk_info(self):
        return requests.get(
            f"{self.BASE_URL}/v1/disk",
            headers=self.headers,
        )