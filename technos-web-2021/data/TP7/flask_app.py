#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)


class Review(db.Model):
    id_review = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255))
    name=db.Column(db.String(), nullable=False)
    latitude=db.Column(db.Float(precision=10), nullable=False)
    longitude=db.Column(db.Float(precision=10), nullable=False)


@app.route("/", methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        all_reviews = Review.query.all()
        return render_template('index.html',
                                list_reviews=all_reviews,
                                nb_reviews = len(all_reviews),
                                current_date=date.today().isoformat())
    elif request.method == 'POST':
        new_review = Review(
            rate=request.form['rate'],
            comment=request.form['comment'],
            name=request.form['name'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude'],
        )
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('root'))

app.run(debug=True)