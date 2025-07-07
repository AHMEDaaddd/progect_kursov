from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver


def test_add_and_get_vacancy(tmp_path):
    filename = tmp_path / "test.json"
    saver = JSONSaver(str(filename))
    vacancy = Vacancy("Dev", "url", 100, 200, "text")

    saver.add_vacancy(vacancy)
    data = saver.get_vacancies()

    assert len(data) == 1
    assert data[0]["title"] == "Dev"

    saver.delete_vacancy(vacancy)
    assert saver.get_vacancies() == []
