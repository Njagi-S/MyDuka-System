from database import cur,conn
from datetime import datetime, date
def fetchSales():
    cur.execute("SELECT * FROM sales;")
    sales = cur.fetchall()
    return sales


def insertSales(pid,qn,crt):
    cur.execute("insert into sales (pid,quantity,created_at) values (%s,%s,%s)",(pid,qn,crt))
    conn.commit()

# insertSales(1,800,"2024-01-01")
# insertSales(2,950,"2024-02-01")
# insertSales(3,550,"2024-03-01")
# insertSales(4,670,"2024-11-01")
# insertSales(5,750,"2024-10-01")
# insertSales(6,880,"2024-09-01")
y = fetchSales()
print(y)

print('\n')

# looping through the sales table
# Loop through the list and unpack each tuple
for id, pid, quantity, created_at in y:
    print(f"ID: {id}, Product ID: {pid}, Quantity: {quantity}, Created_at: {created_at}")