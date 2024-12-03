from flask import Flask,render_template
from database import cur

app = Flask(__name__)
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
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    return render_template("sales.html", mysales = sales)

app.run()