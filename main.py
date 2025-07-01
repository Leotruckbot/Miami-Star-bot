from flask import Flask, render_template, request

app = Flask(__name__)

# Catálogo de ejemplo (puedes ampliarlo luego)
catalogo = {
    "M85000": {
        "nombre": "Amortiguador",
        "link": "https://www.monroe.com/en-us/products/m85000.html"
    },
    "A1234": {
        "nombre": "Rodamiento Delco",
        "link": "https://www.delco.com/parts/A1234"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    if request.method == "POST":
        numero_parte = request.form.get("parte").strip().upper()
        resultado = catalogo.get(numero_parte)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
