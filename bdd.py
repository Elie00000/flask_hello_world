import sqlite3
from werkzeug.security import generate_password_hash

def create_user_db():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()

    # Créer la table
    c.execute('''CREATE TABLE users
                 (email text primary key, password text)''')

    # Insérer un utilisateur
    hashed_password = generate_password_hash('Islande-2404', method='sha256')
    c.execute("INSERT INTO users VALUES ('emile.alberici.snir@gmail.com', ?)", (hashed_password,))

    # Enregistrer (commit) les modifications
    conn.commit()

    # Fermer la connexion
    conn.close()

create_user_db()
