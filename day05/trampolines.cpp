#include <vector>
#include <iostream>
using namespace std;

int walkthrough(vector<int> maze)
{
    int index = 0;
    int moves = 0;
    while(index >= 0 && index < maze.size())
    {
        ++moves;
        index += maze[index]++;
    }
    return moves;
}

int walkthrough2(vector<int> maze)
{
    int index = 0;
    int moves = 0;
    while(index >= 0 && index < maze.size())
    {
        ++moves;
        if (maze[index]<3)
            index += maze[index]++;
        else
            index += maze[index]--;
    }
    return moves;
}

int main() {
    vector<int> maze;
    int x;
    while (cin >> x){
        maze.push_back(x); 
    }
    cout << "part1: " << walkthrough(maze) << endl;
    cout << "part2: " << walkthrough2(maze) << endl;
    return 0;
}
