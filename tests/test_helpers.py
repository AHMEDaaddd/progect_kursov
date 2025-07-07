from src.models.vacancy import Vacancy
from src.utils.helpers import filter_by_keywords, get_top_n_vacancies


def test_filter_by_keywords():
    v1 = Vacancy("Dev", "url1", 100, 200, "Python")
    v2 = Vacancy("QA", "url2", 100, 200, "Manual testing")
    result = filter_by_keywords([v1, v2], ["python"])
    assert v1 in result
    assert v2 not in result


def test_get_top_n_vacancies():
    v1 = Vacancy("Junior", "url1", 50, 100, "")
    v2 = Vacancy("Middle", "url2", 100, 200, "")
    v3 = Vacancy("Senior", "url3", 200, 300, "")
    top = get_top_n_vacancies([v1, v2, v3], 2)
    assert len(top) == 2
    assert top[0].title == "Senior"
