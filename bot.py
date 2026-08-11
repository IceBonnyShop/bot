import telebot
from telebot import types

# ==============================
# НАСТРОЙКИ
# ==============================

BOT_TOKEN = "8626947639:AAGBTUyULQV9y1Rv2-FPVfnQlgvhnzpGKcQ"

FAQ_URL = "https://icebonnyshop.github.io/bot/faq.html"

bot = telebot.TeleBot(BOT_TOKEN)


# ==============================
# СОСТОЯНИЕ МОДЕРАЦИИ
# ==============================

moderation_settings = {
    "links": False,
    "words": False,
    "antispam": False,
    "warnings": True
}


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

def main_menu():

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton(
            "🛡️ Модерация",
            callback_data="moderation"
        ),
        types.InlineKeyboardButton(
            "⚙️ Настройки",
            callback_data="settings"
        )
    )

    markup.add(
        types.InlineKeyboardButton(
            "📋 Журнал",
            callback_data="logs"
        ),
        types.InlineKeyboardButton(
            "❓ Помощь",
            callback_data="help"
        )
    )

    return markup


# ==============================
# МЕНЮ МОДЕРАЦИИ
# ==============================

def moderation_menu():

    markup = types.InlineKeyboardMarkup(row_width=2)

    links_status = "✅" if moderation_settings["links"] else "❌"
    words_status = "✅" if moderation_settings["words"] else "❌"
    antispam_status = "✅" if moderation_settings["antispam"] else "❌"
    warnings_status = "✅" if moderation_settings["warnings"] else "❌"

    markup.add(
        types.InlineKeyboardButton(
            f"🔗 Ссылки {links_status}",
            callback_data="toggle_links"
        ),
        types.InlineKeyboardButton(
            f"🚫 Слова {words_status}",
            callback_data="toggle_words"
        )
    )

    markup.add(
        types.InlineKeyboardButton(
            f"🤖 Антиспам {antispam_status}",
            callback_data="toggle_antispam"
        ),
        types.InlineKeyboardButton(
            f"⚠️ Предупреждения {warnings_status}",
            callback_data="toggle_warnings"
        )
    )

    markup.add(
        types.InlineKeyboardButton(
            "🔙 Назад",
            callback_data="back"
        )
    )

    return markup


# ==============================
# ТЕКСТ МОДЕРАЦИИ
# ==============================

def moderation_text():

    links_status = "✅" if moderation_settings["links"] else "❌"
    words_status = "✅" if moderation_settings["words"] else "❌"
    antispam_status = "✅" if moderation_settings["antispam"] else "❌"
    warnings_status = "✅" if moderation_settings["warnings"] else "❌"

    return (
        "🛡️ <b>Модерация</b>\n\n"
        "Здесь находятся основные функции защиты группы.\n\n"
        f"🔗 Защита ссылок — {links_status}\n"
        f"🚫 Фильтр слов — {words_status}\n"
        f"🤖 Антиспам — {antispam_status}\n"
        f"⚠️ Предупреждения — {warnings_status}\n\n"
        "👇 <b>Нажми на функцию, чтобы включить или выключить её:</b>"
    )


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

    # ==========================
    # МОДЕРАЦИЯ
    # ==========================

    if call.data == "moderation":

        bot.edit_message_text(
            moderation_text(),
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=moderation_menu()
        )

        bot.answer_callback_query(call.id)


    # ==========================
    # ССЫЛКИ
    # ==========================

    elif call.data == "toggle_links":

        moderation_settings["links"] = not moderation_settings["links"]

        bot.edit_message_text(
            moderation_text(),
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=moderation_menu()
        )

        status = "включена ✅" if moderation_settings["links"] else "выключена ❌"

        bot.answer_callback_query(
            call.id,
            f"🔗 Защита ссылок {status}"
        )


    # ==========================
    # СЛОВА
    # ==========================

    elif call.data == "toggle_words":

        moderation_settings["words"] = not moderation_settings["words"]

        bot.edit_message_text(
            moderation_text(),
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=moderation_menu()
        )

        status = "включён" if moderation_settings["words"] else "выключен"

        bot.answer_callback_query(
            call.id,
            f"🚫 Фильтр слов {status}"
        )


    # ==========================
    # АНТИСПАМ
    # ==========================

    elif call.data == "toggle_antispam":

        moderation_settings["antispam"] = not moderation_settings["antispam"]

        bot.edit_message_text(
            moderation_text(),
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=moderation_menu()
        )

        status = "включён" if moderation_settings["antispam"] else "выключен"

        bot.answer_callback_query(
            call.id,
            f"🤖 Антиспам {status}"
        )


    # ==========================
    # ПРЕДУПРЕЖДЕНИЯ
    # ==========================

    elif call.data == "toggle_warnings":

        moderation_settings["warnings"] = not moderation_settings["warnings"]

        bot.edit_message_text(
            moderation_text(),
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=moderation_menu()
        )

        status = "включены" if moderation_settings["warnings"] else "выключены"

        bot.answer_callback_query(
            call.id,
            f"⚠️ Предупреждения {status}"
        )


    # ==========================
    # НАСТРОЙКИ
    # ==========================

    elif call.data == "settings":

        text = (
            "⚙️ <b>Настройки</b>\n\n"
            "Настройки ChatShield находятся "
            "в разделе 🛡️ Модерация.\n\n"
            "Там можно включать и выключать "
            "функции защиты."
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=back_button()
        )

        bot.answer_callback_query(call.id)


    # ==========================
    # ЖУРНАЛ
    # ==========================

    elif call.data == "logs":

        text = (
            "📋 <b>Журнал модерации</b>\n\n"
            "Пока здесь нет действий.\n\n"
            "После подключения настоящей модерации "
            "здесь будут отображаться действия бота."
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=back_button()
        )

        bot.answer_callback_query(call.id)


    # ==========================
    # ПОМОЩЬ
    # ==========================

    elif call.data == "help":

        text = (
            "❓ <b>Помощь</b>\n\n"
            "Нужна помощь с настройкой ChatShield?\n\n"
            "В инструкции подробно объясняется:\n"
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

        bot.answer_callback_query(call.id)


    # ==========================
    # НАЗАД
    # ==========================

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

        bot.answer_callback_query(call.id)


# ==============================
# ЗАПУСК
# ==============================

print("🛡️ ChatShield запущен!")

bot.infinity_polling()
