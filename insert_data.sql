-- Вставка данных из файла customers.csv

\COPY customers (name, age, email, join_date) 
FROM 'data/raw/customers.csv' 
DELIMITER ',' 
CSV HEADER;

-- Вставка данных из файла transactions.csv

\COPY transactions (customer_id, amount, transaction_date) 
FROM 'data/raw/transactions.csv' 
DELIMITER ',' 
CSV HEADER;
