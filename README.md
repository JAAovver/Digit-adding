# Digit-adding
Add the digits of a number, and of the resulting number etc. until the sum is less than 10

The key here is just that a multiple of 9 will have it's digits add to 9. 

So if X is a multiple of 9, it's digits will add to 9. Then the digits of X+1 will add to 0, and X+2 to 1. So whatever the number is, its relation to a multiple of 9 determines the value of the final sum.

I used a list in the code (`numref`) instead of a dictionary because it was faster on the test cases.
