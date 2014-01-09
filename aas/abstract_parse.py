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
    """
    word_dict = defaultdict(int)
    
    filtered_word_list = word_list #[w for w in word_list if not w in nltk.stopwords.words('english')]
    
    for word in filtered_word_list:
        word_stemmed = word.lower() #nltk.stem.snowball(word.lower())        
        word_dict[word_stemmed] += 1
    return word_dict
    

def test_words ():
    word_list = ['HeLlo','worlds']
    word_dict = words2dict(word_list)
    return word_dict


if __name__ == "__main__":
    word_dict = test_words()
    

    