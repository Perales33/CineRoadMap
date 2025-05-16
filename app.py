from flask import Flask, render_template, request, redirect, url_for, make_response, flash, session, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuración de la clave secreta para las sesiones
app.secret_key = os.urandom(24)  # Genera una clave secreta aleatoria para la sesión

# Ruta para el inicio (index.html)
# Redirige a la página de inicio si el usuario está autenticado, de lo contrario, redirige a la página de inicio de sesión.
@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

# Ruta para mostrar recetas

@app.route('/movies')
def movies():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    conn.close()
    return render_template('movies.html', movies=movies)

@app.route('/actors', methods=['GET', 'POST'])
def actors():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    query = request.args.get('query', '')  # Buscar actor por nombre
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if query:
        # Buscar actores por nombre
        cur.execute("SELECT * FROM actors WHERE actor_name LIKE ?", ('%' + query + '%',))
    else:
        # Mostrar todos los actores si no se da una consulta
        cur.execute("SELECT * FROM actors")

    actors = cur.fetchall()
    conn.close()

    return render_template('actors.html', actors=actors)


# Ruta para buscar recetas
# Muestra todas las recetas almacenadas en la base de datos si el usuario está autenticado,
# de lo contrario, redirige a la página de inicio de sesión. Devuelve los resultados en formato JSON.
@app.route('/search')
def search():
    query = request.args.get('query', '')
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies WHERE title LIKE ?", ('%' + query + '%',))
    movies = cur.fetchall()
    conn.close()
    return jsonify([dict(movie) for movie in movies])

@app.route('/searchActors')
def searchActors():
    query = request.args.get('query', '')
    conn = sqlite3.connect('movies.db')  # Asegúrate de que la base de datos esté configurada correctamente
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM actors WHERE actor_name LIKE ?", ('%' + query + '%',))
    actors = cur.fetchall()
    conn.close()
    return jsonify([dict(actor) for actor in actors])

@app.route("/perfil")
def perfil():
    if 'user_id' in session:
        return render_template('perfil.html')
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('movies.db')  # Asegúrate de que la base de datos esté configurada correctamente
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

@app.route('/movie/<string:title>')
def movie_detail(title):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('movies.db')  # Asegúrate de que la base de datos esté configurada correctamente
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    # Obtén la película
    cur.execute("SELECT * FROM movies WHERE title = ?", (title,))
    movie = cur.fetchone()

    conn.close()
    
    return render_template('movie_detail.html', movie=movie)


@app.route('/actor/<string:actor_name>')
def actor_detail(actor_name):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM actors WHERE actor_name = ?", (actor_name,))
    actor = cur.fetchone()
    conn.close()

    return render_template('actor_detail.html', actor=actor)

# Ruta para mostrar el formulario de inicio de sesión
# Muestra un formulario para que el usuario inicie sesión.
# Si las credenciales son correctas, inicia la sesión del usuario y lo redirige al inicio.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('movies.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = username
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Ruta para mostrar el formulario de registro
# Muestra un formulario para que el usuario se registre en la aplicación.
# Si el registro es exitoso, redirige al usuario a la página de inicio de sesión.
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('movies.db')
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            flash('Registro exitoso. Puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El nombre de usuario ya está en uso', 'danger')
        conn.close()

    return render_template('register.html')

# Ruta para cerrar sesión
# Elimina los datos de la sesión y redirige al usuario a la página de inicio de sesión.
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

# Ruta para la página "About Us"
# Muestra información sobre la aplicación o el equipo de desarrollo.
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para la página "Contact Us"
# Muestra un formulario de contacto o información para contactar con los desarrolladores.
@app.route('/contact')
def contact():
    return render_template('contact.html')