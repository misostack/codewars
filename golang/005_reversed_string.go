package main

/*
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
*/

func Solution(word string) string {
	reversed := ""
	for _, c := range word {
		reversed = string(c) + reversed
	}
	return reversed
	// chars := make([]rune, len(word))
	// for index, c := range word {
	// 	chars[len(word)-index-1] = c
	// }
	// return string(chars)
}

func RunTests005() {
	Expect(Solution("world"), "dlrow")
}
