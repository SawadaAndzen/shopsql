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

print(
    cur.execute('''
                SELECT 
                    SUM(products.price * orders.quantity)
                FROM
                    orders JOIN products ON orders.product_id = products.product_id
                ''').fetchone()
)

base.commit()
base.close()