# fit_Covid_LG3
Region fit of Johns Hopkins Covid-19 data using three lognormal functions. This code is open for public use.

Python3 code with several standard library includes. Assumes *c19subs.py* is in the same directory. The code is a bit sensitive. The fit is across a 12-dimensional parameter space and a good starting point (p0) and set of parameter bounds are essential. The bounds and p0 are generated randomly for each iteration. The core routine is scipy.optomize set with maxfev=5000, but if p0 or bounds are pathelogical, optomize may run to full 5000 function evals without convergence and code will terminate with error. Rare event, just run it again and hope for the best.

The user needs to supply an accuracy goal, this is set to target=500 which seems suitable for India as of 9 May 2021. 

To run code from the command line:
```
python fitLG3region.py
```
With (a) result:
```
searching: iter= 1  goal= 500.0  accuracy= 50600
searching: iter= 2  goal= 500.0  accuracy= 10000000
searching: iter= 3  goal= 500.0  accuracy= 90499345
.
.
.
searching: iter= 34  goal= 500.0  accuracy= 120131516
searching: iter= 35  goal= 500.0  accuracy= 357248
searching: iter= 36  goal= 500.0  accuracy= 463
```
The generated fit for this run is in the file *LG3_May09_India.pdf*

Author: Christopher Liner

Department of Geosciences,
University of Arkansas,
Fayetteville, AR, USA
