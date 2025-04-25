from flask import Flask

app = Flask(__name__)
app.secret_key = "@Mara1290"
from app import routes


