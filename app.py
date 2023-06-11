from flask import request
from flask import Flask
from flask import render_template
import pyodbc
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
@app.route("/", methods=['GET'])

def hello_world():
    name = ""
    salpics = []
    picture=''
    if request.method == "GET":
        name = request.args.get('name')
        server = 'sqlserver-1002119262-saarthakmudigeregirish.database.windows.net'
        database = 'DataBase-1002119262-SaarthakMudigereGirish'
        username = 'saarthakmudigeregirish'
        password = 'Hello123'
        driver = '{ODBC Driver 17 for SQL Server}'

        # Establish the connection
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

        # Create a cursor object
        cursor = conn.cursor()
        print(cursor)
        # Execute a simple select query
        if(name=="all"):
            query = "SELECT Picture FROM dbo.people where Salary<9000"
            cursor.execute(query)
            # Fetch the first row from the result set
            rows = cursor.fetchall()
            for i in rows:
                salpics.append(i[0])

        else:
            query = "SELECT Picture FROM dbo.people WHERE name = ?"
            cursor.execute(query, name)

            # Fetch the first row from the result set
            row = cursor.fetchone()
            if row is not None:
                picture = row.Picture
            else:
                picture = None

    return render_template("index.html", name=name, picture=picture,salpics=salpics)

if __name__ == "_main_":
    app.run()
