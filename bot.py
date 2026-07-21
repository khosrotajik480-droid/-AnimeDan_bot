from telegram.ext import (
    ApplicationBuilder
)

from config import TOKEN
from database import create_database


def main():

    create_database()

    app = ApplicationBuilder().token(TOKEN).build()

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
