from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from flask.helpers import flash

from flaskext.mysql import MySQL

app = Flask(__name__)

# Conexion DB
app.config['MYSQL_DATABASE_HOST'] = '192.168.0.33'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'proyectoflask'


mysql = MySQL(app)

# Context processors


@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/tools')
def tools():
    return render_template('tools.html')


@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
        if request.method == 'POST':
                
                marca = request.form['marca']
                modelo = request.form['modelo']
                precio = request.form['precio']
                ciudad = request.form['ciudad']
                
                #return f"{marca} {modelo} {precio} {ciudad}"    
                
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute ("INSERT INTO coches VALUES (NULL, %s, %s, %s, %s)",(marca, modelo, precio, ciudad))
                cursor.connection.commit()
                return redirect(url_for('index'))

        return render_template('crear_coche.html')

@app.route('/coches')
def coches():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM coches")
    coches=cursor.fetchall()
    cursor.close()
    
    return render_template('coches.html', coches=coches)
      
if __name__ == '__main__':
    app.run(debug=True, port=8000)
