from database_utils import DatabaseConnector
from data_extraction import DataExtractor

db_connector = DatabaseConnector()
tables = db_connector.list_db_tables()
print(tables)

user_table_name = 'legacy_users'
data_extractor = DataExtractor(db_connector)
user_df = data_extractor.read_rds_table(db_connector, user_table_name)
print (user_df)
print(type(user_df))