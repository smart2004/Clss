# Singleton should have just one class instance only

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'conection to DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('close connection with DB')

    def read(self):
        return 'DB data'
    
    def write(self, data):
        print(f'write to DB {data}')

db = DataBase('smart2004', '1234', 80)
db2 = DataBase('smart200481xx', '5678', 50)
print(id(db), id(db2))

db.connect()
db2.connect()

