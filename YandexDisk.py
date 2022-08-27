import requests
from pprint import pprint
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
            }
            params = {"path": disk_file_path, "overwrite": "true"}
            response = requests.get(upload_url, headers = headers, params=params)
            pprint(response.json())
            return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
            href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
            response = requests.put(href, data=open(filename, 'rb'))
            print(response.content)
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "Файлик.docx"
    filename = "Файлик.docx"
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(path_to_file, filename)
