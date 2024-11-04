package main

/*
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
*/

func ReverseSeq(n int) []int {
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		numbers[i] = n - i
	}
	return numbers
}

func RunTests003() {
	Expect(ReverseSeq(5), []int{5, 4, 3, 2, 1})
}
