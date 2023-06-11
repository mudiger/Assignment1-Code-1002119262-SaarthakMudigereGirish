from flask import request
from flask import Flask
from flask import render_template
import pyodbc
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

driver = '{ODBC Driver 17 for SQL Server}'
server = 'sqlserver-1002119262-saarthakmudigeregirish.database.windows.net'
database = 'DataBase-1002119262-SaarthakMudigereGirish'
username = 'saarthakmudigeregirish'
password = 'Hello123'

# Establish the connection
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Create a cursor object
cursor = conn.cursor()
print(cursor)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/picture/", methods=['GET', 'POST'])
def name():
    name = ""
    picture = ""
    if request.method == "POST":
        name = request.form.get('name')

        query = "SELECT Picture FROM dbo.people WHERE name = ?"
        cursor.execute(query, name)

        # Fetch the first row from the result set
        row = cursor.fetchone()
        if row is not None:
            picture = row[0]
        else:
            picture = None
            name = None

    return render_template("picture.html", name=name, picture=picture)


@app.route("/group/", methods=['GET', 'POST'])
def group():
    salary = ""
    salpics = []
    if request.method == "POST":
        salary = request.form.get('salary')

        # Execute a simple select query
        query = "SELECT Picture FROM dbo.people where Salary<?"
        cursor.execute(query, salary)
        # Fetch the first row from the result set
        rows = cursor.fetchall()
        for i in rows:
            salpics.append(i[0])

    return render_template("group.html", salpics=salpics)

'''
@app.route("/add/", methods=['GET', 'POST'])
def add():
    name = ""
    picture = ""
    if request.method == "POST":
        name = request.form.get('name')
        add = request.form.get('add')

        query = "SELECT Picture FROM dbo.people WHERE name = ?"
        cursor.execute(query, name)

        # Fetch the first row from the result set
        row = cursor.fetchone()
        if row is not None:
            picture = row[0]
        else:
            picture = None
            name = None

    return render_template("add.html", name=name, picture=picture)
    add = ""
    salpics = []
    picture=''
    if request.method == "POST":
        add = request.form.get('add')

        # Execute a simple select query
        if(name=="all"):
            query = "UPDATE Picture FROM dbo.people where Salary<9000"
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
    return render_template("picture.html", name=name)
'''


@app.route("/remove/", methods=['GET', 'POST'])
def remove():
    name = ""
    if request.method == "POST":
        name = request.form.get('name')

        query = "DELETE FROM dbo.people WHERE name = ?"
        cursor.execute(query, name)

        # Fetch the first row from the result set
        row = cursor.fetchone()
        if row is not None:
            name = row.Picture
        else:
            name = None
        return render_template("remove.html", name=name)


@app.route("/keyword/", methods=['GET', 'POST'])
def keyword():
    name = ""
    keyword = ""
    if request.method == "POST":
        name = request.form.get('name')
        keyword = request.form.get('keyword')

        query = "UPDATE dbo.people SET keywords=? WHERE name=?"
        cursor.execute(query, keyword, name)
        conn.commit()

        query = "SELECT keywords FROM dbo.people WHERE name=?"
        cursor.execute(query, name)

        # Fetch the first row from the result set
        row = cursor.fetchone()
        if row is not None:
            keyword = row[0]
        else:
            name = None

    return render_template("keyword.html", name=name, keyword=keyword)


@app.route("/salary/", methods=['GET', 'POST'])
def salary():
    name = ""
    salary = ""
    if request.method == "POST":
        name = request.form.get('name')
        salary = request.form.get('salary')

        query = "UPDATE dbo.people SET Salary=? WHERE name=?"
        cursor.execute(query, salary, name)
        conn.commit()

        query = "SELECT Salary FROM dbo.people WHERE name=?"
        cursor.execute(query, name)

        # Fetch the first row from the result set
        row = cursor.fetchone()
        if row is not None:
            salary = row[0]
        else:
            name = None

    return render_template("salary.html", name=name, salary=salary)


if __name__ == "__main__":
    app.run()
