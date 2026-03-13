import os

class Config:
    MYSQL_HOST     = os.environ.get('MYSQLHOST', 'localhost')
    MYSQL_USER     = os.environ.get('MYSQLUSER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQLPASSWORD', '')
    MYSQL_DB       = os.environ.get('MYSQLDATABASE', 'eps_citas')
    MYSQL_PORT     = int(os.environ.get('MYSQLPORT', 3306))