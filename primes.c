
#include<header.h>
#include<main.c>
#include<main.o>




void sieveOfE( int N )

/*this finds all the prime numbers that are 
* less than or equal to N using the Sieve 
* of Erathothenes algorithm. 
*/

/*The array element with index i is true if the number i is prime and false otherwise. */
/* 0 = false and 1=true*/

	 int  isPrime[N+1];
	 int i;
	 int j;
	 int k;
	 int limit = N;

	A[k/32] |= 1 << (N%32);  // Set the bit at the k-th position in A[i]


	 isPrime[0] = 0; /* 0 is not prime */
	 isPrime[1] = 0; /* 1 is not prime */
	 
	for (i = 2; i <= limit; i++ ){
		 isPrime[i] = 1;   /* They are all candidates */     
	 }
 k = 2;   // Start with 2 to find all primes


    /* ------------------------
       Perform the sieve of E
       ------------------------ */	  


	      while ( k <= limit )
	      {
	
		 for ( i = k; i <= limit; i++ )
		     if ( isPrime[i] )
		        break;             // Found !


		 for ( j = 2*i; j <= limit; j = j + i )
		     isPrime[j] = 0;
	  
		 k = i+1;
	      }

	 return isPrime; /* the Output is a boolean array */
}

int countPrimes( int N ){
/* this finds the number of primes that are less than or equal to N. */



}


void printPrimes( int k1, int k2, int N ){

/*This prints the prime numbers starting at the k1th prime 
* and ending at the k2th prime for all primes ≤ N. 
*/


}
