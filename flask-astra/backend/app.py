import os
import uuid
from datetime import datetime, timezone

from flask import Flask, flash, redirect, render_template, request, url_for

import db

FRONTEND_DIR = db.BASE_DIR / "frontend"

app = Flask(
    __name__,
    template_folder=str(FRONTEND_DIR / "templates"),
    static_folder=str(FRONTEND_DIR / "static"),
)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-cambiar")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre", "").strip()

    if not nombre:
        flash("Escribe un nombre.", "error")
        return redirect(url_for("index"))
    if len(nombre) > 100:
        flash("El nombre es demasiado largo (máximo 100 caracteres).", "error")
        return redirect(url_for("index"))

    try:
        db.get_table().insert_one(
            {
                "id": uuid.uuid4(),
                "nombre": nombre,
                "creado": datetime.now(timezone.utc),
            }
        )
    except Exception as e:
        flash(f"No se pudo guardar en Astra DB: {e}", "error")
        return redirect(url_for("index"))

    flash(f"¡Listo! Se registró «{nombre}».", "ok")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
