package main

import (
	"fmt"
	"math"
)

func term(n int) int {
	result := 0
	for i := 0; i < 11; i++ {
		sign := 1.0
		if i%2 != 0 {
			sign = -1.0
		}
		result += int(math.Pow(float64(n), float64(i)) * sign)
	}
	return result
}

func fit(coefficient int, sequence []int) string {
	solution := ""
	for i := 0; i < coefficient; i++ {
		solution += "(x - " + fmt.Sprint(sequence[i]) + ")"
	}
	return solution
}

func pe101() {
	sequence := make([]int, 0)
	for i := 0; i < 10; i++ {
		term := term(i + 1)
		sequence = append(sequence, term)
		fmt.Println(term)
	}
	fmt.Println(sequence)
	for i := 0; i < 10; i++ {
		fmt.Println(fit(i, sequence))
	}
}

func main() {
	pe101()
}
