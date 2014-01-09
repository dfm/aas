#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = ["Dataset"]

import json
from nltk import sent_tokenize, word_tokenize


class Dataset(object):

    def __init__(self, path):
        with open(path, "r") as f:
            sessions = json.load(f)

        self.data = []
        for key, session in sessions.iteritems():
            for pid, pres in session["presentations"].iteritems():
                self.data.append({
                    "id": pres["id"],
                    "session_id": key,
                    "session_name": session["title"],
                    "room": session["room"],
                    "words": self.parse(pres["title"]+" "+pres["abstract"]),
                    "title": pres["title"],
                    "abstract": pres["abstract"],
                    "date": session["date"],
                    "type": session["type"],
                    "authors": [a[0] for a in pres["authors"]],
                })

    def parse(self, text):
        return [w for s in map(word_tokenize, sent_tokenize(text)) for w in s]

    def __iter__(self):
        for doc in self.data:
            yield doc
