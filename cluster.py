# coding: utf-8

""" Run a sparse PCA on AAS abstract word counts """

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
import os, sys
import json
import time

# Third-party
import numpy as np
import sklearn
from sklearn.cluster import KMeans, MiniBatchKMeans
from scipy.sparse import bsr_matrix

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
    X = bsr_matrix(X)
    
    print("Initializing k-means")
    km = MiniBatchKMeans(n_clusters=50, init='k-means++', n_init=1,
                         init_size=1000, batch_size=1000, verbose=True)
    print("fitting")
    t0 = time.time()
    km.fit(X) # X is nsamples, nfeatures
    print("Took {} seconds".format(time.time()-t0))

    return km

#if __name__ == "__main__":
#    main()
