#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

entries = [
 {"id_review": 1, "id_batiment": 26, "rate": 5, "comment": "Mattis molestie a iaculis at erat pellentesque adipiscing commodo."},
 {"id_review": 2, "id_batiment": 18, "rate": 4, "comment": "Amet massa vitae tortor condimentum lacinia."},
 {"id_review": 3, "id_batiment": 31, "rate": 3, "comment": "Imperdiet sed euismod nisi porta lorem mollis aliquam."},
 {"id_review": 4, "id_batiment": 22, "rate": 1, "comment": "Dignissim enim sit amet venenatis. Urna cursus eget nunc scelerisque."},
 {"id_review": 5, "id_batiment": 26, "rate": 4, "comment": "A pellentesque sit amet porttitor eget dolor morbi."},
 {"id_review": 6, "id_batiment": 18, "rate": 3, "comment": "Consequat nisl vel pretium lectus quam id leo in vitae."},
]

@app.route('/')
@app.route('/index')
def index():
    current_date = date.today().isoformat()

    return render_template(
        'index.html',
        nb_reviews = len(entries),
        current_date = current_date,
        list_reviews = entries,
    )


@app.route('/review/<int:n>')
def review(n):
    index = n - 1
    rate = entries[index]["rate"]
    comment = entries[index]["comment"]
    return 'Rate : ' + str(rate) + ' Comment : ' + comment


