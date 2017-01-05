# "Molecules to Atoms"
# Codewars kata url: https://www.codewars.com/kata/52f831fa9d332c6591000511
#
# Takes in a molecular formula as a string and returns a dictionary with 
# each atom as a key and the number of each atom as the value
# Input can include an arbitrary number of parentheses and distributed subscripts
#
# Author: Jennine Nash (2016)

import re

def parse_molecule (formula):

    # regex to separate all terms of the formula 
	# where a term is a chemical symbol, a number, or a bracket
    ex = "([A-Z][a-z]|[A-Z]|[\[\({\]\)}]|[0-9]+)"
	
	# sets of possible opening and closing brackets
    p_set = {'(', '{', '['}
    p_set2 = {')', '}', ']'}
	
	# stack to keep track of how many levels of brackets we're in
	# each item is a pair: ([bracket], [index])
    parens = []
	
	# dictionary where the key is a pair: a chemical symbol and its index in the list of terms
	# and the value a pair: the current number of atoms of that element and the length of the
	# 	stack of brackets when it is found
    mols = {}
	
    final = {}
    
    els = re.findall(ex, formula)
    
    for i in range(0, len(els)):
        if els[i] in p_set:
            parens.append((els[i], i)) # note that we are entering a new set of brackets
		
		# closing a set of brackets
        elif els[i] in p_set2:
		
			# pop off last bracket which is the open bracket matching the current closing bracket
            (p, k) = parens.pop()
			
			# if next item in formula is a number, distribute it to all the elements
			# which were inside the set of brackets
            for (s, j) in mols:
                (c, l) = mols[(s,j)]
                if els[i+1].isdigit(): 
                    if j >= k:
                        mols[(s,j)] = (c*int(els[i+1]), l) 
			
			# reset all values in mols to indicate they are inside brackets which have 
			# been completely closed and therefore should have no subscripts 
			# distributed to them in the future
            if len(parens) == 0:
                for (s, j) in mols:
                    (c, l) = mols[(s, j)]
                    mols[(s, j)] = (c, 0)
		
		# if next term is a chemical symbol, add it to mols
        elif re.match("^[A-Z][a-z]?$", els[i]):
            count = 1
            if i < len(els)-1 and els[i+1].isdigit():
                count = int(els[i+1])
            mols[(els[i], i)] = (count, len(parens))
    
	# combine the counts for all entries in mols with the same chemical symbol 
    for (s, j) in mols:
        (c, l) = mols[(s,j)]
        if s in final:
            final[s] += c
        else:
            final[s] = c
    
    return final