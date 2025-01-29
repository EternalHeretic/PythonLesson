import sqlite3

def initiate_db():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            image_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, price, image_url FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

def add_test_data():
    conn = sqlite3.connect('telegram_bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        products = [
            ("Биостимул", "Комплекс витаминов", 100,
             "https://naturalsupp.ru/upload/iblock/a47/10eq49g67pnwzx2mxj1nrr9ordk7uz71.jpg"),
            ("Экстракт Чаги", "Источник полифенолов", 200,
             "https://www.ametis.ru/files/ametis/styles/product_full/public/images/product/15/chaga.jpg?itok=ujkP-1Ly"),
            ("Ундевит", "Вкусная витаминка", 300,
             "https://cdn.eapteka.ru/upload/offer_photo/518/171/1_5e84a5d7529c372f28ff5aea128c7322.png?t=1688566933&_cvc=1737038322"),
            ("Bud", "Запрещенно вкусная витаминка", 400,
             "https://main-cdn.sbermegamarket.ru/big1/hlr-system/113/437/400/082/123/9/100027324179b0.jpg")
        ]
        cursor.executemany('INSERT INTO products (title, description, price, image_url) VALUES (?, ?, ?, ?)', products)
        conn.commit()
    conn.close()