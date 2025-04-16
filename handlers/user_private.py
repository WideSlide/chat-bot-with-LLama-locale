from aiogram import Router, types, F
from aiogram.filters import Command
from utils.gpt import send_message_gpt
from utils.gpt import db


user_private = Router()


@user_private.message(Command('start'))
async def start_chat(message: types.Message):
    await message.answer('Добро пожаловать в чат с нейросетью')



@user_private.message(Command('delete_history'))
async def del_history(message: types.Message):
    db.del_user_history(message.from_user.id)
    await message.answer('История сообщений удалена')


@user_private.message()
async def chat_gpt(message: types.Message):
    if len(message.text) > 150:
        await message.answer('Введите сообщение короче')
        return
    answer = send_message_gpt(message=message.text, user_id=message.from_user.id)
    await message.answer(answer)
