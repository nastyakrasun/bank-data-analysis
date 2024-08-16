import pandas as pd


def analyze_customers(data):
    """Анализ данных клиентов"""
    summary = data.describe()  # Статистические сводки
    age_distribution = data["age"].value_counts()  # Распределение по возрасту
    return summary, age_distribution


def analyze_transactions(data):
    """Анализ данных транзакций"""
    total_transactions = data["amount"].sum()  # Общая сумма транзакций
    transactions_by_customer = data.groupby("customer_id")[
        "amount"
    ].sum()  # Транзакции по клиентам
    return total_transactions, transactions_by_customer
