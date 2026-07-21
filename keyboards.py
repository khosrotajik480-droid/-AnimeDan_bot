from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# دکمه عضویت اجباری
def join_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(

                "📢 عضویت در کانال",

                url="https://t.me/Anime_G_M"

            )

        ],

        [

            InlineKeyboardButton(

                "✅ بررسی عضویت",

                callback_data="check_join"

            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# منوی اصلی
def main_menu():

    keyboard = [

        [

            InlineKeyboardButton(

                "🎬 انتخاب انیمه",

                callback_data="anime_list"

            )

        ],

        [

            InlineKeyboardButton(

                "ℹ️ راهنما",

                callback_data="help"

            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)
