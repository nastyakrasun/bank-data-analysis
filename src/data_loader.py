import pandas as pd
import psycopg2

def load_data_from_csv(file_path):
    """Загрузка данных из CSV файла"""
    data = pd.read_csv(file_path)
    return data


def load_data_from_db(cursor, query):
    """Загрузка данных из базы данных"""
    cursor.execute(query)
    return cursor.fetchall()
