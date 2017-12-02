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
	fmt.Println(readAndSolve(os.Stdin, maxDiff))
}
