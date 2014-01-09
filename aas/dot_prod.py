# scalar product in the space of texts

import nltk
import numpy

def norm2(g, a):
    """
    calculates the norm squared of vector a with metric g
    INPUT:
        g, a - dictionaries
    OUTOUT:
        |a|^2 - float, the dot norm squared of a
        
    """
    res = 0.
    for key, value in a.iteritems():
        res += g.get(key, 0.) * value**2
        
    return res



def product(g, a, b):
    """
    calculates the product of a and b with metric g
    INPUT:
        g - dictionary, metric
        a - dictionary, user vector
        b - dictionary, test text vector
        
    OUTOUT:
        (a, b) - float, the dot product
        
    """
    
    a_norm = np.sqrt(norm2(g, a))
    b_norm = np.sqrt(norm2(g, b))

    res = 0.
    for key, value in b.iteritems():
        res += g.get(key, 0.) * a.get(key, 0.) * value

    res /= (a_norm * b_norm)
    
    return res


