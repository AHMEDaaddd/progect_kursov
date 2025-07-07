"""Абстрактный класс Parser для подключения к API платформ с вакансиями."""
from abc import ABC, abstractmethod
from typing import List, Dict


class Parser(ABC):
    """Абстрактный класс для API-сервисов вакансий."""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получить список вакансий по ключевому слову."""
        pass
