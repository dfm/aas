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

        self.data = {}
        for key, session in sessions.iteritems():
            for pid, pres in session["presentations"].iteritems():
                self.data[pres["id"]] = self.parse(pres["title"]
                                                   + " " + pres["abstract"])

    def parse(self, text):
        return [w for s in map(word_tokenize, sent_tokenize(text)) for w in s]

    def __iter__(self):
        for id_, doc in self.data.iteritems():
            yield doc

    def iteritems(self):
        for id_, doc in self.data.iteritems():
            yield id_, doc


if __name__ == "__main__":
    print("Loading")
    dataset = Dataset("data/abstracts.json")
    print("Loaded")
    for doc in dataset:
        print(doc)
