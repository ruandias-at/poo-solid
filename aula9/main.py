from repositorio import Repositorio
from databases import PostgresDB
from databases import MySQLDB

db_postgres = PostgresDB()
db_mysql = MySQLDB()
repo = Repositorio()
repo.insert(db_postgres)
print()
repo.select(db_mysql)