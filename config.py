import json

db = {
    "user": "root",
    "password": "rlawoals2!",
    "host": "127.0.0.1",
    "port": 3306,
    "database": "fmms"
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

with open("model/checkpoint/sencnn.json", mode="r") as io:
    MODEL = json.load(io)
