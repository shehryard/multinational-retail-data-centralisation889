import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from database_utils import DatabaseConnector

class DataExtractor:

    """
    Note:
        To use the class, you need to pass an instance of the DatabaseConnector class when initializing DataExtractor.
    """
    
    def __init__(self, db_connector):
        self.db_connector = db_connector

    # Read user_data data from the RDS table
    def read_rds_table(self, db_connector, table_name):
        try:
            # Initialize the database engine
            engine = db_connector.init_db_engine()
            # Construct the SQL query to select all data from the specified table
            query = f"SELECT * FROM {table_name}"
            # Read the data from the table into a DataFrame
            df = pd.read_sql(query, engine)
            # Drop the 'index' column if it exists
            if 'index' in df.columns:
                df = df.drop(columns=['index'])
            return df
        except SQLAlchemyError as e:
            print(f"Error reading table '{table_name}': {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

db_connector = DatabaseConnector()
user_table_name = 'legacy_users'
data_extractor = DataExtractor(db_connector)
user_df = data_extractor.read_rds_table(db_connector, user_table_name)
print (user_df)
print(type(user_df))