import sqlite3

class DataBase:
    def __init__(self, name_db: str):
        self.name_db = name_db
        self.connect = sqlite3.connect(self.name_db)
        self.cursor = self.connect.cursor()


    def create_table(self):
        self.cursor.execute('''CREATE TABLE 
                            IF NOT EXISTS 
                            users_chat(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id BIGINT NOT NULL,
                            role VARCHAR(10) NOT NULL,
                            context TEXT)''')
    
    def save_message(self, user_id: int, role: str, context: str):
        self.cursor.execute('''INSERT INTO users_chat (user_id, role, context) VALUES(?,?,?)''', (user_id, role, context))
        self.connect.commit()

    
    def get_user_chat(self, user_id) -> list[dict]:
        user = self.cursor.execute('''SELECT role, context FROM users_chat WHERE user_id = ?''', (user_id,)).fetchall()
        if not user:
            return []
        return [{'role': role, 'content':context} for role, context in user]

    def del_user_history(self, user_id):
        self.cursor.execute('''DELETE FROM users_chat
                            WHERE user_id = ?''', (user_id,))
        self.connect.commit()

    def drop_table(self):
        self.cursor.execute('''DROP TABLE users_chat''')



