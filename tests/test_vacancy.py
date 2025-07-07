from src.models.vacancy import Vacancy


def test_vacancy_creation():
    vacancy = Vacancy("Dev", "url", 100_000, 150_000, "Python")
    assert vacancy.salary_from == 100_000
    assert vacancy.salary_to == 150_000
    assert vacancy.title == "Dev"


def test_salary_validation():
    vacancy = Vacancy("Test", "url", -100, None, "text")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_vacancy_comparison():
    v1 = Vacancy("A", "url1", 50_000, 100_000, "")
    v2 = Vacancy("B", "url2", 70_000, 100_000, "")
    assert v2 > v1
    assert not v1 > v2
