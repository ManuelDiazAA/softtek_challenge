"""This class prepare a sql db"""
import sqlite3

conn = sqlite3.connect("main.db")

conn.execute(
    """
    CREATE TABLE customer_ord_lines(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_number CHAR(10) NOT NULL,
        item_name CHAR(15) NOT NULL,
        status CHAR (10) NOT NULL
    );
    """
)
conn.execute(
    """
    INSERT INTO customer_ord_lines('order_number', 'item_name', 'status')
    VALUES
    ('ORD_1567','LAPTOP','SHIPPED'),
    ('ORD_1567','MOUSE','SHIPPED'),
    ('ORD_1567','KEYBOARD','PENDING'),
    ('ORD_1234','GAME','SHIPPED'),
    ('ORD_1234','BOOK','CANCELLED'),
    ('ORD_1234','BOOK','CANCELLED'),
    ('ORD_9834','SHIRT','SHIPPED'),
    ('ORD_9834','PANTS','CANCELLED'),
    ('ORD_7654','TV','CANCELLED'),
    ('ORD_7654','DVD','CANCELLED');
    """
)
conn.commit()
conn.execute(
    """
    CREATE TABLE customer_orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ord_id CHAR(20) NOT NULL,
        ord_dt CHAR(15) NOT NULL,
        qt_ordd INT NOT NULL
    );
    """
)
conn.execute(
    """
    INSERT INTO customer_orders('ord_id', 'ord_dt', 'qt_ordd')
    VALUES
    ('113-8909896-6940269','9/23/19',1),
    ('114-0291773-7262677','1/1/20',1),
    ('114-0291773-7262697','12/5/19',1),
    ('114-9900513-7761000','9/24/20',1),
    ('112-5230502-8173028','1/30/20',1),
    ('112-7714081-3300254','5/2/20',1),
    ('114-5384551-1465853','4/2/20',1),
    ('114-7232801-4607440','10/9/20',1);
    """
)
conn.commit()
conn.execute(
    """
    CREATE TABLE weather(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date CHAR(15) NOT NULL,
        was_rainy CHAR(5) NOT NULL
    );
    """
)
conn.execute(
    """
    INSERT INTO weather('date', 'was_rainy')
    VALUES
    ('1/1/20','FALSE'),
    ('1/2/20','TRUE'),
    ('1/3/20','TRUE'),
    ('1/4/20','FALSE'),
    ('1/5/20','FALSE'),
    ('1/6/20','TRUE'),
    ('1/7/20','FALSE'),
    ('1/8/20','TRUE'),
    ('1/9/20','TRUE'),
    ('1/10/20','TRUE');
    """
)
conn.commit()
print("DB created ok!")

conn.close()
