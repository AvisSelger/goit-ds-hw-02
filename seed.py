import sqlite3
from faker import Faker

fake = Faker()

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

status_values = ['new', 'in progress', 'completed']
cursor.executemany('INSERT INTO status (name) VALUES (?)', [(s,) for s in status_values])

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute('INSERT INTO users (fullname, email) VALUES (?, ?)', (fullname, email))

user_ids = [row[0] for row in cursor.execute('SELECT id FROM users')]
status_ids = [row[0] for row in cursor.execute('SELECT id FROM status')]

for _ in range(20):
    title = fake.sentence()
    description = fake.text()
    status_id = fake.random.choice(status_ids)
    user_id = fake.random.choice(user_ids)
    cursor.execute('INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)', (title, description, status_id, user_id))

conn.commit()
conn.close()
