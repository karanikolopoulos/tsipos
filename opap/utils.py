from . import Participant
import re, sqlite3
from flask import flash


def is_valid_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError


def success_alert(entry: Participant) -> None:
    msg = (
        f"Επιτυχής συμμετοχή\\n"
        f"Όνομα: {entry.first}\\n"
        f"Επώνυμο: {entry.last}\\n"
        f"e-mail: {entry.mail}\\n"        
    )
    
    flash(msg)

def bad_email_alert(email:str) -> None:
    flash(f"Μη έγκυρο email: {email}")
    

def duplicate_alert() -> None:
    flash("Τα στοιχεία υπάρχουν ήδη.")


def insert_entry(entry: Participant, con: sqlite3.Connection):
    cursor = con.cursor()
    
    cursor.execute(
        "INSERT INTO user (firstname, lastname, mail) VALUES (?, ?, ?)",
        (entry.first, entry.last, entry.mail)
    )
    con.commit()