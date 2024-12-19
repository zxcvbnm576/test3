import csv

total_income = {}

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        product_id = int(row['product_id'])
        quantity = int(row['quantity'])
        price = float(row['price'])
        
        income = quantity * price
        
        if product_id in total_income:
            total_income[product_id] += income
        else:
            total_income[product_id] = income

for product_id, income in total_income.items():
    print(f'Общий доход от продукта {product_id}: {income:.2f}')
