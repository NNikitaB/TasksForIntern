
#  1.Какие шаги ты бы предпринял,если бы пользователь сказал,
#  что API возвращает ему ошибку 500?

# 500-Внутренняя ошибка сервера, которая не входит в рамки остальных ошибок класса.
# Ответ:
# Посмотреть логи сервера, по логам найти причину и устранить её.
# Возможные причины ещё:
# Скрипты работают слишком медленно
# Веб-сервер не может интерпретировать или распознать HTTP-заголовки


#  2.Какие ты видишт проблемы в следующем фрагменте кода?
#  Как его следует исправить?
#  Исправь ошибку и перепиши код ниже с использованием типизации.

# Ответ:
# Ошибка в lambda ('lambda :' вместо 'lambda x=step: callback(x)')
def create_handlers(callback) -> list:
    handlers: list = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda x=step: callback(x))
    return handlers


def execute_handlers(handlers) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


# 3.Сколько HTML-тегов в коде главной страницы сайта greenatom.ru?
# Сколько из них содержит атрибуты?
# Напиши скрипт на Python, который выводит ответы на вопросы выше.

# Ответ:
import urllib.request
from bs4 import BeautifulSoup as BS


def get_count_tags():
    site = 'https://greenatom.ru'
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-En,en;q=0.8',
        'Connection': 'keep-alive'}
    req = urllib.request.Request(site, headers=hdr)
    html = urllib.request.urlopen(req)
    soup = BS(html, "html.parser")
    dom = soup.findAll()
    count_tags = len(dom)
    count_attrs = sum([len(it.attrs) > 0 for it in dom])
    return "tags={0}".format(count_tags), "attrs={0}".format(count_attrs)

# 4.Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера
# (например, с использованием сервиса ifconfig.me).
# Ответ:


def get_my_ip() -> str:
    external_ip: str = urllib.request.urlopen('https://ifconfig.me').read().decode('utf8')
    return external_ip


# 5.Напиши функцию на Python, выполняющую сравнение версий. Условия:
# -Return -1 if version A is older than version В
# -Return 0 if versions A and В are equivalent
# -Return 1 if version A is newer than version В
# -Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.
# Ответ:
def compare_versions(v1: str, v2: str) -> int:
    for n1, n2 in zip(map(int, v1.split(".")), map(int, v2.split("."))):
        if n1 != n2:
            return 1 if n1 > n2 else -1
    return 0


if __name__ == '__main__':
    print("Task2")
    execute_handlers(create_handlers(lambda x: print(x)))
    print("Task3")
    print(get_count_tags())
    print("Task4")
    print(get_my_ip())
    print("Task5")
    print(compare_versions('1.10', ' 1.1'))
