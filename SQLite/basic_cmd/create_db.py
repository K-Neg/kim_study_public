import sqlite3

# criando e conectando...
conn = sqlite3.connect('shop.db')
# desconectando...
conn.close()
