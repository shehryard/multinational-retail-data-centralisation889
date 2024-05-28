import yaml

class DatabaseConnector:
    def __init__(self):
        pass

    def read_db_creds(self):
        try:
            with open('db_creds.yaml', 'r') as yaml_file:
                db_creds = yaml.safe_load(yaml_file)
                return db_creds
        except FileNotFoundError:
            print("db_creds.yaml file not found. Please ensure it is created correctly.")
            return{}
        
        
        
