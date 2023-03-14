import sqlite3


def sql_start(name: str) -> None:
    global db, cur

    db = sqlite3.connect(name)
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS articles('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'title TEXT, '
                'emoji TEXT, '
                'link TEXT, '
                'keywords TEXT, '
                'section INTEGER, '
                'position INTEGER, '
                'is_available BOOL)')
    db.commit()


async def sql_add_article(data: dict[str, str | list | int | bool]) -> None:
    cur.execute('INSERT INTO articles VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
    db.commit()
