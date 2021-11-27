# Searching Algorithm Visualizer

This program serves as an interactive way to demonstrate how the most common searching algorithms work.

## Description

This is a project that provides a way to see how three different searching algorithms work - depth first search, breadth first search, and A*. 
The graph is represented as a NxM grid of squares, with a starting node and ending node chosen by the user. The user is then able to add walls - nodes that the 
algorithms are not allowed to explore - either manually, generated randomly, or both. Once the walls are placed the algorithm that the user chose will run, and
be shown on screen. Explored nodes are colored blue, so it is clear how the alorithm attempts to find the ending node. If there is no possible path from the 
starting node to the ending node, then the algorithm will indicate so and stop. If there is a path, once the algorithm has found the ending node the (not 
necessarily optimal) path that the algorithm took to find the ending node will be colored yellow. This way it is clear what nodes were explored, and the path
that the alogirthm returned. 

## Getting Started

### Dependencies

* Must have graphics.py file in the same folder as the source code


### Executing program

* To get started, download the source code or clone the repository
* The file to execute within the folders is AlgorithmVisualizer.py
* Make the file AlgorithmVisualizer executable, make sure graphics.py is in the same folder, and then type
```
./bin/python AlgorithmVisualizer.py
```

## Help

Generating the walls randomly on a very large board can take some time. Viewing the program while the walls are being generated can make it 
take much longer. I believe this has something to do how graphics.py renders objects. In order to speed up this process significantly, 
view something else and let the program run in the background. As long as you are not looking directly at the program, the walls will render 
faster. This is also true with the board itself, however the board takes much less time.

## Authors


Gabe Holmes <br/>
Cybersecurity student at Northeastern University <br/>
holmes.ga@northeastern.edu <br/>
https://www.linkedin.com/in/gabe-holmes/ <br/>

## Version History


* 0.1
    * Initial Release


