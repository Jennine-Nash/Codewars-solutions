/* "Some Egyptian Fractions"
 * Codewars kata url: https://www.codewars.com/kata/some-egyptian-fractions/c
 * 
 * Takes in the numerator and denominator of a fraction and decomposes the fraction
 * into a series of 1/x_i where 1/x_1 + 1/x_2 + ... + 1/x_n is equal to the fraction.
 * Program should be "greedy," that is, each successive fraction should have as 
 * small a denominator as possible.
 *
 * Author: Jennine Nash
 */

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define FRAC_MAX 30 // any one fraction should not be more than 30 chars
#define RES_MAX 100 // the final result should not be more than 100 chars

// creates a string of a fraction with numerator 1 and denominator dr
char* add_frac(long long dr, int last) {
  char* frac = (char*)malloc(FRAC_MAX*sizeof(char));
  if (last) {
    sprintf(frac, "1/%lld", dr);
  }
  else {
    sprintf(frac, "1/%lld,", dr);
  }
    
  return frac;
}

char* decompose(char* nrStr, char* drStr) {
  long long i, nr, dr, cd, cn;
  char* result = malloc(RES_MAX);
  memset(result, 0, RES_MAX);
    
  nr = (long long)strtol(nrStr, (char**)NULL, 10);
  dr = (long long)strtol(drStr, (char**)NULL, 10);
  
  if (nr == 0) return result;
  if (nr % dr == 0) {
    sprintf(result, "%lld", nr/dr);
    return result;
  }
  // starts result with whole number then continues with fraction part
  if (nr > dr) {
    sprintf(result, "%lld,", nr/dr);
    nr = nr % dr;
  }
  
  // checking all possible denominators starting with 2
  // will terminate when final fraction is found
  for (i = 2; ; i++) {
  
    // adjust nr/dr to have a common denominator with 1/i
    cd = i*dr;
    cn = i*nr;
    
    // nr/dr is smaller than 1/i
    if (dr > cn) continue;
    // nr/dr == 1/i so the program is done
    else if (dr == cn) {
      result = strcat(result, add_frac(i, 1));
      return result;
    }
    // nr/dr > 1/i so we can subtract 1/i from nr/dr
    else {
      result = strcat(result, add_frac(i, 0));
      nr = cn - dr;
      dr = cd;
      
      // to make program faster, check if we are one fraction away from finishing
      if (dr % nr == 0) {
        result = strcat(result, add_frac(dr/nr, 1));
        return result;
      }
    }
  }
}