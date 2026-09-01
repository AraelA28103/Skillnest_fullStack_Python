from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def renderizar_listas():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        contrasena = request.form.get("contrasena")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)