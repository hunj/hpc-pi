#Comparing Implementations
The four methods for computing pi all depend on different mathematical formulas and ideas. 
The different formulas or algorithms were easily implemented using python. 

#Runtime for calculating less than 100 digits of Pi
- The Chudnovsky's and Brent-Salamin algorithms both calculated 100 digts pi in less a millisecond. 
- While the Monte-Carlo method took almost a second to calculate just to calculate 5 digits. 
- Furthermore, while the Nilakantha series is also a converging series like Chudnosky's and Brent-Salamin, 
the series coverged slower and took many more iterations to calculate the next digits of pi. 
The method took almost a second to calculate 10 digits of pi. 

#Runtime for thousands of digits of Pi 
- Monte-Carlo method was not used because many iterations were required to calculate just a few more digits of pi. 
It could not keep up with the other processes. 
- While the Nilakantha series was much faster than the Monte-Carlo, it required more iteration and more time per additional iteration.
We did not use this method to calculate more digits of pi. 
- The Chudnovsky's and Brent-Salamin algorithms were compared

#Chudnovsky's Algorithm
- 10000 digits took 449s
- 20000 digits took 3512s
- 40000 digits took 27675s
- We reached the limit for compute notes while trying to compute 50000 digits of pi

#Brent-Salamin's Algorithm
- 10000 digits took 21s
- 20000 digits took 115s
- 40000 digits took 421s
- 75000 digits took 1621s
- 120000 digits took 4465s 
