from flask import Flask, render_template, request

app = Flask(__name__)

productos = {
    1: {'nombre': 'Teclado', 'precio': 20000},
    2: {'nombre': 'Mouse', 'precio': 15000},
    3: {'nombre': 'Monitor', 'precio': 800000},
    4: {'nombre': 'CPU', 'precio': 200000},
    5: {'nombre': 'Parlantes', 'precio': 50000}
}

def obtener_fecha_venta():
    from datetime import date
    hoy = date.today()
    return hoy.strftime('%d/%m/%Y')

def obtener_hora_venta():
    from datetime import datetime
    ahora = datetime.now()
    return ahora.strftime('%H:%M:%S')

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal):
    if subtotal <= 3000000:
        return subtotal * 0.08
    elif subtotal <= 5000000:
        return subtotal * 0.1
    else:
        return subtotal * 0.2

def calcular_neto(subtotal, descuento):
    return subtotal - descuento

@app.route('/')
def index():
    return render_template('formulario.html', productos=productos)

@app.route('/procesar', methods=['POST'])
def procesar():
    producto = int(request.form['producto'])
    cantidad = int(request.form['cantidad'])

    precio = productos[producto]['precio']
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    neto = calcular_neto(subtotal, descuento)

    numero_venta = '001'
    fecha_venta = obtener_fecha_venta()
    hora_venta = obtener_hora_venta()

    return render_template('resultado.html', 
        numero_venta=numero_venta, 
        fecha_venta=fecha_venta, 
        hora_venta=hora_venta,
        nombre_producto=productos[producto]['nombre'], 
        cantidad=cantidad, 
        precio=precio, 
        subtotal=subtotal, 
        descuento=descuento, 
        neto=neto)

if __name__ == '__main__':
    app.run(debug=True)
