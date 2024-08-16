-- Удаляем таблицы, если они существуют
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS customers;

-- Создание таблицы клиентов
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,  -- Уникальный идентификатор клиента
    name VARCHAR(100) NOT NULL,      -- Имя клиента
    age INT CHECK (age >= 18),       -- Возраст клиента
    email VARCHAR(100) UNIQUE NOT NULL, -- Электронная почта клиента
    join_date DATE NOT NULL           -- Дата присоединения клиента
);

-- Создание таблицы транзакций
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,  -- Уникальный идентификатор транзации
    customer_id INT NOT NULL,           -- Идентификатор клиента
    amount DECIMAL(10, 2) NOT NULL,     -- Сумма транзакции
    transaction_date TIMESTAMP NOT NULL, -- Дата и время транзакции
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- Внешний ключ
);
