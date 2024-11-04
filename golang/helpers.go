package main

import (
	"fmt"
	"reflect"
)

func Expect(value interface{}, expectedValue interface{}) {
	fmt.Printf("tc: %v\n", reflect.DeepEqual(value, expectedValue))
}
