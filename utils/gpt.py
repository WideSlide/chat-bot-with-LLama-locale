import requests
from database.db import DataBase

db = DataBase('chat.db')
db.create_table()

def send_message_gpt(message: str, user_id: int) -> str:
    url: str = 'http://localhost:1234/v1/chat/completions'
    model: str = 'meta-llama-3.1-8b-instruct'
    #Формируем запрос
    history = db.get_user_chat(user_id)

    #print(history)
    
    #Добавляем наше сообщение даже если нет истории
    history.append({'role':'user', 'content': message})

    data = {
            'model': model,
            'messages': [
                {'role':'system', 'content':''},
                *history],
            'stream': False,
            'max_tokens': -1,
            'temperature': 0.3
        }
    
    try:
        #Получаем сообщение от нейросети
        request = requests.post(url= url, json= data)
        response = request.json()

        text = response['choices'][0]['message']['content']
        #Сохраняем в базу
        db.save_message(user_id, role='user', context=message)
        db.save_message(user_id, role='assistant', context=text)

        return text
    
    except Exception as e:
        print('Нет связи с сервером')


