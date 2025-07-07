"""Модель вакансии с валидацией данных и возможностью сравнения по зарплате."""
from functools import total_ordering


@total_ordering
class Vacancy:
    """Класс, представляющий вакансию."""

    __slots__ = ("title", "url", "salary_from", "salary_to", "description")


    def __init__(self, title: str, url: str, salary_from: int
                | None, salary_to: int | None, description: str):
        """Создаёт экземпляр вакансии с проверкой и нормализацией данных."""
        self.title = title
        self.url = url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.description = description

    def _validate_salary(self, value: int | None) -> int:
        if isinstance(value, int) and value > 0:
            return value
        return 0


    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Vacancy для отладки."""
        return (f"{self.title} | {self.salary_from} - "
                f"{self.salary_to} RUB\n{self.url}")


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return (
                self.title == other.title and
                self.url == other.url and
                self.salary_from == other.salary_from and
                self.salary_to == other.salary_to and
                self.description == other.description
        )


    def __lt__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате (используется для сортировки)."""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from < other.salary_from


    @classmethod
    def from_dict(cls, data: dict) -> "Vacancy":
        """Создаёт экземпляр Vacancy из словаря, полученного из API."""
        title = data.get("name", "Нет названия")
        url = data.get("alternate_url", "")
        salary = data.get("salary") or {}
        salary_from = salary.get("from")
        salary_to = salary.get("to")
        description = (data.get("snippet", {}).
                       get("requirement", "Описание не указано"))
        return cls(title, url, salary_from, salary_to, description)


    def __hash__(self) -> int:
        """Возвращает хеш вакансии на основе её полей."""
        return hash((self.title, self.url, self.salary_from, self.salary_to, self.description))
