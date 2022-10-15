from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)
mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="mysql123",
    database="tintoreria",
    auth_plugin="mysql_native_password"
    )
cursor = mydb.cursor(dictionary=True)
@app.route('/')
def inicio():
    return render_template ('index.html', mensaje="Hola bienvenidos a la pagina oficial de titoreria  url='/iniciopagina' para interacturar con ella")

@app.route('/datos')
def datos():
    cursor.execute('select * from cliente')
    usuarios = cursor.fetchall()
    print(usuarios)
    return render_template('datos.html', usuarios=usuarios)

@app.route('/datos2')
def datos2():
    cursor.execute('select * from producto')
    productos = cursor.fetchall()
    print(productos)
    return render_template('datos2.html', productos=productos)

@app.route('/datos3')
def datos3():
    cursor.execute('select * from servicios')
    servicio  = cursor.fetchall()
    print(servicio)
    return render_template('datos3.html', servicio=servicio)

@app.route('/datos4')
def datos4():
    cursor.execute('select * from empleado')
    empleados  = cursor.fetchall()
    print(empleados)
    return render_template('datos4.html', empleados=empleados)

@app.route('/datos5')
def datos5():
    cursor.execute('select * from provedores')
    provedores  = cursor.fetchall()
    print(provedores)
    return render_template('datos5.html', provedores=provedores)

@app.route('/datos6')
def datos6():
    cursor.execute('select * from maquinaria')
    maqui  = cursor.fetchall()
    print(maqui)
    return render_template('datos6.html', maqui=maqui)

@app.route('/datos7')
def datos7():
    cursor.execute('select * from suministros')
    sumin  = cursor.fetchall()
    print(sumin)
    return render_template('datos7.html', sumin=sumin)

@app.route('/datos8')
def datos8():
    cursor.execute('select * from materiales')
    mate  = cursor.fetchall()
    print(mate)
    return render_template('datos8.html', mate=mate)

@app.route('/datos9')
def datos9():
    cursor.execute('select * from nota')
    nota  = cursor.fetchall()
    print(nota)
    return render_template('datos9.html', nota=nota)

@app.route('/datos10')
def datos10():
    cursor.execute('select * from inventario')
    inven  = cursor.fetchall()
    print(inven)
    return render_template('datos10.html', inven=inven)

@app.route('/borrar', methods=['GET', 'POST'])
def borrar():
    if request.method=="POST":
        folio = request.form['folio']
        cursor.execute("delete from nota where folio=%s", (folio,))
        mydb.commit()
        return redirect(url_for('datos9'))
    return render_template('borrar.html')

@app.route('/borrarcliente', methods=['GET', 'POST'])
def borrarcliente():
    if request.method=="POST":
        clave_cli = request.form['clave_cli']
        cursor.execute("delete from cliente where clave_cli=%s", (clave_cli,))
        mydb.commit()
        return redirect(url_for('datos'))
    return render_template('borrar1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method=="POST":
        nombre  = request.form['nombre']
        password = request.form['password']
        cursor.execute('select  clave_cli, password from cliente where nombre=%s and  password=%s',(nombre,password))
        user = cursor.fetchone()
        if user is None:
            error="Nombre de usuario y/o contraseña incorrectos"
            print(error)
        if error is None:
            return render_template('inicio2.html')
    return render_template('login.html', error=error)


@app.route('/usuario', methods=['GET', 'POST'])
def nuevo_empleado():
    error = None
    if request.method=="POST":
        clave_cli = request.form['clave_cli']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        correo = request.form['correo']
        telefono = request.form['telefono']
        password = request.form['password']
        sql=" insert into cliente (clave_cli, nombre, apellido, direccion, correo, telefono,  password )values (%s, %s, %s, %s, %s, %s, %s )"
        values= (clave_cli, nombre, apellido, direccion, correo, telefono,  password)
        cursor.execute(sql, values)
        mydb.commit()
        user = cursor.fetchone()
        if user is None:
            error="Nombre de usuario y/o contraseña incorrectos"
            print(error)
        if error is None:
            return redirect(url_for('registrar'))
    return render_template('usuario.html') 

@app.route('/loginemple', methods=['GET', 'POST'])
def loginemple():
    error = None
    if request.method=="POST":
        nombre  = request.form['nombre']
        password = request.form['password']
        cursor.execute('select  nombre, password from empleado where nombre=%s and  password=%s',(nombre,password))
        user = cursor.fetchone()
        if user is None:
            error="Nombre de usuario y/o contraseña incorrectos"
            print(error)
        if error is None:
            return render_template('menuempleado.html')
    return render_template('login2.html', error=error)

@app.route('/empleado', methods=['GET', 'POST'])
def nuevoempleado():
    error = None
    if request.method=="POST":
        id_emple = request.form['id_emple']
        nombre = request.form['nombre']
        numero = request.form['numero']
        edad = request.form['edad']
        puesto = request.form['puesto']
        curp = request.form['curp']
        password = request.form['password']
        sql=" insert into empleado (id_emple, nombre, numero,edad, puesto, curp,  password )values (%s, %s, %s, %s, %s, %s, %s )"
        values= (id_emple, nombre,curp, numero, edad, puesto,  password)
        cursor.execute(sql, values)
        mydb.commit()
        user = cursor.fetchone()
        if user is None:
            error="Nombre de usuario y/o contraseña incorrectos"
            print(error)
        if error is None:
            return redirect(url_for('inicio3'))
    return render_template('empleado.html') 

@app.route('/quienessomos')
def quienessomos():
    return render_template ('quienesomos.html')

@app.route('/productososervicios')
def productososervicios():
    return render_template ('productososervicios.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template ('ubicacion.html')

@app.route('/curriculum')
def curriculum():
    return render_template ('curriculum.html')

@app.route('/producto', methods=['GET', 'POST'])
def producto():
    if request.method=="POST":
        id_produ = request.form['id_produ']
        marca = request.form['marca']
        prenda = request.form['prenda']
        material = request.form['material']
        color = request.form['color']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        kilo = request.form['kilo']
        sql=" insert into producto (id_produ,marca, prenda,material, color, precio, cantidad,kilo)values (%s,%s, %s, %s, %s, %s,%s,%s)"
        values= (id_produ, marca, prenda,material,color,precio,cantidad,kilo)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos2'))
    return render_template('producto.html')

@app.route('/servicios', methods=['GET', 'POST'])
def servicios():
    if request.method=="POST":
        clave_ser = request.form['clave_ser']
        nombre_servicio = request.form['nombre_servicio']
        precio = request.form['precio']
        sql=" insert into servicios  (clave_ser,nombre_servicio,precio)values (%s,%s,%s)"
        values= (clave_ser, nombre_servicio,precio)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos3'))
    return render_template('servicios.html')


@app.route('/provedores', methods=['GET', 'POST'])
def provedores():
    if request.method=="POST":
        id_prove = request.form['id_prove']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        sql=" insert into provedores (id_prove,nombre,telefono,direccion)values (%s,%s,%s,%s)"
        values= (id_prove,nombre,telefono,direccion)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos5'))
    return render_template('provedores.html')

@app.route('/maquinaria', methods=['GET', 'POST'])
def maquinaria():
    if request.method=="POST":
        id_maquinaria = request.form['id_maquinaria']
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        peso = request.form['peso']
        tamaño = request.form['tamaño']
        sql=" insert into maquinaria  (id_maquinaria,nombre,modelo,peso,tamaño)values (%s,%s,%s,%s,%s)"
        values= (id_maquinaria,nombre,modelo,peso,tamaño)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos6'))
    return render_template('maquinaria.html')

@app.route('/suministros', methods=['GET', 'POST'])
def suministros():
    if request.method=="POST":
        id_sumin = request.form['id_sumin']
        nombre = request.form['nombre']
        precio = request.form['precio']
        sql=" insert into suministros (id_sumin,nombre,precio)values (%s,%s,%s)"
        values= (id_sumin,nombre,precio)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos7'))
    return render_template('suministros.html')

@app.route('/materiales', methods=['GET', 'POST'])
def materiales():
    if request.method=="POST":
        id_mate = request.form['id_mate']
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        sql=" insert into materiales  (id_mate,nombre,cantidad,precio)values (%s,%s,%s,%s)"
        values= (id_mate,nombre,cantidad,precio)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos8'))
    return render_template('materiales.html')

@app.route('/nota', methods=['GET', 'POST'])
def nota():
    if request.method=="POST":
        folio = request.form['folio']
        fecha = request.form['fecha']
        precio_total = request.form['precio_total']
        fecha_entrega = request.form['fecha_entrega']
        sql=" insert into nota  (folio,fecha,precio_total,fecha_entrega)values (%s,%s,%s,%s)"
        values= (folio,fecha,precio_total,fecha_entrega)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos9'))
    return render_template('nota.html')


@app.route('/inventario', methods=['GET', 'POST'])
def inventario():
    if request.method=="POST":
        clave_inv = request.form['clave_inv']
        id_maquinaria = request.form['id_maquinaria']
        id_prove = request.form['id_prove']
        id_sumin = request.form['id_sumin']
        id_mate = request.form['id_mate']
        sql=" insert into inventario (clave_inv,id_maquinaria,id_prove,id_sumin,id_mate)values (%s,%s,%s,%s,%s)"
        values= (clave_inv,id_maquinaria,id_sumin,id_prove,id_mate)
        cursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for('datos10'))
    return render_template('inventario.html')

@app.route('/registrar')
def registrar():
    return render_template ('menuregistrar.html')

@app.route('/usuario')
def usuario():
    return render_template ('usuario.html')

@app.route('/iniciopagina')
def iniciopagina():
    return render_template ('inicio.html')

@app.route('/inicio2')
def inicio2():
    return render_template ('inicio2.html')

@app.route('/inicio3')
def inicio3():
    return render_template ('menuempleado.html')







