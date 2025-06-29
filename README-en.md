![Art](https://i.postimg.cc/05Mg33FL/art.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/Musical-Studying?style=flat&color=70F34A)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/Musical-Studying?style=flat&color=black)
![Pet Project](https://img.shields.io/badge/pet-project-8400FF)

# ProgHelpBot&nbsp;👨‍💻

A Telegram bot that serves as a cheat sheet for Python syntax. Created as a school project&nbsp;🎓.

## Functionality

A Telegram bot that acts as a knowledge base. Users can view articles by section and search by keywords&nbsp;🔎. Administrators can manage content by adding new articles. The bot is designed to provide structured information and quick access to it&nbsp;🗂️. A list of all articles can be found at this [link](https://telegra.ph/python-articles-04-06-2).

### User Commands

- 🏃&nbsp;`/start` - welcome message
- ❓&nbsp;`/help` - help on using the bot
- 📚&nbsp;`/articles` - view all published articles, grouped by section
- 🔎&nbsp;`/search` - search instructions
- 📨&nbsp;`/report`, `/feedback` - commands for feedback
- 👤&nbsp;`/creator` - information about the creator
- 🔎&nbsp;`any text input` - the bot treats any text input as a search query and looks for relevant articles

### Admin Commands

- ✍️&nbsp;`/addarticle` - starts the process of adding a new article through a step-by-step dialog (FSM)
- 📋&nbsp;`/allarticles` - view all articles, including unpublished ones
- ❌&nbsp;`/cancel` - cancel the current action (e.g., adding an article)

## Screenshots

![Getting Started](https://i.postimg.cc/3RGRcqQv/1.png)
![Search](https://i.postimg.cc/nLc70wb2/2.png)
![Adding Articles](https://i.postimg.cc/CLTqWKpz/3.png)

## Technologies and Tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![aiogram](https://img.shields.io/badge/aiogram-005571?style=for-the-badge&color=019cfb)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![nltk](https://img.shields.io/badge/nltk-85C1E9?style=for-the-badge&color=85C1E9)
![fuzzywuzzy](https://img.shields.io/badge/fuzzywuzzy-FF5733?style=for-the-badge&color=FF5733)
![Telegraph](https://img.shields.io/badge/telegraph-2A5DB0?style=for-the-badge&color=2A5DB0)


- **Programming Language**: Python 3
- **Framework for Telegram Bot API**: `aiogram` 3.8.0
- **Database**: `SQLite`
- **Dependency Management**: `pip` and `requirements.txt`
- **Natural Language Processing (NLP)**:
    - `nltk` (SnowballStemmer) for stemming (reducing words to their root form) in Russian.
    - `fuzzywuzzy` and `python-Levenshtein` for fuzzy keyword search.
- **Configuration Management**: `environs` for loading settings from an `.env` file.

## Technical Decisions:

- **Modular Architecture**: The project is divided into logical components (`handlers`, `services`, `database`, `keyboards`, `lexicon`, `states`, `config_data`), which simplifies its maintenance and development.
- **Use of Routers**: `aiogram.Router` is used to separate handlers into user and admin handlers.
- **Finite State Machine (FSM)**: The process of adding an article uses a finite state machine (`aiogram.fsm`), which guides the user step-by-step.
- **Separation of Texts into a "Lexicon"**: All bot text messages are stored in separate files in the `lexicon` directory. This simplifies text management and potential localization.
- **Access Rights Separation**: Clear distinction between functionality for regular users and administrators. Access to admin commands is checked using a custom `IsAdmin` filter.
- **Intelligent Search**: The search mechanism uses stemming to normalize the query and keywords, as well as fuzzy string matching to find relevant matches, which improves search quality.
- **Configuration Storage**: Sensitive data (bot token, admin IDs) and settings (DB file name) are stored in the `.env` file and are not included in the version control system.
- **Articles**: The articles themselves are written on the Telegraph platform. You can get a list of articles [here](https://telegra.ph/python-articles-04-06-2).

## Getting Started

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/id-andyyy/ProgHelpBot.git
    cd ProgHelpBot
    ```
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows: .venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` configuration file** in the project's root directory and add the following variables to it:
    ```env
    BOT_TOKEN=YOUR_BOT_TOKEN
    ADMIN_IDS=ADMIN_ID_1,ADMIN_ID_2
    DATABASE=proghelpbot.db
    ```
    - `BOT_TOKEN`: your Telegram bot token.
    - `ADMIN_IDS`: comma-separated administrator IDs.
    - `DATABASE`: name of the SQLite database file.

5.  **Run the bot**:
    ```bash
    python bot.py
    ```

## Project Structure

```
.
├── config_data/
│   └── config.py           # Loading and processing configuration from .env
│
├── database/
│   └── sqlite.py           # Functions for interacting with SQLite (creating tables, CRUD operations)
│
├── filters/
│   └── is_admin.py         # Filter to check if a user is an administrator
│
├── handlers/
│   ├── admin_handlers.py   # Handlers for administrators
│   └── user_handlers.py    # Handlers for regular users
│
├── keyboards/
│   ├── admin_keyboard.py   # Keyboards for the admin menu
│   └── set_menu.py         # Setting the bot's menu buttons
│
├── lexicon/
│   ├── admin_lexicon.py    # Texts for admin commands
│   ├── other_lexicon.py    # Other common texts
│   └── user_lexicon.py     # Texts for user commands
│
├── services/
│   └── services.py         # Main functions for data processing, article search, etc.
│
├── states/
│   └── admin_states.py     # States for admin scenarios (adding an article)
│
├── .env                    # Configuration file (to be created manually)
├── .env.example            # Example of .env content
├── .gitignore              # File to exclude files and folders from Git
├── bot.py                  # Main file to run the bot, the application's entry point
└── requirements.txt        # List of project dependencies
```

## Feedback

I would be grateful if you give a star&nbsp;⭐️. If you find a bug or have suggestions for improvement,
use the [Issues](https://github.com/id-andyyy/ProgHelpBot/issues) section.

Читать на [русском&nbsp;🇷🇺](README.md)
