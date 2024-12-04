from flask import Flask,render_template
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

@app.route("/products")
def products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    #print(products)
    return render_template("products.html", myproducts = products)

@app.route("/sales")
def sales():
    cur.execute("SELECT sales.id, products.name, sales.quantity, sales.created_at FROM sales JOIN products ON sales.pid = products.id;")
    sales = cur.fetchall()
    #print(sales)
    return render_template("sales.html", mysales = sales)

app.run(debug=True)