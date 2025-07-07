"""Вспомогательные функции: фильтрация, сортировка и печать вакансий."""
from typing import List
from src.models.vacancy import Vacancy



def filter_by_keywords(vacancies: List[Vacancy],
                       keywords: List[str]) -> List[Vacancy]:
    """Фильтрует список вакансий по ключевым словам в описании."""
    result = []
    for v in vacancies:
        description = v.description or ""
        if any(k.lower() in description.lower() for k in keywords):
            result.append(v)
    return result



def get_top_n_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Возвращает топ-N вакансий с наивысшей зарплатой."""
    return sorted(vacancies, reverse=True)[:n]


def cast_list_to_vacancies(raw_vacancies: List[dict]) -> List[Vacancy]:
    """Преобразует список словарей в список объектов Vacancy."""
    return [Vacancy.from_dict(item) for item in raw_vacancies]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Выводит список вакансий в удобочитаемом формате."""
    for v in vacancies:
        print(v)
        print("-" * 80)
