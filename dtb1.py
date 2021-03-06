import sqlite3
con = sqlite3.connect("Store.db")
cur = con.cursor()
cur.execute('''CREATE TABLE orders
                             (order_num INTEGER PRIMARY KEY,
                              order_date FLOAT,
                              customers_id INTEGER,
                              prod_id INTEGER,
                              FOREIGN KEY (customers_id) REFERENCES customers(customers_id),
                              FOREIGN KEY (prod_id) REFERENCES products(prod_id))''')

cur.execute(''' CREATE TABLE products
                              (prod_id INTEGER PRIMARY KEY,
                               vend_id INTEGER,
                               prod_name TEXT,
                               prod_price FLOAT,
                               prod_desc TEXT)''')
cur.execute(''' CREATE TABLE customers
                              (customers_id INTEGER PRIMARY KEY,
                               customers_name TEXT,
                               customers_age INTEGER,
                               customers_city TEXT)                 
                               ''')
cur.execute('INSERT INTO orders VALUES(1, 12.02, 55, 147)')
cur.execute('INSERT INTO orders VALUES(2, 13.02, 56, 148)')
cur.execute('INSERT INTO orders VALUES(3, 14.02, 57, 149)')
cur.execute('INSERT INTO products VALUES(147, 1, "Samsung", 29.99, "old comp")')
cur.execute('INSERT INTO products VALUES(148, 1, "Lenovo", 39.99, "not so old comp")')
cur.execute('INSERT INTO products VALUES(149, 1, "Asus", 129.99, "new comp")')
cur.execute('INSERT INTO customers VALUES(55, "Nicole", 33, "Kyiv")')
cur.execute('INSERT INTO customers VALUES(56, "Helen", 31, "Pacikivka")')
cur.execute('INSERT INTO customers VALUES(57, "Olga", 43, "Poltava")')

con.commit()
cur.close()
con.close()




