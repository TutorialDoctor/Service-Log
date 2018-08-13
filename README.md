# Service-Log
Service Log

## 1. Install SQLAlchemy

<pre>pip install sqlalchemy</pre>

[Get Help](https://www.pythoncentral.io/how-to-install-sqlalchemy/)

## 2. Create the Database
Open a python interpreter from a terminal in the project folder and create the database from the models in the `app.py` file as shown below:

<pre>
python3
from app.py import db
db.create_all()
</pre>

## 3. Run the app

Exit the python interprerter using `exit()` and run the app:

<pre>
python3 app.py
</pre>

It will run on `port 5000` in debug mode.

<pre>
http://http://localhost:5000
</pre>
