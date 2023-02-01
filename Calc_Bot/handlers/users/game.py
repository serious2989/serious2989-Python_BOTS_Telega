from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_data import action_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, logger
from mod_calc import sum_data, sub_data, mul_data, div_data

operator = {"+": sum_data, "-": sub_data, "*": mul_data, "/": div_data}
nums = ""


@dp.message_handler(Command("start"))
async def show_field(message: Message):
    await message.answer(text="Let's calculate",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains="<")
async def delete_char(call: CallbackQuery):
    global nums
    if nums:
        nums = nums[:-1]
        if not nums:
            await call.message.edit_text("0", reply_markup=choice)
        await call.message.edit_text(f"{nums}", reply_markup=choice)
    else:
        await call.answer(cache_time=20)


@dp.callback_query_handler(text_contains="C")
async def erase(call: CallbackQuery):
    global nums
    nums = ""
    await call.message.edit_text("0", reply_markup=choice)


@dp.callback_query_handler(text_contains="=")
async def result(call: CallbackQuery):
    global nums

    await call.answer(cache_time=10)

    if nums:
        nums_list = nums.split()
        if len(nums_list) > 1:
            try:
                check_list = [float(i) if "." in i else int(i)
                              if i.replace(".", "", 1).isdigit()
                              else i for i in nums_list]

                ind_list = [i for i, v in enumerate(check_list) if isinstance(v, str) and v in "*/"]

                # Работа с приоритетными операциями
                while ind_list:
                    k = ind_list[0]
                    a, s, b = check_list[k - 1: k + 2]
                    check_list[k - 1: k + 2] = [operator[s](a, b)]
                    ind_list = [i for i, v in enumerate(check_list) if isinstance(v, str) and v in "*/"]

                while len(check_list) > 1:
                    f, op, s = check_list[:3]
                    check_list[:3] = [operator[op](f, s)]

            except (ValueError, TypeError, KeyError):
                await call.message.edit_text("Введите значения", reply_markup=choice)
            else:
                await call.message.edit_text(f"{nums}"
                                             f" = {check_list[0]}",
                                             reply_markup=choice)
                logger.debug(f'Результат {nums} = {check_list[0]}')
            nums = ""
    else:
        logger.debug(f'Пользователь не ввел значения')
        await call.message.edit_text("Введите значения", reply_markup=choice)


@dp.callback_query_handler(action_callback.filter())
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global nums

    await call.answer(cache_time=1)
    data = callback_data["item_name"]
    if data in "+-*/":
        nums += f" {data} "
    else:
        nums += data
    await call.message.edit_text(f"{nums}",
                                 reply_markup=choice)
    logger.debug(f'Пользователь ввел {nums}')


@dp.message_handler()
async def echo(message: Message):
    logger.debug('Не верный ввод пользователем')
    await message.answer(f'{message.from_user.first_name},'
                         f' пожалуйста, кликай кнопки калькулятора!',
                         reply_markup=choice)
