# Проект: Вакансии с hh.ru

## Описание
Консольное приложение для поиска вакансий по API hh.ru, фильтрации и сохранения в файл.

## Как использовать

1. Установите зависимости:
   ```bash
   poetry install
   ```

2. Запустите программу:
   ```bash
   poetry run python src/main.py
   ```

3. Введите ключевое слово, топ-N и фильтр.

## Структура
- `src/api` — классы для работы с API hh.ru
- `src/models` — класс `Vacancy`
- `src/storage` — сохранение в JSON
- `src/utils` — фильтрация, сортировка
- `src/main.py` — точка входа

## Проверка качества кода

```bash
poetry run mypy src --explicit-package-bases
poetry run flake8 src
poetry run pydocstyle src
poetry run pytest
```
