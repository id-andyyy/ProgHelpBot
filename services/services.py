from fuzzywuzzy import fuzz
from nltk import SnowballStemmer

from database.sqlite import sql_get_articles, sql_add_section, sql_get_sections

from keyboards.admin_keyboard import LEXICON_KEYBOARDS_ADMIN

from lexicon.lexicon_admin import LEXICON_OTHER_ADMIN
from lexicon.lexicon_user import LEXICON_USER
from lexicon.lexicon_other import LEXICON_OTHER

stemmer: SnowballStemmer = SnowballStemmer("russian")


async def get_sections() -> dict[int, str]:
    return {i[0]: i[1] for i in sorted(await sql_get_sections(), key=lambda x: x[2])}


async def add_section(text: str) -> int:
    sections: list[tuple[int | str]] = await sql_get_sections()

    for section in sections:
        if text in section:
            return section[0]

    return await sql_add_section(text)


async def get_articles(only_section: str = None, unpublished_articles: bool = False) -> dict[
    str, list[dict[str, str | int]]]:
    data: list[tuple[str | int]] = await sql_get_articles()
    sections: dict[int, str] = await get_sections()

    articles: dict[str, list[dict[str, str | int]]] = {}

    for row in data:
        title: str = row[1]
        emoji: str = row[2]
        link: str = row[3]
        keywords: str = row[4]
        section: str = sections[row[5]]
        position: str = row[6]
        is_published: bool = row[7]

        if (only_section is None or section == only_section) and (is_published or unpublished_articles):
            if section not in articles:
                articles[section] = []
            articles[section].append(dict(title=title,
                                          emoji=emoji,
                                          link=link,
                                          keywords=keywords,
                                          position=position,
                                          is_published=is_published))

    return dict(sorted(articles.items(), key=lambda x: list(sections.values()).index(x[0])))  # TO DO: incorrect type


async def print_articles(data: dict[str, list[dict[str, str | int]]] = None, only_section: str = None,
                         unpublished_articles: bool = False, new_article: bool = False,
                         search_mode: bool = False) -> str:
    if data is None:
        data = await get_articles(only_section=only_section, unpublished_articles=unpublished_articles)

    text: str = ''

    if len(data) != 0:
        for section, articles in data.items():
            if only_section is None:
                text += f'<b>{section}</b>\n'
            for article in sorted(articles, key=lambda x: x["position"]):
                text += f'{str(article["position"]) + ". " if unpublished_articles else ""}{article["emoji"]} ' \
                        f'<a href="{article["link"]}">{article["title"]}</a>' \
                        f'{" " + (LEXICON_OTHER_ADMIN["is_published"] if article["is_published"] else LEXICON_OTHER_ADMIN["not_is_published"]) if unpublished_articles else ""}\n'
            text += '\n'

        if only_section is not None and new_article:
            text = text[:-1] + f'{data[only_section][-1]["position"] + 1}...'

        if search_mode:
            text = LEXICON_USER['find_articles'].format(results=text)
        else:
            text = LEXICON_OTHER['articles'].format(articles=text)
    else:
        if only_section:
            text += '1...'
        elif search_mode:
            text += LEXICON_USER['not_found']
        else:
            text += LEXICON_OTHER['empty_list']

    return text


async def find_articles(text: str) -> dict[str, list[dict[str, str | int]]]:
    words: list[str] = [stemmer.stem(word) for word in text.lower().split(' ')]
    data: dict[str, list[dict[str, str | int]]] = await get_articles()

    results: dict[str, list[dict[str, str | int]]] = {}

    for section, articles in data.items():
        for article in articles:
            if article['keywords'] is not None:
                stop = False
                for word in words:
                    for keyword in article['keywords'].split(','):
                        if fuzz.ratio(word, keyword) > 65:
                            if section not in results:
                                results[section] = []
                            results[section].append(article)
                            stop = True

                            break

                    if stop:
                        break

    return results


async def handle_article_data(data: dict[str, str | list | int | bool]) -> dict[str, str | list | int | bool]:
    data['keywords'] = ','.join(sorted([stemmer.stem(word) for word in data['keywords'].split(',')]))
    data['section'] = await add_section(data['section'])
    data['is_published'] = data['is_published'] == LEXICON_KEYBOARDS_ADMIN['is_published_button'][-1:]

    return data
