"""Реализация сохранения вакансий в JSON-файл."""
import json
import os
from typing import Any
from .saver_base import Saver
from src.models.vacancy import Vacancy


class JSONSaver(Saver):
    """Хранилище вакансий в формате JSON."""

    def __init__(self, filename: str = "vacancies.json") -> None:
        """Инициализирует JSONSaver с именем файла (по умолчанию 'vacancies.json')."""
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)


    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет новую вакансию в файл, исключая дубликаты."""
        all_vacancies = self.get_vacancies()
        if vacancy.url not in [v["url"] for v in all_vacancies]:
            all_vacancies.append(self._vacancy_to_dict(vacancy))
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(all_vacancies, f, ensure_ascii=False, indent=2)


    def get_vacancies(self) -> list:
        """Возвращает список вакансий из JSON-файла."""
        with open(self.__filename, "r", encoding="utf-8") as f:
            return json.load(f)


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из файла, если она существует."""
        all_vacancies = self.get_vacancies()
        new_vacancies = [v for v in all_vacancies if v["url"] != vacancy.url]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(new_vacancies, f, ensure_ascii=False, indent=2)

    def _vacancy_to_dict(self, vacancy: Vacancy) -> dict:
        return {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "description": vacancy.description
        }
