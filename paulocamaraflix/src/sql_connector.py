from sqlalchemy import create_engine, text
from sqlalchemy.types import Integer
import mypysql
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
class sql_connector():
    
    def __init__(self, username, password, server, port):
        
        self._username = username
        self._password = password
        self._server = str(server)
        self._port = str(port)
        self._engine = create_engine(f'mysql+pymysql://{self._username}:{self._password}@{self._server}:{self._port}')
        self._database = 'tp'
    
    def grantAcess(self):
        """
        
        """
    def createDataBase(self, table_name, schema_json):
        """
        Create a database into the MySQL Server

        Args:
            table_name: Name of the table
            schema_json: A JSON containing the {column_name:data_type}
        
        Authors:
            @marcuscardona
        
        Since:
            02-2023
        """

        # Create List to Save Schema
        var_to_create = []
        for var, var_type in schema_json.items():
            var_to_create.append(var+' '+var_type) 
        # Transform list to tuple
        
        
        with self._engine.connect() as conn:
           conn.execute(text(f"CREATE TABLE {self._database}.{table_name} ({','.join(var_to_create)})"))
           conn.commit()

    def insertInto(self, table_name, json):
        """
        Insert Data into the Table of the specified DB
        
        Args:
            table_name: Name of the table
            schema_json: A JSON containing the {column_name:data_type}
        
        Authors:
            @marcuscardona
        
        Since:
            02-2023
        """
        columns_list = []
        values_list = []
        for columns, values in json.items():
            columns_list.append(columns)
            values_list.append(values)
        with self._engine.connect() as conn:
        #    df.to_sql(name=table_name
        #            , con=conn 
        #            , if_exists='append'
        #            , index = False)
            conn.execute(text(f'INSERT INTO {table_name} ({','.join(columns_list)}) VALUES ({','.join(values_list)})'))
            conn.commit()

    def showDatabases(self):
        with self._engine.connect() as conn:
            result = conn.execute(text('SHOW DATABASES'))
            print(result.all())

sql = sql_connector(username=os.getenv('SQL_USER')
                  , password=os.getenv('SQL_PASSWORD')
                  , server=os.getenv('SQL_SERVER')
                  , port=os.getenv('SQL_PORT'))

df = {'x': 1, 'y':3}
sql.insertInto('tp.teste_python', df)