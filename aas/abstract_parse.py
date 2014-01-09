# ########################################################################### #

# Standard Library
import os

# 3rd Party
import numpy as np
import nltk
from collections import defaultdict

# Internal

# ########################################################################### #

def words2dict (word_list):
    """
    Takes a list of words and returns the vector dictionary
    
    Parameters
    ----------
    word_list : list of strings
    
    Returns
    -------
    word_dict : defaultdict
        The keys are the stemmed words and values are a weighted value of how
        often they appear in an abstract
    
    """
    word_dict = defaultdict(int)
    
    filtered_word_list = word_list #[w for w in word_list if not w in nltk.stopwords.words('english')]
    
    for word in filtered_word_list:
        word_stemmed = word.lower() #nltk.stem.snowball(word.lower())        
        word_dict[word_stemmed] += 1
    return word_dict

def abstracts2word_vectors (abstracts):
    """
    Takes all the abstracts and gives back the vectorized version

    Parameters
    ----------
    abstracts : dict
        keys are abstract ids and values are a list of words from the abstract
    """
    word_vectors = [(ab_id,words2dict(word_list)) for ab_id,word_list in abstracts.items()]
    return word_vectors

def cache_abstracts (filepath,clobber=True):
    """
    write the dictionaries
    list of dict enteries if id,
    """
    if os.path.isfile(filepath) and not clobber:
        raise IOError("don't clobber file '{}'".format(filepath))
    
    raise Exception("do stuff")
    abstracts = None
    word_vectors = abstracts2word_vectors(abstracts)

    # save to file

def test_words ():
    word_list = ['HeLlo','worlds']
    word_dict = words2dict(word_list)
    return word_dict

if __name__ == "__main__":
    word_dict = test_words()
    

    