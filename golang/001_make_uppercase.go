package main

import "strings"

func MakeUpperCase(str string) string {
	return strings.ToUpper(str)
}

func RunTests001() {
	Expect(MakeUpperCase("hello"), "HELLO")
}
