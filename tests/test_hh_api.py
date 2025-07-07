from unittest.mock import patch, MagicMock
from src.api.hh_api import HeadHunterAPI


@patch("src.api.hh_api.requests.get")
def test_get_vacancies(mock_get):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "items": [{"name": "Test Vacancy", "alternate_url": "url",
                   "salary": {}, "snippet": {}}],
        "pages": 1
    }

    mock_get.return_value = fake_response

    hh = HeadHunterAPI()
    result = hh.get_vacancies("python")

    assert isinstance(result, list)
    assert result[0]["name"] == "Test Vacancy"
