from flask import Flask, render_template, request

app = Flask(__name__)

frutas = [
    {"id": "manzana", "nombre": "Manzana", "precio": 2.5, "imagen": "manzana.png", "descripcion": ("Fruta dulce y crujiente, " "rica en fibra y vitamina C.")},
    {"id": "platano", "nombre": "Plátano", "precio": 1.8, "imagen": "platano.png", "descripcion": ("Fruta energética rica en potasio, " "perfecta para deportistas.")},
    {"id": "naranja", "nombre": "Naranja", "precio": 3.0, "imagen": "naranja.png", "descripcion": ("Cítrico jugoso con alto contenido " "de vitamina C y antioxidantes.")},
    {"id": "fresa", "nombre": "Frutilla", "precio": 4.5, "imagen": "frutilla.png", "descripcion": ("Baya dulce y aromática, rica " "en antioxidantes y vitamina C.")},
    {"id": "uva", "nombre": "Uva", "precio": 3.8, "imagen": "uva.png", "descripcion": ("Fruta pequeña y dulce, ideal " "para snacks y postres.")},
    {"id": "pina", "nombre": "Piña", "precio": 5.0, "imagen": "pina.png", "descripcion": ("Fruta tropical dulce y ácida, " "ideal para consumir fresca.")},
    {"id": "sandia", "nombre": "Sandía", "precio": 4.2, "imagen": "sandia.png", "descripcion": ("Fruta refrescante, ideal " "para los días de verano.")},
    {"id": "mango", "nombre": "Mango", "precio": 3.5, "imagen": "mango.png", "descripcion": ("Fruta tropical dulce y aromática, " "rica en vitaminas A y C.")}
]

@app.route("/")
def index():
    return render_template("index.html", frutas=frutas)

@app.route("/frutas", methods=["GET"])
def frutas_view():
    return render_template("frutas.html", frutas=frutas)

@app.route("/checkout", methods=["POST"])
def checkout():
    print(request.form)
    nombre = request.form["nombre"]
    email = request.form["email"]
    direccion = request.form["direccion"]
    pedido = []
    total = 0
    total_frutas = 0
    for fruta in frutas:
        cantidad = int(request.form[fruta["id"]])
        if cantidad > 0:
            subtotal = cantidad * fruta["precio"]
            pedido.append({
                "nombre": fruta["nombre"],
                "precio": fruta["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal,
                "imagen": fruta["imagen"]
            })
            total += subtotal
            total_frutas += cantidad
    return render_template("checkout.html",nombre=nombre, email=email, direccion=direccion, pedido=pedido, total=total, total_frutas=total_frutas)

if __name__ == "__main__":
    app.run(debug=True)
