from telegram.ext import (
    ApplicationBuilder,
    CommandHandler
)

from config import TOKEN
from database import create_database
from handlers import start


def main():

    create_database()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
