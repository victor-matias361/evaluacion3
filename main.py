from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def calcular_estado(n1, n2, n3, asistencia):
    promedio = (n1 + n2 + n3) / 3
    if promedio >= 40 and asistencia >= 75:
        return promedio, "APROBADO"
    return promedio, "REPROBADO"

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    error = None
    if request.method == "POST":
        n1 = float(request.form["nota1"])
        n2 = float(request.form["nota2"])
        n3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])
        if not all(10 <= n <= 70 for n in (n1, n2, n3)) or not 0 <= asistencia <= 100:
            error = "Notas entre 10 y 70, asistencia entre 0 y 100."
        else:
            promedio, estado = calcular_estado(n1, n2, n3, asistencia)
    return render_template("ejercicio1.html", promedio=promedio, estado=estado, error=error)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mayor = None
    cantidad = None
    error = None
    if request.method == "POST":
        nombres = [request.form["nombre1"].strip(),
                   request.form["nombre2"].strip(),
                   request.form["nombre3"].strip()]
        if len(set(n.lower() for n in nombres)) < 3:
            error = "Los 3 nombres deben ser diferentes."
        else:
            mayor = max(nombres, key=len)
            cantidad = len(mayor)
    return render_template("ejercicio2.html", mayor=mayor, cantidad=cantidad, error=error)

if __name__ == "__main__":
    app.run(debug=True)