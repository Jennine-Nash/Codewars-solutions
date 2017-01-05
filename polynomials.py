# "Simplifying Multilinear Polynomials"
# Codewars kata url: https://www.codewars.com/kata/55f89832ac9a66518f000118
#
# Takes in a multilinear polynomial represented by a string and returns the same 
# polynomial in its simplest form, sorted by number of variables and then alphabetically
#
# Author: Jennine Nash (2016)

import re

def simplify(poly):
    ex = "[+-]?[0-9]*[a-z]+" # separate poly into all its separate monomials
    ex2 = "([a-z]+$)" # extract variables from a monomial
    ex3 = "(^[+-]?[0-9]*)" # extract coefficient from a monomial
    coef = {} # dictionary with variable as key and coefficient as value
    final = ''
    
    monos = re.findall(ex, poly)
    for i in range(0, len(monos)):
		
		# separate each monomial into coefficient and variable
        r = re.search(ex2, monos[i])
        c = re.search(ex3, monos[i])
        r0 = ''.join(sorted(list(r.group(0))))
        c0 = c.group(0)
        if c0 == '-' or c0 == '' or c0 == '+':
            c0 += '1'
        
		# combine coefficients if variable has already been seen, otherwise create new
        if r0 in coef:
            coef[r0] += int(c0)
        else:
            coef[r0] = int(c0)
    
	# sort monomials by number of variables, then alphabetically
    deps = sorted(coef, key=lambda x: (len(x), x))
	# throw out monomials with 0 coefficients
    deps = [x for x in deps if coef[x] != 0]
        
	# construct simplified polynomial as a string
    for i in range(0, len(deps)):
        n = coef[deps[i]]
        num = str(n)
        if abs(n) == 1:
            num = str(n)[:len(str(n))-1] # get rid of 1 coefficients
			
        if i == 0 or n < 0:
            final += num + deps[i] # don't need to add sign if first monomial or negative coefficient
        else:
            final += '+' + num + deps[i]
    
    return final