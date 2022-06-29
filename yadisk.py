import requests


def make_folder(folder_name):
    with open('tkn.ya.txt', 'r') as tk:
        token_ya = tk.read().strip()
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token_ya)
    }
    params = {"path": folder_name}
    response = requests.put(url, headers=headers, params=params)
    return response.json()


if __name__ == '__main__':
    print(make_folder('new_folder'))
