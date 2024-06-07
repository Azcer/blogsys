#数据库配置信息
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'qasystem'
USERNAME = 'root'
PASSWORD = 'as1234567'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI


#邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '2425368064@qq.com'
MAIL_PASSWORD = 'jafzijcrytdqdjce'
MAIL_DEFAULT_SENDER = '2425368064@qq.com' 


SECRET_KEY = "dsadjkjxzkljcsoopw21321"