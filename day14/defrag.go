package main

import (
	"fmt"
	"strconv"
)

const size = 256
const blockSize = 16
const iterationAmount = 64

var suffix = []int{17, 31, 73, 47, 23}

// Converts the input string to ascii representation
// and appends the suffix.
func convertInput(input string) []int {
	byteArray := []byte(input)
	out := make([]int, 0)
	for _, b := range byteArray {
		out = append(out, int(b))
	}
	out = append(out, suffix...)
	return out
}

// Converts are [size]int array to a slice of sice
// size/blockSize where each entry represents each block's
// entries being XOR'd together
func denseHash(input [size]int) []int {
	out := make([]int, 0)
	for i := 0; i < size; i += blockSize {
		val := 0
		for j := i; j < i+blockSize; j++ {
			val ^= input[j]
		}
		out = append(out, val)
	}
	return out
}

// Converts int slice to the desired output format
// where each number between 0-255 are converted to
// hexadecimal and concatenated to a string.
// Zeros forced for each number.
func toKnotHexa(input []int) string {
	out := ""
	for _, v := range input {
		out += fmt.Sprintf("%02x", v)
	}
	return out
}

// Executes sparseHash on an array [0..255] with input as the seed.
// Repeated 'iterations' amount of times, with position and skipsize
// maintained between iterations.
func sparseHash(input []int, iterations int) [size]int {
	var out [size]int
	for i := 0; i < size; i++ {
		out[i] = i
	}

	currPos := 0
	skipSize := 0
	for it := 0; it < iterations; it++ {
		for _, length := range input {
			// reverse between currPos and to with wraparound
			to := currPos + length
			for i, j := currPos, to-1; i < j; i, j = i+1, j-1 {
				out[i%size], out[j%size] = out[j%size], out[i%size]
			}
			currPos += length + skipSize
			skipSize++
		}
	}
	return out
}

func knotHash(input string) string {
	in := convertInput(input)
	sparse := sparseHash(in, iterationAmount)
	dense := denseHash(sparse)
	return toKnotHexa(dense)
}

func generateKnotGrid(input string) [][]bool {
	grid := make([][]bool, 128)
	for i := 0; i < len(grid); i++ {
		grid[i] = make([]bool, 128)
	}

	for i := 0; i < 128; i++ {
		hash := knotHash(fmt.Sprintf("%s-%d", input, i))
		val1, _ := strconv.ParseUint(hash[:16], 16, 64)
		val2, _ := strconv.ParseUint(hash[16:], 16, 64)
		bits := fmt.Sprintf("%064b", val1) + fmt.Sprintf("%064b", val2)
		for j, bit := range bits {
			if bit == '1' {
				grid[i][j] = true
			}
		}
	}
	return grid
}

func main() {
	input := "ffayrhll"
	//input := "flqrgnkx"
	grid := generateKnotGrid(input)
	count := 0
	for _, row := range grid {
		for _, bit := range row {
			if bit {
				count++
			}
		}
	}
	fmt.Println(count)
}
