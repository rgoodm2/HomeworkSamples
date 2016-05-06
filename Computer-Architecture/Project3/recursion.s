* ====================================================================
* Do not touch the following xdef:
* ====================================================================
        xdef F, i, j, k
	xdef EndofF, ElseIf, Else, ForLoop, LastPartofElse


* **************************************************************************
* You can add more xdef directives above if you need more external labels
*
* - Remember that you can only add a label as a break point (stop location) 
*   in EGTAPI if the label has been xdef'ed !!!
*
* - And I am pretty sure you will need to use break point for debugging 
* - in this project... So add more xdef above to export your breakpoints
* **************************************************************************


F:

* ********************************************************************
* Put your (recursive) function F here 
*
* F receives the parameters i, j, k on the stack
* F returns the function value in register d0
*
* Make sure you use the "rts" instruction to return to the caller
* Also: Make sure you DE-ALLOCATE the local variables and restore a6
*       BEFORE you return to the caller !!!
* ********************************************************************
	
* -----------------------------------------
*int F(int i, int j, int k)
*  {
*     int s, t;
*
*     if ( i <= 0 || j <= 0 )
*        return(-1);
*     else if ( i + j < k )
*        return (i+j);
*     else
*     {
*        s = 0;
*        for (t = 1; t < k; t++)
*        {
*           s = s + F(i-t, j-t, k-1) + 1;               
*        }
*        return(s);
*     }
*  }*
* Note that when sum starts, the stack is:
*
*     +---------------+ <----- a7 (stack pointer)
*     | return address|	0(A7)
*     +---------------+
*     |      k        | 4(A7)
*     +---------------+
*     |      j        |	8(A7)
*     +---------------+
*     |      i        | 12(A7)
*     +---------------+
* -----------------------------------------
*	NOW WITH 2 LOCAL VARIABLES:
*      	   +---------------------+ <---- Stack pointer (A7)        
*    	   |          t          | -8(A6)
*          +---------------------+ 
*      	   |          s          | -4(A6)
*          +---------------------+ <---- Frame pointer (A6)
*          |     return address  | 0(A6)
*          +---------------------+
*     	   |          k          | 4(A6)
*          +---------------------+
*    	   |          j          | 8(A6)
*          +---------------------+
*      	   |          i          | 12(A6)
*          +---------------------+
*

	MOVEA.L A7, A6 		*setting up as A6
	SUBA.L #8, a7 		*Create 2 local variables!!
	MOVE.L #0, -8(A6)	* t = 0
	MOVE.L #0, -4(A6)	* s = 0

	MOVE.L 12(A6), D1	* puts parameter i in d1
	CMP #0, D1
	BLE ElseIf		*Branch if i is greater than 0

	MOVE.L 8(A6), D2	*puts paramter j in D2
	CMP #0, D2
	BGT ElseIf		*Branch if j is greater than 0

*Then Part of if statement
	MOVE.L #-1,D0
	BRA EndofF 		*return -1 and end function

ElseIf:

	ADD.L D1, D2 		*D2 now equals i + j
	MOVE.L 4(A6), D3 	*D3 now equals k	
	CMP D2,D3
	BGE Else 		*Brnch if greater than or equal to

	MOVE D2,D0		*return i+j and end function
*rts	
	BRA EndofF
Else:
	MOVE.L -4(A6), D4	*Now s is stored in D4
	MOVE.L #0, D4		*s (stored in D4) = 0

	MOVE.L -8(A6), D5	*t is stored in D5
	MOVE.L #1,D5		*t=1
ForLoop:
	CMP D5,D3
	BGE LastPartofElse

*Recursive part
*s = s + F(i-t, j-t, k-1) + 1;
	MOVE.L -4(A6),D4
	ADD.L #1,D4	*S+1
	
	MOVE.L 12(A6), D1
	MOVE.L 8(A6), D2
	MOVE.L 4(A6),D3
	SUB.L D5,D1  	*i-t
	SUB.L D5,D2 	*j-t
	SUB.L #1,D3	*k-1

	MOVE.L D1,-(A6)
	MOVE.L D2,-(A6)
	MOVE.L D3,-(A6)
	MOVE.L D1,-(A6)
	BSR F
	ADDA.L #12,A6	*Pop 3 parameters off stack
	
	MOVE.L D4,-4(A6)
	ADD.L D4,D0
	Bra ForLoop
	rts
	
LastPartofElse:
	MOVE D4, D0		*return s and end function
	BRA EndofF

EndofF:

	move.l  0(A6), d0
	MOVEA.L A6,A7		*Delocate all local Variables
	MOVE.L (A7)+,A6		*Restore caller's frame pointer

*
* If you return NOW, your program will NOT pop the return address
* into the Program counter and it will CRASH !!!

* NOW the stack is:
*
* Offsets
*         +---------------+ <----- a7 (stack pointer)
*   8(a7) | return address|
*         +---------------+
*  12(a7) |      n  (10)  |
*         +---------------+
*  16(a7) |      A  (#A)  |
*         +---------------+
*
* NOW you can rexecute the return instruction !!!

	rts

*====================================================================
* Don't add anything below this line...
* ====================================================================
        end
