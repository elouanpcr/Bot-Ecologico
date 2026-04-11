from flask import Flask, render_template, request

app = Flask(__name__)

WASTE_DATA = {
    "Vidrio": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Sepáralo por color y enjuagar."
    },
    "Botella plastica": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Enjuágala antes de reciclarla."
    },
    "Papel": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Mantenlo seco y limpio."
    },
    "Carton": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Aplana las cajas antes de reciclar."
    },
    "Latas": {
        "category": "Reciclable",
        "action": "Reciclar",
        "tips": "Enjuaga y aplasta las latas."
    },
    "Bateria": {
        "category": "Peligroso",
        "action": "Desecho especial",
        "tips": "Llévala a un punto de desechos peligrosos."
    },
    "Residuos electronicos": {
        "category": "Peligroso",
        "action": "Desecho especial",
        "tips": "Llévala a un punto de desechos peligrosos."
    }
}

# 🔥 FUNCION PARA HACERLO MÁS INTELIGENTE
def normalizar_item(item):
    item = item.lower().strip()

    alias = {
        "plástico": "botella plastica",
        "plastico": "botella plastica",
        "botella": "botella plastica",
        "cartón": "carton",
        "metal": "latas",
        "lata": "latas",
        "batería": "bateria",
        "electronicos": "residuos electronicos",
        "electronico": "residuos electronicos",
        "papel":"Papel" 
    }

    return alias.get(item, item)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None

    if request.method == "POST":
        item = request.form.get("item")

        if not item:
            error = "❌ Ingresa un residuo"
        else:
            item = normalizar_item(item)

            if item in WASTE_DATA:
                resultado = WASTE_DATA[item].copy()
                resultado["nombre"] = item
            else:
                error = "❌ No reconocido. Prueba: vidrio, papel, bateria..."

    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(debug=True)
