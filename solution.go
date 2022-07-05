// // The end sequence N is 1, 683, 44287, etc.
// // The best-guess polynomial for row n of N is some (n - 1) order polynomial P, represented by
// // Pn = a1x(n - 1) + a2x(n - 2) + ... + a3x + a4 = 0

// This polynomial can be found by solving some n by n + 1 matrix.
// What is that matrix?

// When n = 1, N = 1, which is represented by
// [[1 | 1]]
// where the | denotes an augmented matrix.
// F(x) = 1, so the first BOP, F(2) = 1, is 1.
// A matrix is considered solved when it's in reduced echelon form, namely:
// in row n of the matrix, n is 1, and all other values besides those in the augmented matrix are 0
// Solving matrix for N1 (which is already done) gives the best-fit polynomial F, namely F(x) = 1.

// When n = 2, N = 1, 683. Since n is 2, we need an (n-1)-dimensional solution, aka a linear solution given by the system
// 1a + b = 1 => a + b = -1
// 2a + b = 683 => 2a + b = -683
// or
// [
// 	[1 1 | -1]
// 	[2 1 | -683]
// ]

// The algorithm to solve a matrix is as follows:
// beginning with cell (0, 0), multiply each value of the row by n s.t. the value of (0, 0) is 1.
// This is done, since the value of cell (0, 0) is already 1.
// Next, zero all the cells in (0, 0)'s column, aka column zero.
// To do so, find some multiple of row 0, which, when added to the row you're zeroing, makes that cell zero.
// In the case of the matrix above, the first cell to zero is (1, 0).
// Multiplying row 0 by -2 and adding it row 1 will give us 0 in (1, 0).
// Do so, and replace row 1 with the result:
// [
// 	[1 1 | -1]
// 	[0 -1 | -681]
// ]
// Column 0 is now complete.
// Repeat the algorithm for cell (1, 1).
// Multiply row one by -1
// [
// 	[1 1 | -1]
// 	[0 1 | 681]
// ]
// Then find a multiple of row 1 s.t. when it is added to row zero, cell (0, 1) becomes 0. That multiple is -1.
// Multiply row 1 by -1 and add it to row 0, in place
// [
// 	[1 0 | -682]
// 	[0 1 | 681]
// ]
// So a - 682 = 0, and b + 681 = 0.
// a = 682, b = -681.
// The next FIT is F(x) = 682x - 681.
// Note that F(1) = 1, and F(2) = 683.
// The next BOP is F(3) = 682 * 3 - 681 = 1365

// What will the next matrix be? N3 is 44287, so assuming P is an (n - 1)-order polynomial, we have:
// ax2 + bx + c = 1
// 4ax2 + 2bx + c = 683
// 9ax3 + 3bx + c = 44287
// Represented by
// [
// 	[1 1 1 | 1]
// 	[4 2 1 | 683]
// 	[9 3 1 | 44287]
// ]
// and in general, the ith row of the nth matrix is
// [
// 	[i^(n - 1) i^(n - 2) ... i^1 i^0 | Ni]
// ]
// where Ni is the ith integer in the sequence.

package main

import (
	"fmt"
	"math"
)

type Matrix struct {
	rows []Row
}

type Row struct {
	coefficients []int
}

func generatingFunction(n int) int {
	return 1 - n + int(math.Pow(float64(n), 2)) - int(math.Pow(float64(n), 3)) + int(math.Pow(float64(n), 4)) - int(math.Pow(float64(n), 5)) + int(math.Pow(float64(n), 6)) - int(math.Pow(float64(n), 7)) + int(math.Pow(float64(n), 8)) - int(math.Pow(float64(n), 9)) + int(math.Pow(float64(n), 10))
}

func matrixAt(size int) Matrix {
	matrix := Matrix{rows: make([]Row, size)}
	for i := range matrix.rows {
		coefficients := make([]int, size)
		for j := range coefficients {
			coefficients[j] = int(math.Pow(float64(i+1), float64(size-j-1)))
		}
		coefficients = append(coefficients, generatingFunction(i+1))
		matrix.rows[i] = Row{coefficients}
	}
	return matrix
}

func main() {
	fmt.Println(matrixAt(1))
	fmt.Println(matrixAt(2))
	fmt.Println(matrixAt(3))
}
