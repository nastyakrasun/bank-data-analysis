import pandas as pd
from data_loader import load_data_from_csv
from data_analysis import analyze_customers, analyze_transactions
from data_visualization import save_age_distribution_to_excel, save_transaction_totals_to_excel

def main():
    # Загрузка данных
    customers_data = load_data_from_csv('data/raw/customers.csv')
    transactions_data = load_data_from_csv('data/raw/transactions.csv')
                                           
    # Анализ данных
    customer_summary, age_distribution = analyze_customers(customers_data)
    total_transactions, transactions_by_customer = analyze_transactions(transactions_data)

    # Вывод результатов анализа
    print(customer_summary)
    print("Общая сумма транзакций:", total_transactions)

    # Сохранение результатов в Excel
    save_age_distribution_to_excel(age_distribution, file_path='output/age_distribution.xlsx')
    save_transaction_totals_to_excel(transactions_by_customer, file_path='output/transaction_totals.xlsx')
    
if __name__ == "__main__":
    main()
