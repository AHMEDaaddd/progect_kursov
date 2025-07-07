"""Модуль для получения вакансий с платформы hh.ru через API."""
import requests
from typing import List, Dict
from .parser import Parser


class HeadHunterAPI(Parser):
    """Класс для получения вакансий с платформы hh.ru."""

    BASE_URL = "https://api.hh.ru/vacancies"


    def __init__(self):
        """Инициализация клиента HeadHunterAPI с базовым URL и заголовками."""
        self.__headers = {"User-Agent": "Custom-HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 20}

    def __connect(self, params: Dict) -> requests.Response:
        response = requests.get(self.BASE_URL,
                                headers=self.__headers, params=params)
        if response.status_code != 200:
            raise (ConnectionError
                   (f"Ошибка подключения к API hh.ru: {response.status_code}"))
        return response


    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получает список вакансий по заданному поисковому запросу с hh.ru."""
        self.__params["text"] = keyword
        self.__params["page"] = 0
        all_vacancies = []

        while self.__params["page"] < 5:
            response = self.__connect(self.__params)
            data = response.json()
            all_vacancies.extend(data.get("items", []))
            if self.__params["page"] >= data.get("pages", 0) - 1:
                break
            self.__params["page"] += 1

        return all_vacancies
