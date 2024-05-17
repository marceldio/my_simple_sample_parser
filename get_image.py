import requests
import os


with requests.Session() as s:
    for i in range(1,161):
        URL = f"https://parsinger.ru/img_download/img/ready/{i}.png"
        s.get(URL)
        response = s.get(URL)
        if response.status_code != 200:
            continue
        else:
            data_folder = "data_get_image"
            # Проверяем, существует ли папка data
            if not os.path.exists(data_folder):
                # Если папки нет, создаем ее
                os.makedirs(data_folder)
            file_name = f'{i}.png'
            file_path = os.path.join(data_folder, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
