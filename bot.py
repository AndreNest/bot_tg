from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
import asyncio
import bot_def
bot = Bot(token='5976171943:AAE7JafOPEiScPyIAHuUyCapfJxpTUwPJXY')


dp = Dispatcher(bot)
cb = CallbackData('ikb', 'action')
def create_keyboard():

    kb_start = ReplyKeyboardMarkup(resize_keyboard=True) #argument one_time_keyboard=True
    b1 = KeyboardButton('/wether')
    b2 = KeyboardButton('тест')
    kb_start.add(b1).insert(b2)
    return kb_start

def create_InlineKeyboard_inrease_decrease() -> InlineKeyboardMarkup:
    ikb2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Moskow',
                              callback_data='btn_mosсkow'),
         InlineKeyboardButton(text='Tula',
                              callback_data='btn_tula')],
        [InlineKeyboardButton(text='Omsk',
                              callback_data='btn_omsk'),
         InlineKeyboardButton(text='Kirov',
                              callback_data='btn_kirov')]
    ])
    return ikb2


@dp.callback_query_handler(cb.filter())
async def ikb_callback_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('Somthing!')

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message) -> None:
    await message.answer('Что будем делать?',
                         reply_markup=create_keyboard())


@dp.message_handler(commands='wether')
async def cmd_wether(message: types.Message) -> None:
    await message.answer('В каком городе узнать темпиратуру?', reply_markup=create_InlineKeyboard_inrease_decrease())

@dp.callback_query_handler(lambda callback_qerry: callback_qerry.data.startswith('btn'))
async def inline_keyboard_callback_handler(callback: types.CallbackQuery) -> None:
    if callback.data == 'btn_mosсkow':
        await callback.message.edit_text(f'Темпиратура воздуха в Москве = {bot_def.wether("Москва")}',
                                         reply_markup=create_InlineKeyboard_inrease_decrease())
    elif callback.data == 'btn_tula':
        await callback.message.edit_text(f'Темпиратура воздуха в Туле = {bot_def.wether("tula")}',
                                         reply_markup=create_InlineKeyboard_inrease_decrease())
    elif callback.data == 'btn_omsk':
        await callback.message.edit_text(f'Темпиратура воздуха в Омске = {bot_def.wether("omsk")}',
                                         reply_markup=create_InlineKeyboard_inrease_decrease())
    elif callback.data == 'btn_kirov':
        await callback.message.edit_text(f'Темпиратура воздуха в Кирове {bot_def.wether("kirov")}',
                                         reply_markup=create_InlineKeyboard_inrease_decrease())
    else:
        1 / 0

@dp.message_handler(commands='start_test_block')
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer('Test blocked')

@dp.errors_handler(exception=BotBlocked)
async def bot_blocked_handler(updates: types.Update, exception: BotBlocked ) ->bool:
    print('Не могу отправить сообщение, так как меня блокирнули ')

    return True


@dp.callback_query_handler(text='close')
async def ikb_cb_close_handrel(callback: types.CallbackQuery):
    await callback.message.delete()



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)