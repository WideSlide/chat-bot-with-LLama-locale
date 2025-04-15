from aiogram import Router, types
from handlers.gpt import send_message_gpt

user_private = Router()


@user_private.message()
async def chat_gpt(message: types.Message):
    if len(message.text) > 150:
        await message.answer('Введите сообщение короче')
        return
    answer = send_message_gpt(message=message.text, user_id=message.from_user.id)
    await message.answer(answer)
