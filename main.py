from database_utils import DatabaseConnector

db_connector = DatabaseConnector()
tables = db_connector.list_db_tables()
print(tables)