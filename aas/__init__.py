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


@app.before_request
def before_request():
    with app.open_resource("abstracts.json") as f:
        flask.g.abstracts = json.load(f)


@app.route("/")
def index():
    q = flask.request.args.get("q", None)
    abstracts = None
    if q is not None:
        q = [w for s in map(word_tokenize, sent_tokenize(q)) for w in s]
        vec = words2dict(q)
        scores = []
        for abstract in flask.g.abstracts:
            scores.append(compute_dot(vec, abstract["counts"]))
        inds = sorted(zip(range(len(scores)), scores), key=lambda o: o[1],
                      reverse=True)
        abstracts = [flask.g.abstracts[i] for i, score in inds[:10]]

    print(abstracts)

    return flask.render_template("index.html", abstracts=abstracts)
