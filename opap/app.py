import sqlite3
from . import db, create_app, Participant, utils

import pandas as pd
from flask import request
from flask import render_template, redirect, url_for

app = create_app()

@app.route("/", methods=["GET", "POST"])
def index():
    con = db.get_db() # /data/database.db connection
    
    if request.method == 'POST':
        data = [request.form.get(key, None) for key in ("first", "last", "mail")]    
        if all(data):
            entry = Participant(*data)
                        
            try:
                utils.is_valid_email(email=entry.mail)
                utils.insert_entry(entry=entry, con=con)
                utils.success_alert(entry=entry)                
            except sqlite3.IntegrityError:
                utils.duplicate_alert()
            except ValueError:
                utils.bad_email_alert(email=entry.mail)
                
            redirect(url_for("index"))
 
    
    return render_template("index.html")

@app.route("/entries")
def entries():
    con = db.get_db()
    users = pd.read_sql_query("SELECT * FROM user", con=con)
    print (users.to_dict(orient="records"))
    return render_template("entries.html", users=users.to_dict(orient="records"))