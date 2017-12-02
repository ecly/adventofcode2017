package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

type rowFunc func([]int) int

const inf = 1 << 30

// Calculate largest difference between ints in array
func maxDiff(row []int) int {
	max := -inf
	min := inf
	for _, v := range row {
		if v > max {
			max = v
		}
		if v < min {
			min = v
		}
	}
	return max - min
}

// Calculate the result of dividing the first two evenly divisible numbers in the row
func firstEvenlyDivisible(row []int) int {
	for i := 0; i < len(row); i++ {
		vali := row[i]
		for j := i + 1; j < len(row); j++ {
			high := row[j]
			low := vali
			if high < low {
				high, low = low, high
			}
			if high%low == 0 {
				return high / low
			}
		}
	}
	return -1
}

func readAndSolve(reader io.Reader, rf rowFunc) int {
	sum := 0
	scanner := bufio.NewScanner(reader)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		row := make([]int, len(fields))
		for i := 0; i < len(fields); i++ {
			row[i], _ = strconv.Atoi(fields[i])
		}
		sum += rf(row)
	}
	return sum
}

func main() {
	//fmt.Println("first half: ", readAndSolve(os.Stdin, maxDiff))
	fmt.Println("second half: ", readAndSolve(os.Stdin, firstEvenlyDivisible))
}
