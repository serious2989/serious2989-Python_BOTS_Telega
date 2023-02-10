from asyncio import sleep

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import action_callback
from keyboards.inline.choice_buttons import choice_xo
from keyboards.inline.choice_buttons import fun_choice
from loader import dp, logger
from main import check_win
from main import place_sign
import loader

player = ''
bot = ''
win_list = []
table_dict = {}
counter = 0
token = ""


@dp.message_handler(Command("start"))
async def show_field(message: Message):
    global table_dict, counter

    table_dict = {i: k for i, k in zip(range(1, 10), "123456789")}
    counter = 0
    await message.answer(text="Let's play. Choice your sign",
                         reply_markup=choice_xo)


@dp.callback_query_handler(action_callback.filter(item_name=["X", "O"]))
async def choice_sign(call: CallbackQuery, callback_data: dict):
    global player, bot, token
    await call.answer(cache_time=10)
    player = callback_data["item_name"]
    # bot = "X" if player == "O" else "O"
    token = player
    await call.message.answer(text="Choice a number",
                              reply_markup=fun_choice(table_dict))
    await sleep(2)
    await loader.bot.delete_message(chat_id=call.from_user.id,
                                    message_id=call.message.message_id)


@dp.callback_query_handler(action_callback.filter(item_name=["1", "2", "3", "4", "5", "6", "7", "8", "9"]))
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global table_dict, counter, token

    counter += 1
    text = "Ходит игрок"
    data = callback_data["item_name"]

    answer = place_sign(token, data, table_dict)
    if not isinstance(answer, str):
        table_dict = answer
        token = "O" if token == "X" else "X"
    else:
        text = answer

    await call.answer(cache_time=1)

    await call.message.edit_text(f"{text} {token}",
                                 reply_markup=fun_choice(table_dict))
    if counter > 3:
        if check_win(table_dict):
            await call.message.edit_text(
                f"{check_win(table_dict)} - WIN{chr(127942)}{chr(127881)}!",
                reply_markup=fun_choice(table_dict))
            await restart(call)

    if counter == 9:
        await call.message.edit_text(f"Drawn game {chr(129318)}{chr(129309)}!",
                                     reply_markup=fun_choice(table_dict))
        await restart(call)

    logger.debug(f'Пользователь ввел {token} {text}')


async def restart(call):
    await show_field(call.message)
    await sleep(2)
    await loader.bot.delete_message(chat_id=call.from_user.id,
                                    message_id=call.message.message_id)


@dp.message_handler()
async def echo(message: Message):
    logger.debug('Не верный ввод пользователем')
    await message.answer(f'{message.from_user.first_name},'
                         f' пожалуйста, кликай кнопки калькулятора!',
                         reply_markup=fun_choice(table_dict))
