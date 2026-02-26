def total_sales(sales):
    total = 0

    for product in sales:
        total += sales[product]
    
    return total
        
print(total_sales({'laptop' : 5, 'phone': 10, 'tablet' : 3}))

