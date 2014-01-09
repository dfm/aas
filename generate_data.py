#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import json
from collections import defaultdict

from aas.data import Dataset
from aas.abstract_parse import words2dict

if __name__ == "__main__":
    print("Loading dataset...")
    dataset = Dataset("data/abstracts.json")
    print("Finished.")

    print("Parsing abstracts...")
    abstracts = []
    corpus = defaultdict(int)
    for doc in dataset:
        vec = words2dict(doc["words"])
        for k, v in vec.iteritems():
            corpus[k] += v
        abstracts.append(dict(id=doc["id"], counts=vec, title=doc["title"],
                              abstract=doc["abstract"]))
    print("Finished.")

    print("Saving data files...")
    with open("www/corpus.json", "w") as f:
        json.dump(dict(corpus), f)
    with open("www/abstracts.json", "w") as f:
        json.dump(abstracts, f)
