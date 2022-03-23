<h1 align="center">Conway Game of Life</h1>
<h3 align="center">Conway game of life program in python, processed with numpy and render with pygame</h3>


## Introduction to Conway Game of Life
The Game of Life, also known simple as Life, is a cellular automaton dvised by the British mathematician John Horton Conway in 1970. With it's rules as follow:



* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.



##Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Cody-Le/Conway-Game-Of-Life.git
   ```
2. Edit any Variable to your liking
   ```sh
   height, width = [30,30]
   The varaible that dictate the behavior of the games
   underPopRate = 2
   highPopRate = 3
   minimumSpawnRate = 3
   ```


2. run
   ```sh
   py main.py
