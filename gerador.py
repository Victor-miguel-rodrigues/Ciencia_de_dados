import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações
start_date = datetime(2024, 1, 1)
days = 365

regions = ["Sudeste", "Sul", "Nordeste", "Norte", "Centro-Oeste"]
categories = {
    "Eletrônicos": ["Notebook", "Smartphone", "Fone Bluetooth", "TV 50", "Mouse Gamer"],
    "Roupas": ["Camiseta", "Calça Jeans", "Jaqueta", "Vestido", "Tênis"],
    "Casa": ["Air Fryer", "Microondas", "Liquidificador", "Cafeteira"],
    "Beleza": ["Perfume", "Kit Skincare", "Shampoo", "Maquiagem"]
}
payments = ["Cartão de Crédito", "Pix", "Boleto"]

data = []

order_id = 1000

for i in range(days):
    current_date = start_date + timedelta(days=i)
    
    # Número de pedidos por dia (simula crescimento ao longo do ano)
    num_orders = random.randint(5, 15) + int(i * 0.02)
    
    for _ in range(num_orders):
        order_id += 1
        category = random.choice(list(categories.keys()))
        product = random.choice(categories[category])
        
        price = random.randint(50, 4000)
        quantity = random.randint(1, 3)
        total = price * quantity
        
        returned = "Yes" if random.random() < 0.08 else "No"
        
        data.append([
            order_id,
            current_date.strftime("%Y-%m-%d"),
            f"C{random.randint(1, 500):03d}",
            random.choice(regions),
            category,
            product,
            price,
            quantity,
            total,
            random.choice(payments),
            random.randint(2, 10),
            returned
        ])

columns = [
    "order_id","order_date","customer_id","region",
    "product_category","product_name","price","quantity",
    "total_value","payment_method","delivery_days","returned"
]

df = pd.DataFrame(data, columns=columns)

# Salvar arquivo
df.to_csv("ecommerce_2024.csv", index=False)

print("Arquivo gerado: ecommerce_2024.csv")