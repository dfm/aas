#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import json
from math import log
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
            corpus[k] += 1
        doc["counts"] = vec
        abstracts.append(doc)
    print("Finished.")

    print("Normalizing be IDF...")
    d = len(abstracts)
    for w in corpus:
        corpus[w] = log(d/corpus[w])
    for abstract in abstracts:
        for w in abstract["counts"]:
            abstract["counts"][w] *= corpus[w]
    print("Finished.")

    print("Saving data file...")
    with open("aas/abstracts.json", "w") as f:
        json.dump(abstracts, f, sort_keys=True, indent=2,
                  separators=(",", ": "))
