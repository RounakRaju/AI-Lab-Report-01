Student Name: Rounak Hasan Raju 
Student ID: 232002242 
Course: Artificial Intelligence Lab (CSE-316)
2D Maze Pathfinding using IDDFS
This repository contains a Python implementation of the Iterative Deepening Depth-First Search (IDDFS) algorithm to solve a 2D maze pathfinding problem. This project was completed as part of the Artificial Intelligence Lab (CSE-316) course at Green University of Bangladesh.
📘 Project Overview:
The primary goal of this experiment was to determine if a valid path exists between a given starting position and a target position within a 2D grid-based maze. 
1(Path): Represents a traversable cell where movement is allowed.
0 (Wall): Represents a blocked cell where movement is restricted.
The program utilizes IDDFS to ensure the search is both memory-efficient and complete, providing the depth level and the specific traversal order upon success.
Why IDDFS:
In Artificial Intelligence, search strategies are crucial. We used IDDFS because it combines the strengths of two fundamental algorithms: 
Memory Efficiency: Like DFS, it only stores the current path, avoiding the massive memory overhead of keeping all nodes in a queue.
Completeness: Like BFS, it guarantees finding a solution if one exists because it explores the grid level-by-level by gradually increasing the depth limit.
Optimal for Grids: It systematically explores state space without getting lost in infinite paths.
How the Algorithm Works:
The implementation follows a structured 8-step process to ensure accuracy :Grid Initialization:
User defines grid dimensions ($R \times C$) and enters values row-by-row.
Coordinate Input: User provides the Start $(r, c)$ and Target $(r, c)$ positions.
Iterative Scaling: A loop runs from depth $0$ up to a maximum of $R \times C$.
Depth-Limited Search (DLS): For each iteration, a recursive DLS is triggered to explore the maze up to the current limit.
Movement Logic: The algorithm attempts to move in four directions: Up, Down, Left, and Right.
Backtracking: If the goal isn't found within the limit, the algorithm "backtracks" by removing the node from the current path and visited set to explore other branches.
Output: If found, the program prints the path and depth; otherwise, it reports that no path exists within the limit .
Test Results:
Case 1 (Path Exists): The algorithm successfully identified the path at depth 5 for a 4x4 grid. 
Case 2 (No Path): The program correctly identified when the goal was unreachable within the maximum depth.
How to RunEnsure you have Python 3.x installed.
Run the script: lab_01.py
Enter grid size as you want for example( 4 4).
.Input the start and target coordinates.
