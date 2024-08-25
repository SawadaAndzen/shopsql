import sqlite3

base = sqlite3.connect("shopsql/db.db")
cur = base.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            );
            ''')

cur.execute('''
            CREATE TABLE IF NOT EXISTS customers ( 
                customer_id INTEGER PRIMARY KEY, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL, 
                email TEXT NOT NULL UNIQUE 
            );
            ''')

cur.execute('''
            CREATE TABLE IF NOT EXISTS orders ( 
                order_id INTEGER PRIMARY KEY, 
                customer_id INTEGER NOT NULL, 
                product_id INTEGER NOT NULL, 
                quantity INTEGER NOT NULL, 
                order_date DATE NOT NULL, 
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
                FOREIGN KEY (product_id) REFERENCES products(product_id) 
            );
            ''')

cur.executemany('''
            INSERT INTO customers (customer_id, first_name, last_name, email) VALUES (?, ?, ?, ?)
            ''', 
            [
                (1, 'Vergil', 'Sparda', 'motivated@gmail.com'),
                (2, 'Paul', 'Stones', 'stone@gmail.com'),
                (3, 'Anna', 'Johnson', 'jbl12@gmail.com'),
                (4, 'Cris', 'Phillips', 'pppl@gmail.com'),
                (5, 'Phil', 'Phillips', 'pl@gmail.com')
            ]
                )

cur.executemany('''
            INSERT INTO products (product_id, name, category, price) VALUES (?, ?, ?, ?)
            ''', 
            [
                (101, 'Lenovo', 'Laptops', 24500.00),
                (102, 'Redmi Note 9', 'Phones', 6700.00),
                (103, 'JBL', 'Headphones', 150.00),
                (104, 'Phillips', 'Fridges', 8000.00),
                (105, 'Galaxy S1', 'Tablets', 9000.00)
            ]
                )

cur.executemany('''
            INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?, ?)
            ''', 
            [
                (301, 1, 103, 1, '27.01.2024'),
                (302, 2, 101, 2, '27.02.2024'),
                (303, 3, 102, 4, '17.01.2024'),
                (304, 4, 105, 5, '31.06.2024'),
                (305, 5, 104, 3, '21.01.2024')
            ]
                )

base.commit()