import textwrap
from unittest.mock import MagicMock, patch

from config import config
from src.db_manager import DBManager

DB_MANAGER = DBManager()


def test_init():
    assert DB_MANAGER.database_name == "hh_ru"
    assert DB_MANAGER.params == config()


@patch("psycopg2.connect")
def test_get_companies_and_vacancies_count(mock_connect):
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cur
    mock_connect.return_value = mock_conn
    mock_cur.fetchall.return_value = [
        ("It’s Simple", 6),
        ("IT SCOUT(match)", 36),
        ("1С БИЗНЕС РЕШЕНИЯ", 7),
        ("IT-hunters", 40),
        ("1С-Архитектор бизнеса", 13),
        ("MyRest", 48),
        ("IT школа Hello World", 25),
        ("It's wear (ИП Хан Алексей Афанасьевич)", 10),
        ("Loft It", 2),
        ("Prof-IT", 5),
        ("It's beauty", 6),
        ("Napoleon IT", 9),
        ("DESPORT", 13),
    ]
    expected_result = [{'company': 'It’s Simple', 'vacancies_amount': 6},
                       {'company': 'IT SCOUT(match)', 'vacancies_amount': 36},
                       {'company': '1С БИЗНЕС РЕШЕНИЯ', 'vacancies_amount': 7},
                       {'company': 'IT-hunters', 'vacancies_amount': 40},
                       {'company': '1С-Архитектор бизнеса', 'vacancies_amount': 13},
                       {'company': 'MyRest', 'vacancies_amount': 48},
                       {'company': 'IT школа Hello World', 'vacancies_amount': 25},
                       {'company': "It's wear (ИП Хан Алексей Афанасьевич)", 'vacancies_amount': 10},
                       {'company': 'Loft It', 'vacancies_amount': 2}, {'company': 'Prof-IT', 'vacancies_amount': 5},
                       {'company': "It's beauty", 'vacancies_amount': 6},
                       {'company': 'Napoleon IT', 'vacancies_amount': 9},
                       {'company': 'DESPORT', 'vacancies_amount': 13}]

    actual_result = DB_MANAGER.get_companies_and_vacancies_count()
    expected_sql = textwrap.dedent(
        """
    SELECT employers.name, COUNT(vacancy_id) AS vacancies_count
    FROM employers
    JOIN vacancies USING(employer_id)
    GROUP BY employer_id, employers.name
    """
    )
    mock_cur.execute.assert_called_once_with(expected_sql)
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()
    assert actual_result == expected_result


@patch("psycopg2.connect")
def test_get_all_vacancies(mock_connect):
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cur
    mock_connect.return_value = mock_conn
    expected_db_response = [
        (
            "IT-hunters",
            "Аналитик данных (Analyst)",
            120000,
            "https://api.hh.ru/vacancies/128538238?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Верстальщик Playable",
            None,
            "https://api.hh.ru/vacancies/129001890?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Мультидисциплинарный дизайнер",
            None,
            "https://api.hh.ru/vacancies/128941141?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Project Manager",
            None,
            "https://api.hh.ru/vacancies/129042214?host=hh.ru",
        ),
        (
            "IT-hunters",
            "ML Engineer",
            None,
            "https://api.hh.ru/vacancies/128955889?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Помощник по дому в семью ВИП",
            None,
            "https://api.hh.ru/vacancies/128283887?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Operations Project Manager",
            None,
            "https://api.hh.ru/vacancies/128578950?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Content Manager/ Editor",
            None,
            "https://api.hh.ru/vacancies/128480227?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Личный финансист/ казначей Family Office",
            None,
            "https://api.hh.ru/vacancies/128560598?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media buyer FB/in-app",
            None,
            "https://api.hh.ru/vacancies/128999254?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Motion Designer",
            None,
            "https://api.hh.ru/vacancies/128627004?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Юрист по работе с маркировкой рекламы",
            None,
            "https://api.hh.ru/vacancies/128988032?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764110?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Личный финансист для CEO",
            None,
            "https://api.hh.ru/vacancies/128369395?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Гардеробщица/гардеробщик в VIP семью",
            None,
            "https://api.hh.ru/vacancies/128258680?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Аккаунт менеджер/Account Manager (Global)",
            None,
            "https://api.hh.ru/vacancies/128538157?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Специалист по работе с маркировкой рекламы",
            None,
            "https://api.hh.ru/vacancies/129020546?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Lead Country Manager",
            None,
            "https://api.hh.ru/vacancies/127882178?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Senior Playable Ads Developer",
            None,
            "https://api.hh.ru/vacancies/129009016?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media Buyer",
            None,
            "https://api.hh.ru/vacancies/123029473?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Team Lead Buyer Push",
            None,
            "https://api.hh.ru/vacancies/129038015?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media Buyer Senior Push",
            None,
            "https://api.hh.ru/vacancies/129041986?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media Buyer Middle Push",
            None,
            "https://api.hh.ru/vacancies/129039952?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media Buyer Team Lead",
            None,
            "https://api.hh.ru/vacancies/127788435?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Аккаунт Менеджер",
            None,
            "https://api.hh.ru/vacancies/127656464?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media buyer (Fb + in-app)",
            None,
            "https://api.hh.ru/vacancies/119508256?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Team Lead Media Buyer",
            None,
            "https://api.hh.ru/vacancies/126878022?host=hh.ru",
        ),
        (
            "IT-hunters",
            "ML Engineer",
            None,
            "https://api.hh.ru/vacancies/128955888?host=hh.ru",
        ),
        (
            "IT-hunters",
            "ML Engineer",
            None,
            "https://api.hh.ru/vacancies/128955890?host=hh.ru",
        ),
        (
            "IT-hunters",
            "ML Engineer",
            None,
            "https://api.hh.ru/vacancies/128955815?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764116?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764114?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764111?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764113?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Lead Country Manager",
            None,
            "https://api.hh.ru/vacancies/127882117?host=hh.ru",
        ),
        (
            "IT-hunters",
            "ML Engineer",
            None,
            "https://api.hh.ru/vacancies/126874963?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764112?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Media Buyer Senior Push",
            None,
            "https://api.hh.ru/vacancies/129041987?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Motion Designer",
            None,
            "https://api.hh.ru/vacancies/128627005?host=hh.ru",
        ),
        (
            "IT-hunters",
            "Моушн-дизайнер (Intern)",
            None,
            "https://api.hh.ru/vacancies/128764115?host=hh.ru",
        ),
        (
            "It's beauty",
            "Администратор салона красоты",
            52500,
            "https://api.hh.ru/vacancies/128877526?host=hh.ru",
        ),
        (
            "It's beauty",
            "Стажер мастером маникюра",
            80000,
            "https://api.hh.ru/vacancies/128959277?host=hh.ru",
        ),
        (
            "It's beauty",
            "Brow-мастер / ламимейкер",
            100500,
            "https://api.hh.ru/vacancies/128762684?host=hh.ru",
        ),
        (
            "It's beauty",
            "Brow-мастер / бровист",
            100500,
            "https://api.hh.ru/vacancies/128163610?host=hh.ru",
        ),
        (
            "It's beauty",
            "Мастер маникюра",
            190000,
            "https://api.hh.ru/vacancies/128959015?host=hh.ru",
        ),
        (
            "It's beauty",
            "Парикмахер-стилист / парикмахер-колорист",
            160000,
            "https://api.hh.ru/vacancies/128496157?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Affiliate manager (менеджер по привлечению партнеров)",
            None,
            "https://api.hh.ru/vacancies/127313403?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Affiliate Manager (менеджер по привлечению партнеров)",
            None,
            "https://api.hh.ru/vacancies/128522884?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Модератор",
            None,
            "https://api.hh.ru/vacancies/128960252?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Руководитель отдела контроля качества",
            None,
            "https://api.hh.ru/vacancies/128760886?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Аккаунт-менеджер",
            120000,
            "https://api.hh.ru/vacancies/128865462?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Бизнес аналитик (Junior)",
            None,
            "https://api.hh.ru/vacancies/128093583?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Помощник системного администратора",
            None,
            "https://api.hh.ru/vacancies/128824134?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Anti-fraud analyst",
            None,
            "https://api.hh.ru/vacancies/128985657?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Localization manager",
            None,
            "https://api.hh.ru/vacancies/128634492?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Marketing Researcher",
            None,
            "https://api.hh.ru/vacancies/128791775?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Помощник системного администратора",
            None,
            "https://api.hh.ru/vacancies/128715977?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Специалист технической поддержки (2-я линия)",
            65000,
            "https://api.hh.ru/vacancies/128920690?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Concierge Manager",
            None,
            "https://api.hh.ru/vacancies/129003918?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "DataOps / DevOps Engineer",
            None,
            "https://api.hh.ru/vacancies/128840605?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Operations Payment Manager",
            None,
            "https://api.hh.ru/vacancies/128920751?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Influence manager / Специалист по работе с блогерами",
            None,
            "https://api.hh.ru/vacancies/128148333?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Менеджер по развитию партнерской сети",
            None,
            "https://api.hh.ru/vacancies/128833759?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Специалист технической поддержки (2-я линия)",
            None,
            "https://api.hh.ru/vacancies/128267340?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Payment Manager / Администратор платежей для VIP пользователей",
            None,
            "https://api.hh.ru/vacancies/128263302?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Бизнес-тренер",
            None,
            "https://api.hh.ru/vacancies/128828813?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Менеджер по контролю качества",
            None,
            "https://api.hh.ru/vacancies/127303959?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Node.js developer (GTA)",
            None,
            "https://api.hh.ru/vacancies/128557224?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Менеджер по работе с партнёрами (Digital)",
            None,
            "https://api.hh.ru/vacancies/128283317?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Бизнес-тренер со знанием испанского языка",
            None,
            "https://api.hh.ru/vacancies/128828763?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Smm manager",
            None,
            "https://api.hh.ru/vacancies/128909458?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Рекрутер",
            None,
            "https://api.hh.ru/vacancies/128394856?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Специалист по поиску медийных личностей / Скаут (со знанием корейского языка)",
            None,
            "https://api.hh.ru/vacancies/128534626?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Senior Java / Kotlin Developer",
            None,
            "https://api.hh.ru/vacancies/128614382?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Affiliate-менеджер со знанием иностранного языка",
            None,
            "https://api.hh.ru/vacancies/128539716?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Media Buyer FB",
            None,
            "https://api.hh.ru/vacancies/128762581?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Influence Manager/Менеджер по работе с блогерами",
            None,
            "https://api.hh.ru/vacancies/128094828?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Senior AQA Engineer / Тестировщик-автоматизатор",
            None,
            "https://api.hh.ru/vacancies/128715264?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "SEO Drop Hunter",
            None,
            "https://api.hh.ru/vacancies/128094543?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "КДП-менеджер",
            None,
            "https://api.hh.ru/vacancies/128336341?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "CR Manager",
            None,
            "https://api.hh.ru/vacancies/128760044?host=hh.ru",
        ),
        (
            "IT SCOUT(match)",
            "Concierge Manager (Spanish)",
            None,
            "https://api.hh.ru/vacancies/128764574?host=hh.ru",
        ),
        (
            "It’s Simple",
            "Мастер смены",
            85000,
            "https://api.hh.ru/vacancies/128661728?host=hh.ru",
        ),
        (
            "It’s Simple",
            "Шеф-монтажник",
            150000,
            "https://api.hh.ru/vacancies/128636185?host=hh.ru",
        ),
        (
            "It’s Simple",
            "Электросварщик на полуавтомат",
            70000,
            "https://api.hh.ru/vacancies/128633349?host=hh.ru",
        ),
        (
            "It’s Simple",
            "Менеджер по закупкам и логистике",
            None,
            "https://api.hh.ru/vacancies/128760628?host=hh.ru",
        ),
        (
            "It’s Simple",
            "Слесарь-сборщик",
            65000,
            "https://api.hh.ru/vacancies/128633667?host=hh.ru",
        ),
        (
            "It’s Simple",
            "Менеджер по закупкам и ВЭД",
            None,
            "https://api.hh.ru/vacancies/128671829?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR (ТЦ Броско Молл)",
            65000,
            "https://api.hh.ru/vacancies/128459803?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR (ТЦ Магазины Радости)",
            65000,
            "https://api.hh.ru/vacancies/128933432?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Старший продавец магазина одежды ITSWEAR",
            72500,
            "https://api.hh.ru/vacancies/128933414?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR",
            65000,
            "https://api.hh.ru/vacancies/128933527?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Помощник руководителя/ассистент",
            70000,
            "https://api.hh.ru/vacancies/125870259?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR (ТЦ Кловер Хаус)",
            65000,
            "https://api.hh.ru/vacancies/125511462?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант (ТРК Сити Молл)",
            65000,
            "https://api.hh.ru/vacancies/128848740?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR (ТЦ Бум)",
            51000,
            "https://api.hh.ru/vacancies/128405866?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR (ТЦ Дом Быта)",
            65000,
            "https://api.hh.ru/vacancies/128933496?host=hh.ru",
        ),
        (
            "It's wear (ИП Хан Алексей Афанасьевич)",
            "Продавец-консультант ITSWEAR (ТЦ Острова)",
            60000,
            "https://api.hh.ru/vacancies/128933475?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Программист Python Middle (backend)",
            225000,
            "https://api.hh.ru/vacancies/128955079?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Backend-разработчик Python (Middle)",
            225000,
            "https://api.hh.ru/vacancies/128836864?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Методист для детской онлайн школы по дизайну",
            80000,
            "https://api.hh.ru/vacancies/128318185?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор начальных классов",
            45000,
            "https://api.hh.ru/vacancies/127950667?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Методист в онлайн-школу (Edtech)",
            None,
            "https://api.hh.ru/vacancies/122917696?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по математике",
            35000,
            "https://api.hh.ru/vacancies/124334357?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по русскому языку (5-11 класс)",
            48000,
            "https://api.hh.ru/vacancies/128127168?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель Python в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/128277607?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель Скорочтения",
            47000,
            "https://api.hh.ru/vacancies/127130049?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по информатике 9-11 класс",
            35000,
            "https://api.hh.ru/vacancies/126586445?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель Python и Roblox в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/127780979?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по информатике 9-11 класс (онлайн)",
            35000,
            "https://api.hh.ru/vacancies/124383462?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по информатике 9-11 класс",
            45500,
            "https://api.hh.ru/vacancies/126122168?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель ментальной арифметики в онлайн-школу",
            47000,
            "https://api.hh.ru/vacancies/128835663?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по физике",
            500,
            "https://api.hh.ru/vacancies/128128801?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор начальных классов",
            45000,
            "https://api.hh.ru/vacancies/128659290?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель начальных классов",
            45000,
            "https://api.hh.ru/vacancies/127399523?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Python backend developer (Middle)",
            225000,
            "https://api.hh.ru/vacancies/127608139?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Методист в онлайн-школу (Edtech)",
            None,
            "https://api.hh.ru/vacancies/122918683?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель Python и Roblox в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/128538405?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель Скорочтения",
            47000,
            "https://api.hh.ru/vacancies/127130048?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по русскому языку (5-11 класс)",
            48000,
            "https://api.hh.ru/vacancies/128127276?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Репетитор по русскому языку (5-11 класс)",
            48000,
            "https://api.hh.ru/vacancies/128127227?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель Python, Scratch в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/128277608?host=hh.ru",
        ),
        (
            "IT школа Hello World",
            "Преподаватель ментальной арифметики в онлайн-школу",
            47000,
            "https://api.hh.ru/vacancies/128432096?host=hh.ru",
        ),
        (
            "Loft It",
            "Менеджер по работе с клиентами",
            125000,
            "https://api.hh.ru/vacancies/127215301?host=hh.ru",
        ),
        (
            "Loft It",
            "Менеджер по оптовым продажам светотехники",
            200000,
            "https://api.hh.ru/vacancies/128244799?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            81000,
            "https://api.hh.ru/vacancies/128314867?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314191?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            56500,
            "https://api.hh.ru/vacancies/128313946?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314192?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            70500,
            "https://api.hh.ru/vacancies/128314551?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            76500,
            "https://api.hh.ru/vacancies/128314811?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314184?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            70500,
            "https://api.hh.ru/vacancies/128314549?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314195?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314187?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            62000,
            "https://api.hh.ru/vacancies/128314316?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            65000,
            "https://api.hh.ru/vacancies/128906269?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            72000,
            "https://api.hh.ru/vacancies/128906367?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314188?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            65500,
            "https://api.hh.ru/vacancies/128314371?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314190?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            72500,
            "https://api.hh.ru/vacancies/128314698?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            62000,
            "https://api.hh.ru/vacancies/128906202?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            70500,
            "https://api.hh.ru/vacancies/128314550?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            72500,
            "https://api.hh.ru/vacancies/128314699?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314189?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            73000,
            "https://api.hh.ru/vacancies/128906711?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            62000,
            "https://api.hh.ru/vacancies/128314318?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            62000,
            "https://api.hh.ru/vacancies/128314317?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            70500,
            "https://api.hh.ru/vacancies/128314553?host=hh.ru",
        ),
        (
            "MyRest",
            "Заместитель директора ресторана Rostic's (Ростикс)",
            67000,
            "https://api.hh.ru/vacancies/126303945?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            56500,
            "https://api.hh.ru/vacancies/128313947?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            58000,
            "https://api.hh.ru/vacancies/126304205?host=hh.ru",
        ),
        (
            "MyRest",
            "Заместитель директора ресторана Rostic's (Ростикс)",
            83000,
            "https://api.hh.ru/vacancies/126304041?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            84000,
            "https://api.hh.ru/vacancies/128906481?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            55000,
            "https://api.hh.ru/vacancies/126304284?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            81000,
            "https://api.hh.ru/vacancies/128314866?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314197?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314186?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            70500,
            "https://api.hh.ru/vacancies/128314552?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            76500,
            "https://api.hh.ru/vacancies/128314810?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314194?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314193?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314182?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            56500,
            "https://api.hh.ru/vacancies/128313948?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314183?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            65000,
            "https://api.hh.ru/vacancies/128906270?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            58500,
            "https://api.hh.ru/vacancies/128314196?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            62000,
            "https://api.hh.ru/vacancies/128314319?host=hh.ru",
        ),
        (
            "MyRest",
            "Менеджер ресторана Rostic's (Ростикс)",
            73000,
            "https://api.hh.ru/vacancies/128906712?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            76500,
            "https://api.hh.ru/vacancies/128314809?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            56500,
            "https://api.hh.ru/vacancies/128313949?host=hh.ru",
        ),
        (
            "MyRest",
            "Сотрудник ресторана Rostic's (Ростикс)",
            70500,
            "https://api.hh.ru/vacancies/128314548?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Стажер Project Manager",
            None,
            "https://api.hh.ru/vacancies/128540367?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Python developer (Middle)",
            None,
            "https://api.hh.ru/vacancies/127492651?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Интервьюер - Аналитик",
            None,
            "https://api.hh.ru/vacancies/128984035?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Стажер в отдел рекрутинга",
            None,
            "https://api.hh.ru/vacancies/129003468?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Интервьюер .NET",
            None,
            "https://api.hh.ru/vacancies/128974348?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Руководитель направления ИИ | Head of AI",
            None,
            "https://api.hh.ru/vacancies/128532918?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Analyst Middle+",
            None,
            "https://api.hh.ru/vacancies/127175464?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "Стажёр Reels-мейкер / Видео-контентмейкер с ИИ-инструментами",
            None,
            "https://api.hh.ru/vacancies/128094745?host=hh.ru",
        ),
        (
            "Napoleon IT",
            "PHP-разработчик (Bitrix 24) Middle",
            None,
            "https://api.hh.ru/vacancies/127915386?host=hh.ru",
        ),
        (
            "Prof-IT",
            "Менеджер по продажам IT услуг",
            60000,
            "https://api.hh.ru/vacancies/119806970?host=hh.ru",
        ),
        (
            "Prof-IT",
            "Операционный менеджер",
            40000,
            "https://api.hh.ru/vacancies/128822540?host=hh.ru",
        ),
        (
            "Prof-IT",
            "Менеджер по работе с клиентами (b2b)",
            60000,
            "https://api.hh.ru/vacancies/120822587?host=hh.ru",
        ),
        (
            "Prof-IT",
            "Менеджер в отдел продаж",
            125000,
            "https://api.hh.ru/vacancies/128235757?host=hh.ru",
        ),
        (
            "Prof-IT",
            "Стажер в отдел продаж",
            50000,
            "https://api.hh.ru/vacancies/128154156?host=hh.ru",
        ),
        (
            "DESPORT",
            "Старший смены",
            115000,
            "https://api.hh.ru/vacancies/128829695?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант (ТРЦ Авиапарк)",
            75000,
            "https://api.hh.ru/vacancies/128417673?host=hh.ru",
        ),
        (
            "DESPORT",
            "Оператор складской техники",
            100000,
            "https://api.hh.ru/vacancies/128829735?host=hh.ru",
        ),
        (
            "DESPORT",
            "Охранник-контролёр (склад Домодедово)",
            80000,
            "https://api.hh.ru/vacancies/128917044?host=hh.ru",
        ),
        (
            "DESPORT",
            "Кладовщик",
            85000,
            "https://api.hh.ru/vacancies/128828512?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант",
            52174,
            "https://api.hh.ru/vacancies/128414180?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант DESPORT (г. Мытищи)",
            70000,
            "https://api.hh.ru/vacancies/128862137?host=hh.ru",
        ),
        (
            "DESPORT",
            "Специалист по контекстной рекламе (контекстолог)",
            172500,
            "https://api.hh.ru/vacancies/128414387?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант (ТЦ Парк Молл)",
            72500,
            "https://api.hh.ru/vacancies/128412981?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант (г. Одинцово)",
            75000,
            "https://api.hh.ru/vacancies/128414244?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант, Ульяновск",
            55000,
            "https://api.hh.ru/vacancies/127627695?host=hh.ru",
        ),
        (
            "DESPORT",
            "Продавец-консультант (г. Пермь)",
            55000,
            "https://api.hh.ru/vacancies/128413982?host=hh.ru",
        ),
        (
            "DESPORT",
            "Руководитель торгового сектора, Одинцово",
            90000,
            "https://api.hh.ru/vacancies/128414347?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Бухгалтер (Акты сверок)",
            82000,
            "https://api.hh.ru/vacancies/128823250?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Аналитик 1С (Документооборот)",
            100000,
            "https://api.hh.ru/vacancies/128857458?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127867189?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Менеджер по продажам 1С",
            None,
            "https://api.hh.ru/vacancies/128389478?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127314248?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127314249?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127867188?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Менеджер по продажам 1С",
            None,
            "https://api.hh.ru/vacancies/128389477?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Менеджер по продажам, направление 1С",
            None,
            "https://api.hh.ru/vacancies/128700129?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Менеджер по продажам 1С",
            None,
            "https://api.hh.ru/vacancies/128389479?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127867187?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127314247?host=hh.ru",
        ),
        (
            "1С-Архитектор бизнеса",
            "Менеджер по продажам, направление 1С",
            None,
            "https://api.hh.ru/vacancies/128696932?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Специалист по сопровождению 1С",
            40000,
            "https://api.hh.ru/vacancies/128600624?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Программист 1С (Middle, Senior)",
            185000,
            "https://api.hh.ru/vacancies/128511268?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Менеджер по продажам 1С",
            65000,
            "https://api.hh.ru/vacancies/127399504?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Бухгалтер консультант 1С",
            100000,
            "https://api.hh.ru/vacancies/127710733?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Помощник менеджера по продажам",
            32500,
            "https://api.hh.ru/vacancies/128787404?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Менеджер по работе с клиентами",
            50000,
            "https://api.hh.ru/vacancies/127594686?host=hh.ru",
        ),
        (
            "1С БИЗНЕС РЕШЕНИЯ",
            "Менеджер по продажам и работе с тендерами",
            65250,
            "https://api.hh.ru/vacancies/128511224?host=hh.ru",
        ),
    ]

    mock_cur.fetchall.return_value = expected_db_response
    actual_response = DB_MANAGER.get_all_vacancies()
    expected_sql = textwrap.dedent(
        """SELECT employers.name, vacancies.name, salary, url
                            FROM vacancies
                            JOIN employers USING(employer_id)"""
    )
    mock_cur.execute.assert_called_once_with(expected_sql)
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()
    assert expected_db_response == actual_response


@patch("psycopg2.connect")
def test_get_avg_salary(mock_connect):
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cur
    mock_connect.return_value = mock_conn
    expected_db_response = 78065.302325581395
    mock_cur.fetchone.return_value = (expected_db_response,)
    actual_response = DB_MANAGER.get_avg_salary()
    expected_sql = """SELECT AVG(salary) AS avg_salary
                            FROM vacancies"""

    assert actual_response == expected_db_response
    mock_cur.execute.assert_called_once_with(textwrap.dedent(expected_sql))
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("psycopg2.connect")
def test_get_vacancies_with_higher_salary(mock_connect):
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cur
    mock_connect.return_value = mock_conn
    expected_db_response = [
        (
            128538238,
            5591530,
            "Аналитик данных (Analyst)",
            120000,
            "https://api.hh.ru/vacancies/128538238?host=hh.ru",
        ),
        (
            128959277,
            3147167,
            "Стажер мастером маникюра",
            80000,
            "https://api.hh.ru/vacancies/128959277?host=hh.ru",
        ),
        (
            128762684,
            3147167,
            "Brow-мастер / ламимейкер",
            100500,
            "https://api.hh.ru/vacancies/128762684?host=hh.ru",
        ),
        (
            128163610,
            3147167,
            "Brow-мастер / бровист",
            100500,
            "https://api.hh.ru/vacancies/128163610?host=hh.ru",
        ),
        (
            128959015,
            3147167,
            "Мастер маникюра",
            190000,
            "https://api.hh.ru/vacancies/128959015?host=hh.ru",
        ),
        (
            128496157,
            3147167,
            "Парикмахер-стилист / парикмахер-колорист",
            160000,
            "https://api.hh.ru/vacancies/128496157?host=hh.ru",
        ),
        (
            128865462,
            11181389,
            "Аккаунт-менеджер",
            120000,
            "https://api.hh.ru/vacancies/128865462?host=hh.ru",
        ),
        (
            128661728,
            3655078,
            "Мастер смены",
            85000,
            "https://api.hh.ru/vacancies/128661728?host=hh.ru",
        ),
        (
            128636185,
            3655078,
            "Шеф-монтажник",
            150000,
            "https://api.hh.ru/vacancies/128636185?host=hh.ru",
        ),
        (
            128955079,
            3407499,
            "Программист Python Middle (backend)",
            225000,
            "https://api.hh.ru/vacancies/128955079?host=hh.ru",
        ),
        (
            128836864,
            3407499,
            "Backend-разработчик Python (Middle)",
            225000,
            "https://api.hh.ru/vacancies/128836864?host=hh.ru",
        ),
        (
            128318185,
            3407499,
            "Методист для детской онлайн школы по дизайну",
            80000,
            "https://api.hh.ru/vacancies/128318185?host=hh.ru",
        ),
        (
            127608139,
            3407499,
            "Python backend developer (Middle)",
            225000,
            "https://api.hh.ru/vacancies/127608139?host=hh.ru",
        ),
        (
            127215301,
            5046934,
            "Менеджер по работе с клиентами",
            125000,
            "https://api.hh.ru/vacancies/127215301?host=hh.ru",
        ),
        (
            128244799,
            5046934,
            "Менеджер по оптовым продажам светотехники",
            200000,
            "https://api.hh.ru/vacancies/128244799?host=hh.ru",
        ),
        (
            128314867,
            217918,
            "Сотрудник ресторана Rostic's (Ростикс)",
            81000,
            "https://api.hh.ru/vacancies/128314867?host=hh.ru",
        ),
        (
            126304041,
            217918,
            "Заместитель директора ресторана Rostic's (Ростикс)",
            83000,
            "https://api.hh.ru/vacancies/126304041?host=hh.ru",
        ),
        (
            128906481,
            217918,
            "Менеджер ресторана Rostic's (Ростикс)",
            84000,
            "https://api.hh.ru/vacancies/128906481?host=hh.ru",
        ),
        (
            128314866,
            217918,
            "Сотрудник ресторана Rostic's (Ростикс)",
            81000,
            "https://api.hh.ru/vacancies/128314866?host=hh.ru",
        ),
        (
            128235757,
            2910384,
            "Менеджер в отдел продаж",
            125000,
            "https://api.hh.ru/vacancies/128235757?host=hh.ru",
        ),
        (
            128829695,
            18071,
            "Старший смены",
            115000,
            "https://api.hh.ru/vacancies/128829695?host=hh.ru",
        ),
        (
            128829735,
            18071,
            "Оператор складской техники",
            100000,
            "https://api.hh.ru/vacancies/128829735?host=hh.ru",
        ),
        (
            128917044,
            18071,
            "Охранник-контролёр (склад Домодедово)",
            80000,
            "https://api.hh.ru/vacancies/128917044?host=hh.ru",
        ),
        (
            128828512,
            18071,
            "Кладовщик",
            85000,
            "https://api.hh.ru/vacancies/128828512?host=hh.ru",
        ),
        (
            128414387,
            18071,
            "Специалист по контекстной рекламе (контекстолог)",
            172500,
            "https://api.hh.ru/vacancies/128414387?host=hh.ru",
        ),
        (
            128414347,
            18071,
            "Руководитель торгового сектора, Одинцово",
            90000,
            "https://api.hh.ru/vacancies/128414347?host=hh.ru",
        ),
        (
            128823250,
            2235,
            "Бухгалтер (Акты сверок)",
            82000,
            "https://api.hh.ru/vacancies/128823250?host=hh.ru",
        ),
        (
            128857458,
            2235,
            "Аналитик 1С (Документооборот)",
            100000,
            "https://api.hh.ru/vacancies/128857458?host=hh.ru",
        ),
        (
            127867189,
            2235,
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127867189?host=hh.ru",
        ),
        (
            127314248,
            2235,
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127314248?host=hh.ru",
        ),
        (
            127314249,
            2235,
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127314249?host=hh.ru",
        ),
        (
            127867188,
            2235,
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127867188?host=hh.ru",
        ),
        (
            127867187,
            2235,
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127867187?host=hh.ru",
        ),
        (
            127314247,
            2235,
            "Программист 1С УТ11",
            147500,
            "https://api.hh.ru/vacancies/127314247?host=hh.ru",
        ),
        (
            128511268,
            1852940,
            "Программист 1С (Middle, Senior)",
            185000,
            "https://api.hh.ru/vacancies/128511268?host=hh.ru",
        ),
        (
            127710733,
            1852940,
            "Бухгалтер консультант 1С",
            100000,
            "https://api.hh.ru/vacancies/127710733?host=hh.ru",
        ),
    ]
    mock_cur.fetchall.return_value = expected_db_response
    actual_response = DB_MANAGER.get_vacancies_with_higher_salary()
    expected_sql = textwrap.dedent(
        (
            """SELECT *
                            FROM vacancies
                            WHERE salary > (SELECT AVG(salary) FROM vacancies)"""
        )
    )

    mock_cur.execute.assert_called_once_with(expected_sql)
    assert actual_response == expected_db_response
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("psycopg2.connect")
def test_get_vacancies_with_keyword(mock_connect):
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cur
    mock_connect.return_value = mock_conn
    expected_response = [
        (
            128955079,
            3407499,
            "Программист Python Middle (backend)",
            225000,
            "https://api.hh.ru/vacancies/128955079?host=hh.ru",
        ),
        (
            128836864,
            3407499,
            "Backend-разработчик Python (Middle)",
            225000,
            "https://api.hh.ru/vacancies/128836864?host=hh.ru",
        ),
        (
            128277607,
            3407499,
            "Преподаватель Python в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/128277607?host=hh.ru",
        ),
        (
            127780979,
            3407499,
            "Преподаватель Python и Roblox в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/127780979?host=hh.ru",
        ),
        (
            127608139,
            3407499,
            "Python backend developer (Middle)",
            225000,
            "https://api.hh.ru/vacancies/127608139?host=hh.ru",
        ),
        (
            128538405,
            3407499,
            "Преподаватель Python и Roblox в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/128538405?host=hh.ru",
        ),
        (
            128277608,
            3407499,
            "Преподаватель Python, Scratch в онлайн-школу программирования",
            50000,
            "https://api.hh.ru/vacancies/128277608?host=hh.ru",
        ),
        (
            127492651,
            1062788,
            "Python developer (Middle)",
            None,
            "https://api.hh.ru/vacancies/127492651?host=hh.ru",
        ),
    ]
    mock_cur.fetchall.return_value = expected_response
    keyword = "python"
    actual_response = DB_MANAGER.get_vacancies_with_keyword(keyword)
    expected_sql = textwrap.dedent(
        f"""SELECT *
                            FROM vacancies
                            WHERE vacancies.name LIKE '%{keyword[1:]}%'"""
    )
    mock_cur.execute.assert_called_once_with(expected_sql)
    assert actual_response == expected_response
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()
