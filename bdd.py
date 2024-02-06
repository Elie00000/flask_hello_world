import sqlite3
from werkzeug.security import generate_password_hash

def create_user_db():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()

    try:
        # Vérifier si la table existe
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if c.fetchone() is None:
            # Créer la table si elle n'existe pas
            c.execute('''CREATE TABLE users
                         (email text primary key, password text)''')

        # Insérer un utilisateur
        email = 'emile.alberici.snir@gmail.com'  # à obtenir de manière sécurisée
        password = 'Islande-2404'  # à obtenir de manière sécurisée
        hashed_password = generate_password_hash(password, method='sha256')
        c.execute("INSERT INTO users VALUES (?, ?)", (email, hashed_password))

        # Enregistrer (commit) les modifications
        conn.commit()
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        # Fermer la connexion
        conn.close()

create_user_db()
