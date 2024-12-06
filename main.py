from flask import Flask,render_template, request
from database import cur
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
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
        #print(products)
        return render_template("products.html", myproducts = products)
    else:
        name = request.form["productname"]
        buying_price = request.form["buyingprice"]
        selling_price = request.form["sellingprice"]
        stock_quantity = request.form["stockquantity"]
        print(name, buying_price, selling_price, stock_quantity)
        return "Product Added Successfully"

@app.route("/sales")
def sales():
    cur.execute("SELECT sales.id, products.name, sales.quantity, sales.created_at FROM sales JOIN products ON sales.pid = products.id;")
    sales = cur.fetchall()
    #print(sales)
    return render_template("sales.html", mysales = sales)

app.run(debug=True)