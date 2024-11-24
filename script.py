import sqlite3

# Connexion à la base de données
connection = sqlite3.connect("e-commerce.db")
cursor = connection.cursor()

# Création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS CLIENT (
    ID_CLIENT INT PRIMARY KEY,
    NOM TEXT,
    PRENOM TEXT,
    TELEPHONE TEXT,
    EMAIL TEXT,
    DATE_NAISSANCE DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ADRESS (
    ID_ADRESS INT PRIMARY KEY,
    ID_CLIENT INT,
    ADRESSE TEXT,
    VILLE TEXT,
    CODE_POSTAL TEXT,
    PAYS TEXT,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCT (
    ID_PRODUCT INT PRIMARY KEY,
    NOM TEXT,
    DESCRIPTION TEXT,
    PRIX REAL,
    STOCK INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CART (
    ID_CART INT PRIMARY KEY,
    ID_CLIENT INT,
    DATE_ACHAT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS COMMANDE (
    ID_COMMANDE INT PRIMARY KEY,
    ID_CLIENT INT,
    DATE_COMMANDE DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS commerce_product (
    ID_CART INT,
    ID_PRODUCT INT,
    ID_INVOICE INT,
    ID_COMMANDE INT,
    QUANTITY INT,
    FOREIGN KEY (ID_CART) REFERENCES CART(ID_CART),
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE),
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS INVOICE (
    ID_INVOICE INT PRIMARY KEY,
    ID_COMMANDE INT,
    DATE_FACTURE DATE,
    FOREIGN KEY (ID_COMMANDE) REFERENCES COMMANDE(ID_COMMANDE)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PHOTO (
    ID_PHOTO INT PRIMARY KEY,
    ID_CLIENT INT,
    ID_PRODUCT INT,
    URL TEXT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PAIMENT (
    ID_PAIMENT INT PRIMARY KEY,
    ID_CLIENT INT,
    ID_INVOICE INT,
    DATE_PAIMENT DATE,
    FOREIGN KEY (ID_CLIENT) REFERENCES CLIENT(ID_CLIENT),
    FOREIGN KEY (ID_INVOICE) REFERENCES INVOICE(ID_INVOICE)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS MODE_PAIMENT (
    ID_MODE_PAIMENT INT PRIMARY KEY,
    NOM TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS RATE (
    ID_RATE INT PRIMARY KEY,
    ID_PRODUCT INT,
    RATE INT,
    ID_CLIENT INT,
    MODE_PAIMENT INT,
    FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCT(ID_PRODUCT)
)
""")

# Insertion des données dans toutes les tables
clients = [
    (1, 'Doe', 'John', '0612345678', 'john.doe@example.com', '1980-01-01'),
    (2, 'Jake', 'Jane', '0623456789', 'jane.doe@example.com', '1985-05-12'),
    (3, 'Brown', 'Alice', '0634567890', 'alice.brown@example.com', '1990-08-22'),
    (4, 'Johnson', 'Bob', '0645678901', 'bob.johnson@example.com', '1978-09-14'),
    (5, 'Smith', 'Eve', '0656789012', 'eve.smith@example.com', '1995-11-30'),
]

adresses = [
    (1, 1, '1 rue de la paix', 'Paris', '75000', 'France'),
    (2, 2, '2 rue de la paix', 'Paris', '75000', 'France'),
    (3, 3, '3 rue de la paix', 'Paris', '75000', 'France'),
    (4, 4, '4 rue de la paix', 'Paris', '75000', 'France'),
    (5, 5, '5 rue de la paix', 'Paris', '75000', 'France'),
]

products = [
    (1, 'Iphone 12', 'Smartphone', 1000.0, 10),
    (2, 'Samsung S21', 'Smartphone', 900.0, 10),
    (3, 'Huawei P40', 'Smartphone', 800.0, 10),
    (4, 'Xiaomi Mi 11', 'Smartphone', 700.0, 10),
    (5, 'OnePlus 54', 'Smartphone', 600.0, 10),
]

carts = [
    (1, 1, '2021-04-01'),
    (2, 2, '2023-12-02'),
    (3, 3, '2024-01-04'),
    (4, 4, '2024-06-06'),
    (5, 5, '2025-11-05'),
]

commandes = [
    (1, 1, '2021-04-01'),
    (2, 2, '2023-12-02'),
    (3, 3, '2024-01-04'),
    (4, 4, '2024-06-06'),
    (5, 5, '2025-11-05'),
]

invoices = [
    (1, 1, '2021-04-01'),
    (2, 2, '2023-12-02'),
    (3, 3, '2024-01-04'),
    (4, 4, '2024-06-06'),
    (5, 5, '2025-11-05'),
]

photos = [
    (1, 1, 3, 'https://img.pccomponentes.com/articles/28/281356/huawei-p40-5g-8-128gb-negro-libre-comprar.jpg'),
    (2, 2, 5, 'https://www.01net.com/app/uploads/2022/06/OnePlus-10-Pro.jpg'),
    (3, 3, 1, 'https://m.media-amazon.com/images/I/71ZOtNdaZCL.jpg'),
    (4, 4, 2, 'https://www.largo.fr/6815-large_default/galaxy-s21-5g-double-sim-128go-gris-fantome-reconditionne.jpg'),
    (5, 5, 4, 'https://boulanger.scene7.com/is/image/Boulanger/6934177734083_h_f_l_0?wid=500&hei=500'),
]

rates = [
    (1, 3, 5, 1, 1),
    (2, 5, 4, 2, 1),
    (3, 1, 3, 3, 2),
    (4, 2, 2, 4, 1),
    (5, 4, 1, 5, 2),
]

commerce_products = [
    (1, 3, 1, 1, 4),
    (2, 1, 2, 2, 5),
    (3, 4, 3, 3, 1),
    (4, 5, 4, 4, 2),
    (5, 2, 5, 5, 3),
]

mode_paiment = [
    (1, 'Carte bancaire'),
    (2, 'Espece'),
]

paiments = [
    (1, 1, 1, '2021-04-01'),
    (2, 2, 2, '2023-12-02'),
    (3, 3, 3, '2024-01-04'),
    (4, 4, 4, '2024-06-06'),
    (5, 5, 5, '2025-11-05'),
]

# Exécuter les insertions
cursor.executemany("""
INSERT INTO CLIENT VALUES (?, ?, ?, ?, ?, ?)
""", clients)

cursor.executemany("""
INSERT INTO ADRESS VALUES (?, ?, ?, ?, ?, ?)
""", adresses)

cursor.executemany("""
INSERT INTO PRODUCT VALUES (?, ?, ?, ?, ?)
""", products)

cursor.executemany("""
INSERT INTO CART VALUES (?, ?, ?)
""", carts)

cursor.executemany("""
INSERT INTO COMMANDE VALUES (?, ?, ?)
""", commandes)

cursor.executemany("""
INSERT INTO INVOICE VALUES (?, ?, ?)
""", invoices)

cursor.executemany("""
INSERT INTO PHOTO VALUES (?, ?, ?, ?)
""", photos)

cursor.executemany("""
INSERT INTO RATE VALUES (?, ?, ?, ?, ?)
""", rates)

cursor.executemany("""
INSERT INTO commerce_product VALUES (?, ?, ?, ?, ?)
""", commerce_products)

cursor.executemany("""
INSERT INTO MODE_PAIMENT VALUES (?, ?)
""", mode_paiment)

cursor.executemany("""
INSERT INTO PAIMENT VALUES (?, ?, ?, ?)
""", paiments)

# Valider les changements et fermer la connexion
connection.commit()
connection.close()
