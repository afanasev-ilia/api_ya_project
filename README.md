# api_ya_project

api_ya_project

[![CI](https://github.com/LihieTapki/api_ya_project)

## Описание

API интерфейс для обмена данными c проектом ya_project

## Технологии

Python 3.7

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/LihieTapki/api_ya_project
```

```bash
cd api_ya_project
```

Cоздать и активировать виртуальное окружение:

```python
python -m venv venv
```

```bash
source venv/bin/activate
```

```python
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Cгенерировать .env файл:

```python
cp .env.example .env
``` 

Выполнить миграции:

```python
python manage.py migrate
```

Запустить проект:

```python
python manage.py runserver
```

Документация для API Yatube в формате Redoc:

```HTTP
http://127.0.0.1:8000/redoc/
```

## Автор

Илья Афанасьев
