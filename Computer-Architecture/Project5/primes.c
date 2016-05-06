#include "header.h"

void setBit( int k ) {

   int i = k/32;
   int pos = k%32;
   unsigned int flag = 1;
   flag = flag << pos;
   prime[i] = prime[i] | flag;
}

/* -------------------------------------------------
   testBit( n ): return 1 if bit n is RESET
   ------------------------------------------------- */
int testBitIs0( int k ) {

   int i = k/32;
   int pos = k%32;
   unsigned int flag = 1;
   flag = flag << pos;

   int r = prime[i] & (1 << pos); 

   if ( r == 0 )
      return 1;        // return 1 to indicate that n is still prime
   else
      return 0;
}


void sieveOfE( int N )

/*this finds all the prime numbers that are 
* less than or equal to N using the Sieve 
* of Erathothenes algorithm. 
*/

/*The array element with index i is true if the number i is prime and false otherwise. */
/* 0 = false and 1=true*/

	 int i;
	 int j;
	 int k;
	
	for ( i = 0; i < N/MAX+1; i++ )
      prime[i] = 0;


	setBit( 0 );    // 0 is not prime
   setBit( 1 );    // 1 is not prime

	 

 k = 2;   // Start with 2 to find all primes


    /* ------------------------
       Perform the sieve of E
       ------------------------ */	  


	      while ( k <= N )
	      {
	
		 for ( i = k; i <= N; i++ )
		     if ( testBitIs0(i) )
		        break;             // Found !


		 for ( j = 2*i; j <= N; j = j + i )
		     setBit(j);
	  
		 k = i+1;
	      }

	 return isPrime; /* the Output is a boolean array */
}

int countPrimes( int N ){
/* this finds the number of primes that are less than or equal to N. */
	int count, i;

   count = 0;

   for ( i = 2; i <= N; i++ )
      if ( testBitIs0(i) )
         count++;

   return count;


}


void printPrimes( int k1, int k2, int N ){

/*This prints the prime numbers starting at the k1th prime 
* and ending at the k2th prime for all primes ≤ N. 
*/
	int i;

   for ( i = 2; i <= N; i++ )
      if ( testBitIs0(i) )
         printf("%d ", i );
   printf("\n\n");

}
