LEXICON_ADMIN: dict[str, str] = {
    'success': '✅ Операция успешно завершена ✅',
    '/cancel1': 'Никакой процесс пока не запущен 👀',
    '/cancel2': '⛔️ Операция остановлена. ⛔️ Чтобы начать сначала, введите нужную команду',
    'fill_title': 'Введите название новой статьи ✏️',
    'fill_emoji': 'Отправьте смайлик к статье (он должен ассоциироваться с названием статьи) 🤪',
    'fill_link': 'Отправьте ссылку на статью 🔗',
    'fill_keywords': 'Отправьте ключевые слова через запятую с пробелами 🔎',
    'fill_section': 'Выберите на клавиатуре один из существующих разделов или введите название нового 🗂',
    'fill_position': 'Введите номер позиции, на которую надо поместить статью. 🔢 Текущие статьи раздела <b>{section}</b>:\n'
                     '{articles}',
    'fill_is_published': 'Выберите на клавиатуре, сделать ли статью доступной для пользователей 🔑',
    'check_data': 'Проверьте правильность введённых данных 🛂\n\n'
                  '<b>Название:</b> {title}\n'
                  '<b>Смайлик:</b> {emoji}\n'
                  '<b>Ссылка:</b> {link}\n'
                  '<b>Ключевые слова:</b> {keywords}\n'
                  '<b>Раздел:</b> {section}\n'
                  '<b>Позиция:</b> {position}\n'
                  '<b>Доступ:</b> {is_published}',
    'warning_keyboard': '⚠️ Для ответа на предыдущее сообщение воспользуйтесь специальной клавиатурой ⚠️'
}

LEXICON_COMMANDS_ADMIN: dict[str, str] = {
    '/cancel': '⛔️ Остановить операцию',
    '/allarticles': '🔐 Подробно про статьи',
    # '/addlang': '➕ Добавить яп',
    # '/editlang': '✏️ Редактировать яп',
    # '/orderlang': '🔢 Изменить порядок яп',
    # '/dellang': '❌ Удалить яп',
    # '/addsection': '➕ Добавить раздел',
    # '/editsection': '✏️ Редактировать раздел',
    # '/ordersection': '🔢 Изменить порядок разделов',
    # '/delsection': '❌ Удалить раздел',
    '/addarticle': '➕ Добавить статью',
    # '/editarticle': '✏️ Редактировать статью',
    # '/orderarticle': '🔢 Изменить порядок статей',
    # '/delarticle': '❌ Удалить статью'
}

LEXICON_KEYBOARDS_ADMIN: dict[str, str] = {
    'is_published_button': 'Открыть доступ ✅',
    'not_is_published_button': 'Закрыть доступ ❌',
    'allow_publishing_button': 'Опубликовать ✅',
    'not_allow_publishing_button': 'Отменить ❌'
}

LEXICON_OTHER_ADMIN: dict[str, str] = {
    'is_published': '✅',
    'not_is_published': '❌'
}
