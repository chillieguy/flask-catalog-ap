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
    items = session.query(Item).order_by(Item.updated_at).limit(10).all()
    return render_template('index.html', catagories=catagories, items=items)


@app.route('/catalog/<int:catagory_id>/')
def show_catagory(catagory_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).one()
    items = session.query(Item).filter_by(catagory_id=catagory.id)

    return render_template('showcatagory.html', catagory=catagory, items=items)

@app.route('/catalog/<int:catagory_id>/<int:item_id>/')
def show_item(catagory_id, item_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).one()
    item = session.query(Item).filter_by(id=item_id).one()

    return render_template('showitem.html', catagory=catagory, item=item)

@app.route('/catalog/additem/', methods=['GET', 'POST'])
def add_item():
    catagories = session.query(Catagory).all()

    if request.method == "POST":
        if request.form['item']:
            if request.form['description']:
                if request.form['catagory']:
                    name = request.form['item']
                    description = request.form['description']
                    catagory_id = int(request.form['catagory'])
                    
                    new_item = Item(name=name, description=description, catagory_id=catagory_id)
                    session.add(new_item)
                    session.commit()
        return redirect(url_for('index'))

    return render_template('additem.html', catagories=catagories)


@app.route('/catalog/edititem/<int:item_id>/', methods=['GET', 'POST'])
def edit_item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    catagories = session.query(Catagory).all()

    if request.method == "POST":
        if request.form['item']:
            if request.form['description']:
                if request.form['catagory']:
                    name = request.form['item']
                    description = request.form['description']
                    catagory_id = int(request.form['catagory'])

                    edit_item = session.query(Item).filter_by(id=item_id).one()
                    edit_item.name = name
                    edit_item.description = description
                    edit_item.catagory_id = catagory_id
                    session.commit()
        return redirect(url_for('index'))

    return render_template('edititem.html', item=item, catagories=catagories)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
