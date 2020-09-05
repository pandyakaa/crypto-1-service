from flask import Flask

app = Flask(__name__)

from app import text_routes, file_routes