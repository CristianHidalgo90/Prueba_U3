from errno import EILSEQ

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        n1=int(request.form['n1'])
        n2=int(request.form['n2'])
        n3=int(request.form['n3'])
        asistencia=int(request.form['asistencia'])
        promedio=(n1+n2+n3)/3
        if promedio>=40 and asistencia>=75:
            situacion="APROBADO"
        else:
            situacion="REPROBADO"
        return render_template('ejercicio1.html',n1=n1,n2=n2,n3=n3,asistencia=asistencia,promedio=promedio,situacion=situacion)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1=request.form['nombre1']
        nombre2=request.form['nombre2']
        nombre3=request.form['nombre3']

        if len(nombre1)>=len(nombre2) and len(nombre1)>=len(nombre3):
            nombre_mayor=nombre1
        elif len(nombre2)>=len(nombre1) and len(nombre2)>=len(nombre3):
            nombre_mayor=nombre2
        else:
            nombre_mayor=nombre3
        cant_letras=len(nombre_mayor)
        return render_template('ejercicio2.html',nombre1=nombre1,nombre2=nombre2,nombre3=nombre3,nombre_mayor=nombre_mayor,cant_letras=cant_letras)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)