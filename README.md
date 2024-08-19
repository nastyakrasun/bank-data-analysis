# bank-data-analysis
Проект направлен на анализ клиентских данных банка с использованием SQL для обработки данных, Python для анализа и Excel для визуализации.

Проект включает в себя:

- загрузку и обработку данных клиентов и их транзакций;
- использование SQL для создания и манипуляции таблицами;
- анализ данных с помощью Python-библиотеки Pandas;
- визуализацию результатов анализа с использованием Excel.

Структура проекта

- project_root (Корень проекта):
-- src  (Исходный код проекта):
--- data_loader.py (Код для загрузки данных из CSV и базы данных):
--- data_visualization.py (Код для визуализации данных в Excel):
--- main.py (Основной файл, запускающий анализ)
-- data (Папка для данных):
--- raw (Исходные CSV файлы):
--- customers.csv (Данные о клиентах):
--- processed (Обработанные или промежуточные данные (если потребуется))
-- output (Папка для выходных файлов):
--- age_distribution.xlsx (Выходной файл с распределением возраста):
--- transaction_totals.xlsx (Выходной файл с общими транзакциями)
-- requirements.txt (Список зависимостей)
-- README.md (Описание проекта и инструкции по его использованию)

Описание файлов и модулей

1. src/data_loader.py:
   отвечает за загрузку данных из различных источников, включая CSV файлы и базы данных:
   - `load_data_from_csv`: загружает данные из указанного CSV файла с использованием библиотеки Pandas.
   - `load_data_from_db`: используется для извлечения данных из базы данных по указанному SQL запросу.

2. src/data_analysis.py:
   здесь расположен код для анализа загруженных данных.
   - `analyze_customers`: анализирует данные о клиентах, предоставляет статистические сводки и распределение по возрасту.
   - `analyze_transactions`: анализирует транзакции, рассчитывает общую сумму транзакций и суммы транзакций по каждому клиенту.

3. src/data_visualization.py:
   занимается сохранением результатов анализа в формате Excel.
   - `save_age_distribution_to_excel`: сохраняет распределение возраста клиентов в Excel файл.
   - `save_transaction_totals_to_excel`: сохраняет общие суммы транзакций по каждому клиенту в Excel файл.

4. src/main.py:
   основной файл, который запускает весь процесс: загружает данные о клиентах и транзакциях, вызывает функции анализа и сохраняет результаты в Excel файлы.

Установка

1. Клонирование репозитория:
git clone https://github.com/ваш_пользователь/bank-data-analysis.git

2. Переход в папку проекта:
cd bank-data-analysis

3. Установка зависимостей:
pip install -r requirements.txt

1. Запуск SQL-скриптов из папки `sql/` для создания таблиц и загрузки данных в базу данных.
2. Запуск Python-скрипа `src/analyze_bank_data.py`, чтобы провести анализ и получить результаты в формате, подходящем для Excel.
3. Открытие Jupyter Notebook в папке `notebooks/` для документирования процесса анализа и получения визуализаций в интерактивном формате.

Примеры
Вывод анализа и визуализация в Excel демонстрирует результаты работы проекта.

Заключение
Проект является примером работы с клиентскими данными банка, позволяя использовать SQL для обработки данных, Python для их анализа и Excel для визуализации.
Проект следует расшять добавлением функций анализа по возрастным группам, визуализации по времени транзакций, использования Matplotlib для более подробной автоматизации процесса анализа данных, чем Excel.
