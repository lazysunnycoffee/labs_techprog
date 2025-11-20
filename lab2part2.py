import requests




class MyFile:
    def __init__(self, path, mode='read'):
        self.path = path
        self.mode = mode

        valid_modes = ['read', 'write', 'append', 'url', 'r', 'w', 'a']
        if self.mode not in valid_modes:
            raise ValueError(f'Недопустимый режим: {self.mode}!')

    def read(self):
        if self.mode not in ['read', 'r']:
            print('Чтение файла возможно только в режиме read!')
            return None
        try:
            with open(self.path, mode='r') as f:
                return f.read()
        except Exception as e:
            print('Ошибка при чтении файла!', e)
            return None


    def write(self, text):
        if self.mode not in ['write', 'w', 'append', 'a']:
            print('Запись в файл возможно только в режиме write!')
            return None
        _mode = 'w' if self.mode == 'write' else 'a'
        try:
            with open(self.path, mode=_mode) as f:
                return f.write(text)
        except Exception as e:
            print('Ошибка при записи в файл!', e)
            return None


    def read_url(self):
        if self.mode != 'url':
            print('Ошибка! Работа с urls возможно только в режиме url!')
            return None
        try:
            return requests.get(self.path).text
        except Exception as e:
            print(f'Ошибка чтения сайта: {e}')
            return None

    def count_urls(self):

        site_code = self.read_url()
        if site_code is None:
            print('Ошибка чтения кода страницы!')
            return None
        return site_code.count('<a')

    def write_url(self, file):
        site_code = self.read_url()
        if site_code is None:
            print('Ошибка чтения кода страницы!')
            return None
        try:
            with open(file, mode='w') as f:
                f.write(site_code)
        except Exception as e:
            print('Ошибка записи url в файл!')




file = MyFile("text.txt", "read")
text = file.read() # происходит чтение в виде str
print(f'Содержимое файла: {text}')

file = MyFile("text.txt", "write")
text = file.write("привет!") # происходит запись строки в файл

file = MyFile("text.txt", "append")
text = file.write("привет!") # происходит добавление строки в конец файла

# указали URL
file = MyFile("https://apple.com", "url")
# и может читать содержимое страницы по указанному URL
text = file.read_url() # происходит чтение в виде str
print('Содержимое сайта:')
print(text)

# возвращает кол-во url адресов на странице, например, методом count
count = file.count_urls()
print(f'Количество url адресов на сайте: {count}')

# происходит запись содержимого страницы по URL в указанный файл
file.write_url("text.txt")
