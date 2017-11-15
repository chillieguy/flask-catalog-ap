# Flask imports

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

# Database imports

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Catagory, Item


# Create the app

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Routes

@app.route('/')
def index():
    catagories = session.query(Catagory).all()
    return render_template('index.html', catagories=catagories)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
