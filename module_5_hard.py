# Задача "Свой YouTube"

import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):               # Имя пользователя в строковом виде
        return str(self.nickname)

    def __hash__(self):              # Пароль в хэшированном виде
        return hash(self.password)

    def __int__(self):               # Возраст в целочисленном виде
        return int(self.age)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):               # Название видео в строковом виде
        return str(self.title)

    def __int__(self):               # Продолжительность видео и текущая секунда просмотра в целочисленном виде
        return int(self.duration, self.time_now)


class UrTube:
    def __init__(self):
        self.users = []              # Список пользователей
        self.videos = []             # Список видеозаписей
        self.current_user = None     # Текущий пользователь платформы

    def log_in(self, nickname, password):   # Замена текущего пользователя
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age): # Регистрация нового пользователя и автоматический вход
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.log_out()
        self.log_in(user.nickname, user.password)

    def log_out(self):                           # Сброс текущего пользователя
        self.current_user = None

    def add(self, *args):                        # Добавление видеозаписей в список с пропуском дубликатов
        for video in args:
            if video in self.videos:
                continue
            else:
                self.videos.append(video)

    def get_videos(self, word):                  # Поиск видео по словам
        list_of_coincidence = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                list_of_coincidence.append(video.title)
        return list_of_coincidence

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if title == video.title:
                to_watch = video
                if self.current_user.age < 18 and to_watch.adult_mode is True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                else:
                    while to_watch.time_now < to_watch.duration:
                        to_watch.time_now += 1
                        print(to_watch.time_now)
                        time.sleep(1)
                    print('Конец видео')
                    to_watch.time_now = 0



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')