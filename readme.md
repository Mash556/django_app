# Django APP menu 

Это проект где вы можете оставлять интересные вещи с ссылкой на эти каналы, сайты, страницы и т.д

### Важно ❗️❗️❗️

Чтобы запустить проект у вас должен быть установлен

#### [Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)   [VScode](https://code.visualstudio.com/download)  [Python](https://www.python.org/downloads/)

---

Клонируем репозиторий:
```
git clone {ssh ссылка репозитория} {название папки}
```
---
Переходим в папку
```
cd {название папки}
```
Проводим миграции 
```
python manage.py makemigrations
python manage.py migrate
```
---
Создаем пользователя в терминале
```
python manage.py createsuperuser
```
---
Теперь можем запустить сервер 
```
python manage.py runserver
```
---
Теперь надо зайти в админку django 
перейдите по этой ссылке [admin](http://127.0.0.1:8000/admin/)

Он попросит вас вести данные в поле **username** и **password**
Вы должны вести данные пользователья которого ранее создовали ***python manage.py createsuperuser***

---
После того как вы зашли в [admin](http://127.0.0.1:8000/admin/)

Создайте несколько Menu

В поле title можете передать название которое соответсвиям остальным полям 

Что бы создать пару Menu следуйте этим инструкциям 

```
в поле title передайте:      слепой печать тренажер
в поле url передайте:        https://www.ratatype.com/ru/
description:                 Давайте научимся слепому печатью 
и нажмите на save
```
давайте создади еще несколько Menu
```
в поле title передайте:      python lesson программирование тренажер
в поле url передайте:        https://letpy.com/
description:                 Python — это язык программирования 
и нажмите на save
```

```
в поле title передайте:      python django
в поле url передайте:        https://docs.djangoproject.com/en/5.0/#top
description:                 Django это популярный фреймворк написанный на python 
и нажмите на save
```
Вы также можете передать поле parent это будет его родителем (древовидное меню)
```
в поле title передайте:      python aiogram asing
в поле url передайте:        https://docs.aiogram.dev/en/latest/
description:                 Aiogram - это асинхронный python фреймворк для создания telegram-ботов
и нажмите на save
```

---

Теперь можете перейдите в страницу [Menu](http://127.0.0.1:8000/menu/)

Тут будет отображаться *Menu* которых добавили вы 

## Немного об этой страничке [Menu](http://127.0.0.1:8000/menu/)
При клике на имена меню происходит переход по заданному в нем URL

>Если вы добавили не существующий url то он будет работать для поиска такого элемента в **Menu**

Можете использовать поис поиск будет происходить по названию *Menu*  (поле title)

Рядом самим названием *Menu* будут отображаться его дочерние *Menu* если они есть 

---

```
Если вы не можете зайти в [admin](http://127.0.0.1:8000/admin/) 
Проверьте запущен ли у вас сервер 
```

```
Если не получаеися создать менью то проверьте прошли ли все миграции успешно
```