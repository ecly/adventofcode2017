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

type Graph = map[int][]int
type Visited = map[int]bool

func bfs(graph Graph, start int, visited Visited) (int, Visited) {
	queue := []int{start}
	count := 0
	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		if _, ok := visited[head]; !ok {
			visited[head] = true
			count++
			for _, v := range graph[head] {
				queue = append(queue, v)
			}
		}
	}
	return count, visited
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
	size, visited := bfs(graph, 0, Visited{})
	fmt.Println(size)

	count := 1
	for k := range graph {
		if _, ok := visited[k]; !ok {
			count++
			_, visited = bfs(graph, k, visited)
		}
	}
	fmt.Println(count)
}
