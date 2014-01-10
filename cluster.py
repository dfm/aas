# coding: utf-8

""" Run a sparse PCA on AAS abstract word counts """

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
import os, sys
import json

# Third-party
import numpy as np
import sklearn
from sklearn.decomposition import SparsePCA

def main():

    with open("aas/corpus.json") as f:
        corpus = json.loads(f.read())

    corpus = [(k,v) for k,v in corpus.items() if v > 5]
    corpus = sorted(corpus, key=lambda x: x[1])
    corpus = corpus[:-6]
    Ncorpus = len(corpus)

    with open("aas/abstracts.json") as f:
        abstracts = json.loads(f.read())

    X = np.zeros((len(abstracts),Ncorpus))
    for jj,abstract in enumerate(abstracts):
        for ii in range(Ncorpus):
            try:
                X[jj,ii] = abstract['counts'][corpus[ii][0]]
            except KeyError:
                continue

    pca = SparsePCA(alpha=100., tol=1e-4)
    pca.fit(X[:25]) # X is nsamples, nfeatures

if __name__ == "__main__":
    main()