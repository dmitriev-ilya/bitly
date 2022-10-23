# Обрезка ссылок с помощью Битли

Скрипт проверяет формат введённой ссылки, если она в виде Битли-ссылки, то выводит количество переходов по ней, если нет - преобразовает её в Битли формат вида `bit.ly/3gmb8Id`.

### Как установить


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Помимо этого, для работы понадобится создать файл `.env` в корневом каталоге проекта. Данный файл необходим для работы с переменными окружения и должен содержать в себе переменную `BITLY_TOKEN=<ACCESS TOKEN Bitly>`. Для получения `ACCESS TOKEN` необходимо зарегестрироваться на сайте [Bitly](https://bitly.com/) и следовать инструкции по [ссылке](https://dev.bitly.com/). Данные манипуляции необходимы для получения доступа к API Bitly, без них работа скрипта невозможна.

### Использование скрипта

Обрабатываемая ссылка должна вводится в виде аргумента командной строки.
При вводе полноразмерной ссылки, скрипт возвращет ссылку в формате Bitly:
```bash
$ python3 main.py https://yandex.ru
Битлинк bit.ly/3SwVWpq
```
При вводе ссылки в формате Bitly, скрипт возвращает статистику переходов по этой ссылке:
```bash
$ python3 main.py bit.ly/3SwVWpq
Количество переходов по ссылке битли: 3
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
