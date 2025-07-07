"""Точка входа в приложение. Реализует консольное взаимодействие с пользователем."""
from src.api.hh_api import HeadHunterAPI
from src.storage.json_saver import JSONSaver
from src.utils.helpers import (
    filter_by_keywords,
    get_top_n_vacancies,
    cast_list_to_vacancies,
    print_vacancies
)


def user_interaction() -> None:
    """Обрабатывает ввод пользователя: выполняет поиск, фильтрацию, сортировку и вывод вакансий."""
    print("\n🔎 Добро пожаловать в поиск вакансий с hh.ru!\n")
    keyword = input("Введите поисковый запрос: ").strip()
    top_n = int(input("Сколько топ вакансий показать? ").strip())
    words = (input("Ключевые слова для фильтрации (через пробел): ")
             .strip().split())

    hh = HeadHunterAPI()
    raw_vacancies = hh.get_vacancies(keyword)
    vacancies = cast_list_to_vacancies(raw_vacancies)

    filtered = filter_by_keywords(vacancies, words)
    top_vacancies = get_top_n_vacancies(filtered, top_n)

    print("\n📋 Найденные вакансии:\n")
    print_vacancies(top_vacancies)

    saver = JSONSaver()
    for vacancy in top_vacancies:
        saver.add_vacancy(vacancy)

    print(f"\n✅ {len(top_vacancies)} вакансий сохранено в файл!")


if __name__ == "__main__":
    user_interaction()
