import sqlite3
import pandas as pd

class SQLiteDB:
    def __init__(self, db_path):
        """
        Устанавливает соединение с БД.
        """
        if db_path:
            self.conn = sqlite3.connect(db_path)
    
    def get_tables(self):
        """
        Возвращает список  таблиц 
        """
        query = """
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' 
                AND name NOT LIKE 'sqlite_%'
        """
        #Сделать проверки, try и т.д.
        df = pd.read_sql_query(query, self.conn)
        cols = df['name'].to_list()
        return cols


    def get_table(self,table_name):
        '''Возвращает DF выбранной таблицы'''
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, self.conn)
        return df
 

    def close(self):
        """Закрывает соединение с базой данных"""
        if self.conn:
            self.conn.close()
            self.conn = None

    def __enter__(self):
        """Поддержка контекстного менеджера"""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Автоматическое закрытие соединения при выходе из контекста"""
        self.close()

    def __del__(self):
        """Закрытие соединения при удалении объекта (дополнительная защита)"""
        self.close()