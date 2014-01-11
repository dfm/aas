#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

__all__ = ["app"]

import flask
import json
import sqlite3
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


def order_by(q, query=None, args=()):
    if q is None:
        return None
    q = [w for s in map(word_tokenize, sent_tokenize(q)) for w in s]
    vec = words2dict(q)
    scores = []

    with flask.g.db as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        if query is None:
            query = "select * from abstracts"
        c.execute(query, args)
        abstracts = c.fetchall()

    for i, abstract in enumerate(abstracts):
        scores.append((i, compute_dot(vec, json.loads(abstract["counts"]))))
    inds = sorted(scores, key=lambda o: o[1], reverse=True)
    return [abstracts[i] for i, score in inds[:10]]


@app.before_request
def before_request():
    flask.g.db = sqlite3.connect("aas/aas.db")


@app.teardown_request
def teardown_request(exception):
    db = getattr(flask.g, "db", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    q = flask.request.args.get("q", None)
    p, t = ("posters" in flask.request.args), ("talks" in flask.request.args)
    if p or t:
        if p and t:
            sq = "type=? or type=?"
            args = ("Oral Session", "Poster Session")
        else:
            sq = "type=?"
            args = ("Poster Session", ) if p else ("Oral Session", )

        query = """select * from abstracts
                   where session_id in
                        (select id from sessions where {0})
                """.format(sq)
        abstracts = order_by(q, query=query, args=args)

    else:
        abstracts = order_by(q)

    return flask.render_template("index.html", abstracts=abstracts)


@app.route("/abs/<abs_id>")
def abstract(abs_id):
    with flask.g.db as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("select * from abstracts where aas_id=?", (abs_id,))
        doc = c.fetchone()

        if doc is None:
            return flask.abort(404)

        c.execute("select * from sessions where id=?", (doc["session_id"],))
        session = c.fetchone()

        c.execute("select name from authors where abstract_id=?",
                  (doc["id"],))
        authors = map(lambda a: a[0], c.fetchall())
    abstracts = order_by(doc["title"] + " " + doc["abstract"])
    return flask.render_template("abstract.html", doc=doc,
                                 abstracts=abstracts[1:],
                                 session_info=session, authors=authors)
