#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

__all__ = ["app"]

import flask
import json
from math import sqrt

from nltk import sent_tokenize, word_tokenize
from .abstract_parse import words2dict

app = flask.Flask(__name__)


def compute_dot(u, d):
    value = 0.0
    norm = 0.0
    for k, v in d.iteritems():
        value += u.get(k, 0.0) * v
        norm += v*v
    return value / sqrt(norm)


def order_by(q):
    if q is None:
        return None
    q = [w for s in map(word_tokenize, sent_tokenize(q)) for w in s]
    vec = words2dict(q)
    scores = []
    for k, abstract in flask.g.abstracts.iteritems():
        scores.append((k, compute_dot(vec, abstract["counts"])))
    inds = sorted(scores, key=lambda o: o[1], reverse=True)
    return [flask.g.abstracts[i] for i, score in inds[:10]]


@app.before_request
def before_request():
    with app.open_resource("abstracts.json") as f:
        data = json.load(f)

    flask.g.abstracts = {}
    for doc in data:
        flask.g.abstracts[doc["id"]] = doc


@app.route("/")
def index():
    q = flask.request.args.get("q", None)
    abstracts = order_by(q)
    return flask.render_template("index.html", abstracts=abstracts)


@app.route("/abs/<abs_id>")
def abstract(abs_id):
    doc = flask.g.abstracts.get(abs_id, None)
    if doc is None:
        return flask.abort(404)
    abstracts = order_by(doc["title"] + " " + doc["abstract"])
    return flask.render_template("abstract.html", doc=doc,
                                 abstracts=abstracts[1:])
