import pandas as pd

def save_age_distribution_to_excel(age_distribution, file_path='age_distribution.xlsx'):
    """Сохранение распределения возраста клиентов в Excel файл."""
    age_distribution_df = age_distribution.reset_index()
    age_distribution_df.columns = ['Age', 'Customer Count']
    age_distribution_df.to_excel(file_path, index=False, sheet_name='Age Distribution')

def save_transaction_totals_to_excel(transactions_by_customer, file_path='transaction_totals.xlsx'):
    """Сохранение общих транзакций по клиентам в Excel файл."""
    transactions_df = transactions_by_customer.reset_index()
    transactions_df.columns = ['Customer ID', 'Total Transactions']
    transactions_df.to_excel(file_path, index=False, sheet_name='Transaction Totals')
