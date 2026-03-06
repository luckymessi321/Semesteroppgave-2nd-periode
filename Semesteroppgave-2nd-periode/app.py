# koden for funksjonen get_conn() og rutene ('/register') og ('/login') er limt inn fra en lærer sin presentasjon, men tilpasset prosjektet mitt. alle kommentarer er skrevet av meg unless stated otherwise
# koden for ruten '/save_score' er tatt fra en venn sitt prosjekt
from flask import Flask, render_template, redirect, session, request
import mysql.connector
from forms import RegisterForm, LoginForm


app = Flask(__name__)
# importert fra presentasjon
app.secret_key = "hemmelig-nok"

# funksjon som oppretter en tilkobling til databasen 'login' med brukeren 'lukas'
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="lukas",
        password="messi123",
        database="login"
    )

@app.route('/')
def index():
    return render_template('index.html')

# rute med kode som kjører KUN når register.html henter data fra app.py (GET), eller sender data til app.py (POST)
@app.route("/register", methods=["GET", "POST"])
def register():
    # oppretter et nytt objekt 'form' av 'RegisterForm' klassen importert fra forms.py
    form = RegisterForm()
    # kode som KUN kjører når brukeren sender inn data (submit)
    if form.validate_on_submit():
        # definerer brukernavn og passord i variabler
        username = form.username.data
        password = form.password.data

        # oppretter tilkobling til MySQL databasen og lagrer tilkoblingen som en variabel 'conn'. dette lar meg bruke methods som .commit()
        conn = get_conn()
        # oppretter et cursor objekt 'cur' koblet til databasen. dette objektet kan kjøre MySQL kode på serveren.
        cur = conn.cursor()
        # kjører MySQL kode på serveren som lagrer brukernavn og passord hentet fra '/register' ruten i databasen.
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        # lagrer endringene gjort i cur.execute og lukker tilkoblingen til databasen
        conn.commit()
        cur.close()
        conn.close()
        # sender brukeren til login siden
        return redirect("/login")

    return render_template("register.html", form=form)

# rute med kode som kjører KUN når login.html henter data fra app.py (GET), eller sender data til app.py (POST)
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        conn = get_conn()
        cur = conn.cursor()
        # kjører MySQL kode på serveren som henter brukernavnet til brukeren spilleren logget inn med
        cur.execute(
            "SELECT username FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        # lagrer brukernavnet som variablen 'user'
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        # kode som KUN kjører om spillerens brukernavn eksisterer
        if user:
            # lagrer brukernavn i session-data og sender spilleren til '/' ruten
            session['username'] = user[0]
            return redirect("/")
        # returnerer feilmelding om brukernavn ikke finnes
        else:
            form.username.errors.append("Invalid username or password")

    return render_template("login.html", form=form)

# oppretter ruten '/save_score' slik at app.py kan sende data til 'script.js' og motta data fra 'script.js'
@app.route('/save_score', methods=["POST"]) # methods=["POST"] får koden til å KUN aktivere når ruten får en POST-request (mottar data)
# funksjon som henter score fra 'script.js' og lagrer det i MySQL databasen
def save_score():
    # henter brukernavnet til brukeren lagret i '/login' ruten
    username = session.get('username')

    #  utfører en GET-request til script.js, leser resultatet som en JSON fil, konverterer resultatet til python format (.py), og lagrer resultatet som variablen 'data'. dette lar dataen bli brukt med metoder som .get(). 
    data = request.get_json()
    # lagrer verdien av nøkkelen 'score' i GET-requesten definert over som variablen score
    score = data.get('score')

    conn = get_conn()
    cur = conn.cursor()
    # kjører MySQL kode på serveren som oppdaterer 'score' verdien under den innloggede til å være scoren hentet fra script.js 
    cur.execute('UPDATE users SET score = %s WHERE username = %s', (score, username))

    # lagrer endringene gjort i cur.execute() og lukker tilkoblingen
    conn.commit()
    cur.close()
    conn.close()

    # sender ordboken 'status : success' til script.js
    return{'status': 'success'}


if __name__ == "__main__":
    app.run(debug=True)