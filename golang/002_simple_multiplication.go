package main

/*
This kata is about multiplying a given number by eight
 if it is an even number and by nine otherwise.
*/

func SimpleMultiplication(n int) int {
	if n%2 == 0 {
		return n * 8
	}
	return n * 9
}

func RunTests002() {
	Expect(SimpleMultiplication(1), 9)
	Expect(SimpleMultiplication(3), 27)
	Expect(SimpleMultiplication(2), 16)
	Expect(SimpleMultiplication(4), 32)
}
