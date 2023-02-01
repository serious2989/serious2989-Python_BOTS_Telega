from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="+", callback_data="move:+"),
            InlineKeyboardButton(text="-", callback_data="move:-"),
            InlineKeyboardButton(text="*", callback_data="move:*"),
            InlineKeyboardButton(text="/", callback_data="move:/"),
        ],
        [
            InlineKeyboardButton(text="1", callback_data="move:1"),
            InlineKeyboardButton(text="2", callback_data="move:2"),
            InlineKeyboardButton(text="3", callback_data="move:3"),
            InlineKeyboardButton(text="4", callback_data="move:4"),
        ],
        [
            InlineKeyboardButton(text="5", callback_data="move:5"),
            InlineKeyboardButton(text="6", callback_data="move:6"),
            InlineKeyboardButton(text="7", callback_data="move:7"),
            InlineKeyboardButton(text="8", callback_data="move:8"),
        ],
        [
            InlineKeyboardButton(text="9", callback_data="move:9"),
            InlineKeyboardButton(text="0", callback_data="move:0"),
            InlineKeyboardButton(text=".", callback_data="move:."),
            InlineKeyboardButton(text="=", callback_data="move:="),
        ],
        [
            InlineKeyboardButton(text="<", callback_data="move:<"),
            InlineKeyboardButton(text="C", callback_data="move:C"),
        ],
    ]
)
