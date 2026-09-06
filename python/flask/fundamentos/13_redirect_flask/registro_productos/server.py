from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    producto = request.form["producto"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    print("Producto:", producto)
    print("Precio:", precio)
    print("Stock:", stock)

    return redirect(url_for("ver_producto"))

@app.route("/producto_guardado")
def ver_producto():
    return render_template("ver_producto.html")

if __name__ == "__main__":
    app.run(debug=True)
