from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Main keyboard
def get_main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="/start"),
                KeyboardButton(text="/help"),
                KeyboardButton(text="/info")
            ]
        ],
        resize_keyboard=True
    )

