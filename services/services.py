from database.sqlite import sql_get_articles, sql_add_section, sql_get_sections
from keyboards.admin_keyboard import LEXICON_KEYBOARDS_ADMIN


async def get_articles() -> str:
    data: list[tuple[str | int]] = await sql_get_articles()
    sections_list: list[tuple[int | str]] = sorted(await sql_get_sections(), key=lambda x: x[2])
    sections: dict[int, str] = {i[0]: i[1] for i in sections_list}

    articles: dict[str, list[list[str | int]]] = {}

    for one in data:
        title: str = one[1]
        emoji: str = one[2]
        link: str = one[3]
        section: str = sections[one[5]]
        position: str = one[6]
        is_published: bool = one[7]

        if is_published:
            if section in articles:
                articles[section].append([emoji, title, link, position])
            else:
                articles[section] = [[emoji, title, link, position]]

    text: str = ''

    for section in sections.values():
        if section in articles:
            text += f'{section}\n'
            for article in sorted(articles[section], key=lambda x: x[3]):
                text += f'{article[0]} <a href="{article[2]}">{article[1]}</a>\n'
            text += '\n'

    return text


async def handle_section(text: str) -> int:
    sections: list[tuple[int | str]] = await sql_get_sections()

    for section in sections:
        if text in section:
            return section[0]

    return await sql_add_section(text)


async def handle_article_data(data: dict[str, str | list | int | bool]) -> dict[str, str | list | int | bool]:
    # data['keywords'].split(', ')
    data['section'] = await handle_section(data['section'])
    data['is_available'] = data['is_available'] == LEXICON_KEYBOARDS_ADMIN['available_button'][-1:]

    return data
