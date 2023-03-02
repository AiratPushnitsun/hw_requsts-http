# Задача №1
import requests
from pprint import pprint


url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url=url)
res = response.json()

def super_hero_dict(res):
    hero = ['Hulk', 'Captain America', 'Thanos']
    hero_dict = {}
    for dict in res:
        if dict['name'] in hero:
            hero_dict.setdefault(dict['name'], dict['powerstats']['intelligence'])
    max_intelligence = max(hero_dict.values())
    name_max_intelligence = max(hero_dict, key=hero_dict.get)
    print(f'Герой {name_max_intelligence} имеет наибольший показатель intelligence = {max_intelligence}')



if __name__ == '__main__':
    super_hero_dict(res)



# Задача №2
TOKEN = ''


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл успешно загружен'
        else:
            return 'Ошибка при загрузке файла'


if __name__ == '__main__':
    ya = YaUploader(TOKEN)
    pprint(ya.upload_file_to_disk(disk_file_path='geely.jpg',
                                  filename='C:/Users/Ryze/Desktop/geely.jpg'))