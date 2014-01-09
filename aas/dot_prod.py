# scalar product in the space of texts

#import nltk
import numpy as np

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
            for example, {'word': 1 / log(1 + n['word']), ...}
            where n['word'] is the number of times 'word' occurs in texts
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


if __name__ == '__main__':
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nw = len(words)
    n = np.arange(1., nw + 1., 1.)
    a = {}
    b = {}
    g = {}
    for i in range(nw):
        g[words[i]] = 1. / np.log(1. * i + 2.)
        
    for i in range(4):
        a[words[i]] = i * 2. + 1.
        b[words[nw - i - 1]] = i * 2. + 1.

    prod = product(g, a, b)

    print 'metric:', g
    print 'user vector:', a
    print 'text vector:', b
    print 'scalar product:', prod
    
