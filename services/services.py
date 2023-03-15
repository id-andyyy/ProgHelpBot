from database.sqlite import sql_get_articles, sql_add_section, sql_get_sections
from keyboards.admin_keyboard import LEXICON_KEYBOARDS_ADMIN
from lexicon.lexicon_admin import LEXICON_OTHER_ADMIN


async def get_articles(only_section: str = None, secret_articles: bool = False, new_article: bool = False) -> str:
    data: list[tuple[str | int]] = await sql_get_articles()
    sections: dict[int, str] = {i[0]: i[1] for i in sorted(await sql_get_sections(), key=lambda x: x[2])}

    articles: dict[str, list[dict[str, str | int | bool]]] = {}

    for row in data:
        title: str = row[1]
        emoji: str = row[2]
        link: str = row[3]
        section: str = sections[row[5]]
        position: str = row[6]
        is_published: bool = row[7]

        if (only_section is None or section == only_section) and (is_published or secret_articles):
            if section not in articles:
                articles[section] = []
            articles[section].append(dict(emoji=emoji,
                                          title=title,
                                          link=link,
                                          position=position,
                                          is_published=is_published))

    text: str = ''

    if len(articles) != 0:
        for section in sections.values():
            if section in articles:
                if only_section is None:
                    text += f'<b>{section}</b>\n'
                for article in sorted(articles[section], key=lambda x: x["position"]):
                    text += f'{str(article["position"]) + ". " if secret_articles else ""}{article["emoji"]} ' \
                            f'<a href="{article["link"]}">{article["title"]}</a>' \
                            f'{" " + (LEXICON_OTHER_ADMIN["is_published"] if article["is_published"] else LEXICON_OTHER_ADMIN["not_is_published"]) if secret_articles else ""}\n'
                text += '\n'

        if only_section is not None and new_article:
            text = text[:-1] + f'{articles[only_section][-1]["position"] + 1}...'
    else:
        text += '1...'

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
    data['is_published'] = data['is_published'] == LEXICON_KEYBOARDS_ADMIN['is_published_button'][-1:]

    return data
