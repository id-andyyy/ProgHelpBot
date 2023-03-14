import sqlite3


def sql_start(name: str) -> None:
    global db, cur

    db = sqlite3.connect(name)
    db.execute('PRAGMA foreign_keys=on')
    cur = db.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS sections('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'title TEXT NOT NULL, '
                'position INTEGER NOT NULL)')
    cur.execute('CREATE TABLE IF NOT EXISTS articles('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'title TEXT NOT NULL, '
                'emoji TEXT, '
                'link TEXT, '
                'keywords TEXT, '
                'section INTEGER NOT NULL, '
                'position INTEGER NOT NULL, '
                'is_available BOOL NOT NULL, '
                'FOREIGN KEY (section) REFERENCES sections(id))')
    db.commit()


async def sql_add_article(data: dict[str, str | list | int | bool]) -> None:
    cur.execute('INSERT INTO articles VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
    db.commit()


async def sql_get_articles() -> list[tuple[str | int]]:
    articles: list[tuple[str | int]] = cur.execute('SELECT * FROM articles').fetchall()
    return articles


async def sql_add_section(title: str) -> int:
    position: int = len(await sql_get_sections()) + 1
    cur.execute('INSERT INTO sections VALUES (NULL, ?, ?)', (title, position))
    db.commit()

    return position


async def sql_get_sections() -> list[tuple[str | int]]:
    sections: list[tuple[str | int]] = cur.execute('SELECT * FROM sections').fetchall()
    return sections
