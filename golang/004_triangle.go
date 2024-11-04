package main

/*
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle
*/

func OtherAngle(a int, b int) int {
	// your code here
	return 180 - a - b
}

func RunTests004() {
	Expect(OtherAngle(30, 60), 90)
	Expect(OtherAngle(10, 20), 150)
	Expect(OtherAngle(43, 78), 59)
}
