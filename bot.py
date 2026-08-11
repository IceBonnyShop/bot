import telebot
from telebot import types

# ==============================
# НАСТРОЙКИ
# ==============================

BOT_TOKEN = "8626947639:AAGBTUyULQV9y1Rv2-FPVfnQlgvhnzpGKcQ"

bot = telebot.TeleBot(BOT_TOKEN)


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)

    moderation_btn = types.InlineKeyboardButton(
        "🛡️ Модерация",
        callback_data="moderation"
    )

    settings_btn = types.InlineKeyboardButton(
        "⚙️ Настройки",
        callback_data="settings"
    )

    logs_btn = types.InlineKeyboardButton(
        "📋 Журнал",
        callback_data="logs"
    )

    help_btn = types.InlineKeyboardButton(
        "❓ Помощь",
        callback_data="help"
    )

    markup.add(moderation_btn, settings_btn)
    markup.add(logs_btn, help_btn)

    return markup


# ==============================
# КНОПКА НАЗАД
# ==============================

def back_button():
    markup = types.InlineKeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton(
            "🔙 Назад",
            callback_data="back"
        )
    )

    return markup


# ==============================
# /START
# ==============================

@bot.message_handler(commands=["start"])
def start(message):

    text = (
        "🛡️ <b>Добро пожаловать в ChatShield!</b>\n\n"
        "🤖 Я — бот для управления и модерации Telegram-групп.\n\n"
        "С помощью меня ты сможешь настроить защиту "
        "своего чата от спама и нежелательных сообщений.\n\n"
        "👇 <b>Выбери нужный раздел:</b>"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="HTML",
        reply_markup=main_menu()
    )


# ==============================
# ОБРАБОТКА КНОПОК
# ==============================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    # --------------------------
    # МОДЕРАЦИЯ
    # --------------------------

    if call.data == "moderation":

        text = (
            "🛡️ <b>Модерация</b>\n\n"
            "Здесь находятся основные функции защиты группы.\n\n"
            "🔗 Защита ссылок — ❌\n"
            "🚫 Фильтр слов — ❌\n"
            "🤖 Антиспам — ❌\n"
            "⚠️ Предупреждения — ✅\n\n"
            "Выбери функцию:"
        )

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton(
                "🔗 Ссылки",
                callback_data="links"
            ),
            types.InlineKeyboardButton(
                "🚫 Слова",
                callback_data="words"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "🤖 Антиспам",
                callback_data="antispam"
            ),
            types.InlineKeyboardButton(
                "⚠️ Предупреждения",
                callback_data="warnings"
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "🔙 Назад",
                callback_data="back"
            )
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=markup
        )


    # --------------------------
    # НАСТРОЙКИ
    # --------------------------

    elif call.data == "settings":

        text = (
            "⚙️ <b>Настройки</b>\n\n"
            "Здесь будут находиться настройки ChatShield.\n\n"
            "🔗 Ссылки: ❌\n"
            "🚫 Фильтр слов: ❌\n"
            "🤖 Антиспам: ❌\n"
            "⚠️ Предупреждения: ✅"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=back_button()
        )


    # --------------------------
    # ЖУРНАЛ
    # --------------------------

    elif call.data == "logs":

        text = (
            "📋 <b>Журнал модерации</b>\n\n"
            "Пока здесь нет действий.\n\n"
            "Когда бот начнёт модерировать группу, "
            "здесь будут отображаться его действия."
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=back_button()
        )


    # --------------------------
    # ПОМОЩЬ
    # --------------------------

    elif call.data == "help":

        text = (
            "❓ <b>Помощь</b>\n\n"
            "Нужна помощь с настройкой ChatShield?\n\n"
            "В нашей инструкции подробно объясняется:\n"
            "• как добавить бота в группу;\n"
            "• какие права выдать боту;\n"
            "• как настроить модерацию;\n"
            "• как работают функции защиты."
        )

        markup = types.InlineKeyboardMarkup()

        markup.add(
            types.InlineKeyboardButton(
                "📖 Открыть инструкцию",
                url=FAQ_URL
            )
        )

        markup.add(
            types.InlineKeyboardButton(
                "🔙 Назад",
                callback_data="back"
            )
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=markup
        )


    # --------------------------
    # НАЗАД
    # --------------------------

    elif call.data == "back":

        text = (
            "🛡️ <b>ChatShield</b>\n\n"
            "🤖 Панель управления ботом.\n\n"
            "👇 Выбери нужный раздел:"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=main_menu()
        )


    # --------------------------
    # ФУНКЦИИ МОДЕРАЦИИ
    # --------------------------

    elif call.data == "links":

        bot.answer_callback_query(
            call.id,
            "🔗 Защиту ссылок подключим следующим шагом!"
        )


    elif call.data == "words":

        bot.answer_callback_query(
            call.id,
            "🚫 Фильтр слов подключим следующим шагом!"
        )


    elif call.data == "antispam":

        bot.answer_callback_query(
            call.id,
            "🤖 Антиспам подключим следующим шагом!"
        )


    elif call.data == "warnings":

        bot.answer_callback_query(
            call.id,
            "⚠️ Систему предупреждений подключим следующим шагом!"
        )


    # Убираем часики загрузки после нажатия
    bot.answer_callback_query(call.id)


# ==============================
# ЗАПУСК
# ==============================

print("🛡️ ChatShield запущен!")

bot.infinity_polling()