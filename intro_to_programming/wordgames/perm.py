from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

def get_perms(hand, n):
    handlist = []
    for key in hand:
	for i in range(hand[key]):
	    handlist.append(key)
    l = [] 
    toret = []
    for c in xuniqueCombinations(handlist,n):
	l.append(c)
    for j in l:
        for p in xpermutations(j):
            toret.append("".join(p))
    return toret	

