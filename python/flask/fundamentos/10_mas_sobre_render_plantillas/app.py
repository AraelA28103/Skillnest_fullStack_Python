from flask import Flask, render_template
import  random
app = Flask(__name__)

@app.route("/")
@app.route("/listas")
def renderizar_listas():
    listado_estudiantes = [
        {'nombre': 'Florencia', 'edad': 25},
        {'nombre': 'Valentina', 'edad': 30},
        {'nombre': 'José', 'edad': 27},
        {'nombre': 'Patricio', 'edad': 21}
    ]
    
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    num3 = random.randint(-10, 10)
    return render_template('listas.html', numeros=[num1, num2, num3], estudiantes=listado_estudiantes)

@app.route("/videojuegos")
def listado_videojuegos():
    lista_videojuegos = [
        {"nombre": "Minecraft", "plataforma": "PC / Consolas / Móviles", "publicacion": 2009},
        {"nombre": "Grand Theft Auto V", "plataforma": "PC / PlayStation / Xbox", "publicacion": 2013},
        {"nombre": "The Witcher 3: Wild Hunt", "plataforma": "PC / PlayStation / Xbox / Nintendo Switch", "publicacion": 2015},
        {"nombre": "The Legend of Zelda: Breath of the Wild", "plataforma": "Nintendo Switch / Wii U", "publicacion": 2017},
        {"nombre": "Elden Ring", "plataforma": "PC / PlayStation / Xbox", "publicacion": 2022},
        {"nombre": "Baldur's Gate 3", "plataforma": "PC / Mac / PlayStation / Xbox", "publicacion": 2023}
    ]
    return render_template("videojuegos.html", videojuegos = lista_videojuegos)

if __name__ == "__main__":
    app.run(debug=True)
