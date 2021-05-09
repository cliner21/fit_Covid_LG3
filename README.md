# fit_Covid_LG3
Region fit of Johns Hopkins Covid-19 data using three lognormal functions. This code is open for public use.

Python3 code with several standard library includes. Assumes *c19subs.py* is in the same directory. The code is a bit sensitive. The fit is across a 12-dimensional parameter space and a good starting point and set of parameter bounds are essential. These are generated randomly for each iteration. The user needs to supply an accuracy goal, this is set to 500 which seems suitable for India as of 9 May 2021. 

To run code from the command line:
```
python fitLG3region.py
```
With result:
```
searching: iter= 1  goal= 500.0  accuracy= 342751
searching: iter= 2  goal= 500.0  accuracy= 10000000
searching: iter= 3  goal= 500.0  accuracy= 10000000
searching: iter= 4  goal= 500.0  accuracy= 12435
searching: iter= 5  goal= 500.0  accuracy= 55478
.
.
.
searching: iter= 83  goal= 500.0  accuracy= 10000000
searching: iter= 84  goal= 500.0  accuracy= 259789
searching: iter= 85  goal= 500.0  accuracy= 461
```
That generated this fit:

Author: Christopher Liner

Department of Geosciences,
University of Arkansas,
Fayetteville, AR, USA
