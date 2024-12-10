from flask import Flask,render_template, request, redirect
from database import cur,conn
from datetime import datetime
app = Flask(__name__)
# Define a custom filter
@app.template_filter('strftime')
def format_datetime(value, format="%B %d, %Y"):
    return value.strftime(format)

@app.route("/")
def index():
    name = "John Doe"
    return render_template("index.html", myname = name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")

@app.route("/products" , methods = ["GET", "POST"])
def products():
    if request.method=="GET":
        cur.execute("SELECT * FROM products order by id desc")
        products = cur.fetchall()
        #print(products)
        return render_template("products.html", myproducts = products)
    else:
        name = request.form["productname"]
        buying_price = float(request.form["buyingprice"])
        selling_price = float(request.form["sellingprice"])
        stock_quantity = int(request.form["stockquantity"])
        #print(name, buying_price, selling_price, stock_quantity)
        if selling_price < buying_price:
            return "Selling price should be greater than buying price"            
        query="insert into products(name,buying_price,selling_price,stock_quantity) "\
        "values('{}',{},{},{})".format(name,buying_price,selling_price,stock_quantity)       
        cur.execute(query)
        conn.commit()
        return redirect("/products")

@app.route("/sales", methods=["GET", "POST"])
def sales():
    if request.method=="POST":
        pid=request.form["pid"]
        quantity=request.form["quantity"]
        query_s="insert into sales(pid,quantity,created_at) "\
        "values('{}','{}','{}')".format(pid,quantity,'now()')
        cur.execute(query_s)
        conn.commit()
        return redirect("/sales")
    else:
        cur.execute("select * from products")
        products = cur.fetchall()
        cur.execute("SELECT sales.id, products.name, sales.quantity, sales.created_at FROM sales JOIN products ON sales.pid = products.id;")
        sales = cur.fetchall()
        #print(sales)
        return render_template("sales.html", myproducts = products, mysales = sales)

@app.route("/dashboard")
def dashboard():
    cur.execute("select round(sum (products.selling_price * sales.quantity),2) as sales, DATE(sales.created_at) as sales_date from sales join products on products.id = sales.pid group by DATE(sales.created_at) order by DATE(sales.created_at) ASC; ")
    daily_sales = cur.fetchall()
    #print(daily_sales)
   
    # Extract daily sales data
    x = [i[1].strftime("%B %d, %Y") for i in daily_sales]
    y = [float(i[0]) for i in daily_sales]
    
    # print(x)
    # print("\n")
    # print(y)
    query = "SELECT products.name AS product_name, ROUND(SUM(products.selling_price * sales.quantity), 2) AS total_sales FROM sales JOIN products ON products.id = sales.pid GROUP BY products.name ORDER BY total_sales DESC;"
    cur.execute(query)
    sales_per_prod = cur.fetchall()
    
    # Extract sales per product data
    a = [i[0] for i in sales_per_prod]  # Product names
    b = [float(i[1]) for i in sales_per_prod]  # Total sales

    # Debugging
    # print("Daily Sales (x, y):", x, y)
    # print("Sales Per Product (a, b):", a, b)

    # Debugging
    print(sales_per_prod)

    return render_template("dashboard.html", x=x, y=y, a=a, b=b, sales_data = daily_sales)
    
app.run(debug=True)
