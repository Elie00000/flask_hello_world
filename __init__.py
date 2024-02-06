from flask import Flask, render_template_string, render_template, jsonify, json
from urllib.request import urlopen
import sqlite3
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_clé_secrète_ici'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Ici, vous devriez vérifier les identifiants de l'utilisateur
    # Si ils sont corrects, vous pouvez connecter l'utilisateur
    username = request.form['username']
    user = User()
    user.id = username
    login_user(user)
    return redirect(url_for('protected'))

@app.route('/protected')
@login_required
def protected():
    return 'Connecté !'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Déconnecté !'
@app.route("/histogramme/")
@login_required
def mongraphique():
    return render_template("histogramme.html")

if __name__ == "__main__":
  app.run(debug=True)
