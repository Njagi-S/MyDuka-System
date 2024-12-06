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

@app.route("/sales")
def sales():
    cur.execute("SELECT sales.id, products.name, sales.quantity, sales.created_at FROM sales JOIN products ON sales.pid = products.id;")
    sales = cur.fetchall()
    #print(sales)
    return render_template("sales.html", mysales = sales)

app.run(debug=True)