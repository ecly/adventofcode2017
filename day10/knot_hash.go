package main

import (
	"fmt"
)

const size = 256

func solve(input []int) []int {
	out := make([]int, size)
	for i := 0; i < len(out); i++ {
		out[i] = i
	}
	currPos := 0
	skipSize := 0
	for _, length := range input {
		// reverse between currPos and to with wraparound
		to := currPos + length
		for i, j := currPos, to-1; i < j; i, j = i+1, j-1 {
			out[i%size], out[j%size] = out[j%size], out[i%size]
		}
		currPos += length + skipSize
		skipSize++
	}
	return out
}

func main() {
	input := []int{102, 255, 99, 252, 200, 24, 219, 57, 103, 2, 226, 254, 1, 0, 69, 216}
	output := solve(input)
	fmt.Printf("%v\n", output[0]*output[1])
}
