from fake_useragent import UserAgent

# Создание объекта класса UserAgent - 2 способа
# ua = fake_useragent.UserAgent() - 1й способ
# или
ua = UserAgent() # 2й способ

headers = {‘user-agent’: ua.random}