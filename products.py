from database import cur,conn

def fetchProducts():
    cur.execute("SELECT * FROM products;")
    products = cur.fetchall()
    return products

def insertProduct(name,bp,sp,st):
    cur.execute("insert into products (name,buying_price, selling_price, stock_quantity) values (%s,%s,%s,%s)",(name,bp,sp,st))
    conn.commit()

# insertProduct("Tecno Spark 9",11899,19999,1740)
# insertProduct("Tecno Spark 10",12899,20999,1457)
# insertProduct("Tecno Spark 20",13999,21999,1570)
# insertProduct("Tecno Spark 30",18999,27999,1470)
# insertProduct("Infinix Hot 40",23899,31999,957)
# insertProduct("Infinix Hot 50",33899,41999,4570)

# Taking into consideration users input:
# new_value=(input("Please Enter Product Name: " ))
# buy_p = float(input("Please Enter Buying Price: " ))
# sell_p = float(input("Please Enter Selling Price: " ))
# stoc_am = float(input("Please Enter The Stock Quantity: "))

# insertProduct(new_value,buy_p,sell_p,stoc_am)


x = fetchProducts()

print(x)

print('\n')

# looping through the products table
# Loop through the list and unpack each tuple
for id, name, buying_price, selling_price, stock_quantity in x:
    print(f"ID: {id}, Name: {name}, Buying Price: {buying_price}, Selling Price: {selling_price}, Stock: {stock_quantity}")

print('\n')
# # Function to fetch profit per product
# def fetchProfitPerProduct():
#     cur.execute("SELECT sum((products.selling_price - products.buying_price)*sales.quantity) FROM products inner join sales on sales.pid=products.id group by products.name;")
#     profits = cur.fetchall()
#     print(profits)
#     return profits

# # Fetch and print profit per product
# fetchProfitPerProduct()