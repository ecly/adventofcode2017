#include <vector>
#include <iostream>

int walkthrough(std::vector<int> maze)
{
    int index = 0, moves = 0;
    while(index >= 0 && index < maze.size())
    {
        ++moves;
        index += maze[index]++;
    }
    return moves;
}

int walkthrough2(std::vector<int> maze)
{
    int index = 0, moves = 0;
    while(index >= 0 && index < maze.size())
    {
        ++moves;
        if (maze[index]<3) index += maze[index]++;
        else index += maze[index]--;
    }
    return moves;
}

int main() {
    std::vector<int> maze;
    int x;
    while (std::cin >> x)
        maze.push_back(x); 
    std::cout << "part1: " << walkthrough(maze) << std::endl;
    std::cout << "part2: " << walkthrough2(maze) << std::endl;
    return 0;
}
