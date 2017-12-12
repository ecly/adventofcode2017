package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// Graph ...
type Graph = map[int][]int

func bfsCountReachable(graph Graph, start int) int {
	queue := []int{start}
	visisted := make(map[int]bool)
	count := 0
	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		if _, ok := visisted[head]; !ok {
			visisted[head] = true
			count++
			for _, v := range graph[head] {
				queue = append(queue, v)
			}
		}
	}
	return count
}

func readGraph(reader io.Reader) Graph {
	graph := make(Graph)
	scanner := bufio.NewScanner(reader)
	re := regexp.MustCompile("[0-9]+")
	for scanner.Scan() {
		split := strings.Fields(scanner.Text())
		from, _ := strconv.Atoi(split[0])
		neighbours := make([]int, 0)
		for _, v := range split[2:] {
			trimmed := re.FindString(v)
			to, _ := strconv.Atoi(trimmed)
			neighbours = append(neighbours, to)
		}
		graph[from] = neighbours
	}
	return graph
}

func main() {
	graph := readGraph(os.Stdin)
	fmt.Printf("first half: %v\n", bfsCountReachable(graph, 0))
}
