thinkers = {
    1: {'name': 'Платон',
        'years': '428 BC - 348 BC',
        'works': {'Государство', 'Диалоги', 'Апология Сократа'},
        'hometown': 'Athens',
        'photo': 'https://en.wikipedia.org/wiki/File:Plato_Silanion_Musei_Capitolini_MC1377.jpg',
        'more_info': 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%B0%D1%82%D0%BE%D0%BD#%D0%A2%D0%B5%D0%BA%D1%81%D1%82%D1%8B'},
    2: {'name': 'Сёрен Кьеркегор',
        'years': '1813 - 1855',
        'works': {'Или-или', 'Стадии жизненного пути', 'Страх и трепет'},
        'hometown': 'Copenhagen',
        'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/S%C3%B8ren_Kierkegaard_%281813-1855%29_-_%28cropped%29.jpg/411px-S%C3%B8ren_Kierkegaard_%281813-1855%29_-_%28cropped%29.jpg',
        'more_info': 'https://ru.wikipedia.org/wiki/%D0%9A%D1%8C%D0%B5%D1%80%D0%BA%D0%B5%D0%B3%D0%BE%D1%80,_%D0%A1%D1%91%D1%80%D0%B5%D0%BD'},
    3: {'name': 'Иммануил Кант',
        'years': '1724 - 1804',
        'works': {'Критика чистого разума', 'Сочинения в шести томах'},
        'hometown': 'Konigsberg',
        'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Kant_gemaelde_3.jpg/411px-Kant_gemaelde_3.jpg',
        'more_info': 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D1%82,_%D0%98%D0%BC%D0%BC%D0%B0%D0%BD%D1%83%D0%B8%D0%BB'}
}


def text_about_thinker(num: int):
    """
    Функция формирует информацию о выбранном философе.
    """
    name = thinkers[num]['name']
    years = f'Годы жизни: {thinkers[num]["years"]}'
    works = ', '.join(thinkers[num]['works'])
    works = f'Наиболее значимые труды: {works}'
    result_text = f"""
    {name}.
{years}.
{works}.
    """
    return result_text


def thinker_location(num: int):
    """
    Функция возвращает ширину и долготу города рождения
    выбранного философа.
    """
    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(thinkers[num]['hometown'])

    return {
        'latitude': location.latitude,
        'longitude': location.longitude,
    }


def inline_keyboard(num: int):
    """
    Функция формирует клавиатруру для текста о философе.
    """
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    post_ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Подробнее',
                               url=thinkers[num]['more_info'])
    post_ikb.add(ib1)
    return post_ikb
