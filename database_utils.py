import yaml
from sqlalchemy import create_engine, text

class DatabaseConnector:
    def __init__(self):
        
        self.db_creds = self.read_db_creds()

    def read_db_creds(self):
        try:
            with open('db_creds.yaml', 'r') as yaml_file:
                db_creds = yaml.safe_load(yaml_file)
                return db_creds
        except FileNotFoundError:
            print("db_creds.yaml file not found. Please ensure it is created correctly.")
            return{}

    def init_db_engine (self):
        db_url = f"postgresql://{self.db_creds['RDS_USER']}:{self.db_creds['RDS_PASSWORD']}@{self.db_creds['RDS_HOST']}:{self.db_creds['RDS_PORT']}/{self.db_creds['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine
        
        
