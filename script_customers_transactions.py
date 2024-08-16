import pandas as pd
import random

# Создание фиктивных данных
num_customers = 100
customers = {
    'customer_id': range(1, num_customers + 1),
    'name': [f'Customer {i}' for i in range(1, num_customers + 1)],
    'age': [random.randint(18, 70) for _ in range(num_customers)],
    'email': [f'customer{i}@example.com' for i in range(1, num_customers + 1)],
    'join_date': pd.date_range(start='2015-01-01', periods=num_customers, freq='M')
}

customers_df = pd.DataFrame(customers)
customers_df.to_csv('data/raw/customers.csv', index=False)

# Создание фиктивных транзакций
num_transactions = 300
transactions = {
    'transaction_id': range(1, num_transactions + 1),
    'customer_id': [random.randint(1, num_customers) for _ in range(num_transactions)],
    'amount': [round(random.uniform(10.0, 1000.0), 2) for _ in range(num_transactions)],
    'transaction_date': pd.date_range(start='2024-01-01', periods=num_transactions, freq='D')
}

transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv('data/raw/transactions.csv', index=False)
