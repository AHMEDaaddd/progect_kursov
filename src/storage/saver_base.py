"""Абстрактный базовый класс Saver для сохранения вакансий в хранилище."""
from abc import ABC, abstractmethod
from typing import Any


class Saver(ABC):
    """Абстрактный класс для работы с хранилищем вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Any) -> None:
        """Проверяет равенство вакансий по значениям зарплаты (от и до)."""
        pass


    @abstractmethod
    def get_vacancies(self) -> list:
        """Абстрактный метод: должен быть реализован в дочернем классе."""
        pass


    @abstractmethod
    def delete_vacancy(self, vacancy: Any) -> None:
        """Абстрактный метод: должен быть реализован в дочернем классе."""
        pass
