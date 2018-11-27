def  get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    mysql = DATABASE.get('mysql') or 'pymysql'
    username =DATABASE.get('username') or 'root'
    password =DATABASE.get('password') or '123456'
    host = DATABASE.get('host') or 'localhost'
    port = DATABASE.get('port') or '3306'
    db =DATABASE.get('db') or 'taopp'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect, mysql, username, password, host, port, db)

class Config():
    TEST=True
    DEBUG = True
    SECERT_KEY = '120'
    SESSION_TYPE ='redis'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'mysql':'pymysql',
        'username':'root',
        'password': '123456',
        'host': 'localhost',
        'port': '3306',
        'db': 'blogdb',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

env ={
        'develop':DevelopConfig
    }

