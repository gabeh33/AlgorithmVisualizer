from graphics import *
import math
import heapq

# The starting window to specify the dimensions, square size, and algorithm used
startingWindow = GraphWin('Path Finding Visualizer', 400, 400)


def make_starting_window():
    # Displays the headers
    startingWindow.setBackground('yellow')
    header = Text(Point(startingWindow.getWidth() / 2, 25), 'Path Finding Visualizer')
    subheader = Text(Point(startingWindow.getWidth() / 2, 58), 'By: Gabe Holmes')
    header.setSize(35)
    subheader.setSize(28)
    header.setFill('red')
    header.setStyle('bold')
    header.draw(startingWindow)
    subheader.draw(startingWindow)

    # Width entry box
    widthPrompt = Text(Point(150, 170), 'Enter the width you would like for the board:\n Default is 40')
    widthPrompt.setSize(13)
    widthPrompt.draw(startingWindow)

    widthEntry = Entry(Point(315, 170), 5)
    widthEntry.draw(startingWindow)

    # Height entry box
    heightPrompt = Text(Point(150, 220), 'Enter the height you would like for the board: \n Default is 40')
    heightPrompt.setSize(13)
    heightPrompt.draw(startingWindow)

    heightEntry = Entry(Point(315, 220), 5)
    heightEntry.draw(startingWindow)

    # Size of square entry box
    square = Text(Point(150, 270), 'Enter the size of each square (in pixels): \n Default is 15')
    square.setSize(13)
    square.draw(startingWindow)

    squareEntry = Entry(Point(315, 270), 5)
    squareEntry.draw(startingWindow)

    # Create rectangles for the different algorithms
    dfsRec = Rectangle(Point(10, 340), Point(90, 380))
    dfsRec.setFill('orange')
    dfsRec.draw(startingWindow)

    dfsText = Text(Point(50, 360), 'DFS')
    dfsText.setSize(27)
    dfsText.draw(startingWindow)

    # BFS rectangle
    bfsRec = Rectangle(Point(110, 340), Point(190, 380))
    bfsRec.setFill('orange')
    bfsRec.draw(startingWindow)

    bfsText = Text(Point(150, 360), 'BFS')
    bfsText.setSize(27)
    bfsText.draw(startingWindow)

    # A* rectangle
    asRec = Rectangle(Point(210, 340), Point(290, 380))
    asRec.setFill('orange')
    asRec.draw(startingWindow)

    asText = Text(Point(250, 360), 'A*')
    asText.setSize(27)
    asText.draw(startingWindow)

    # Starting rectangle
    startingRec = Rectangle(Point(310, 340), Point(390, 380))
    startingRec.setFill('green')
    startingRec.draw(startingWindow)

    startingText = Text(Point(350, 360), 'Start!')
    startingText.setSize(27)
    startingText.draw(startingWindow)
    alg_selected = None
    warning = Text(Point(startingWindow.getWidth() / 2, 90), 'Please select an algorithm to use!')
    while True:
        pt = startingWindow.getMouse()
        if 340 <= pt.y <= 380:
            if 10 <= pt.x <= 90:
                alg_selected = "dfs"
                dfsRec.setFill('gray')
                bfsRec.setFill('orange')
                asRec.setFill('orange')
                warning.undraw()
            elif 110 <= pt.x <= 190:
                alg_selected = "bfs"
                dfsRec.setFill('orange')
                bfsRec.setFill('gray')
                asRec.setFill('orange')
                warning.undraw()
            elif 210 <= pt.x <= 290:
                alg_selected = "astar"
                dfsRec.setFill('orange')
                bfsRec.setFill('orange')
                asRec.setFill('gray')
                warning.undraw()
            elif 310 <= pt.x <= 390:
                try:
                    width_squares = int(widthEntry.getText())
                except ValueError:
                    width_squares = 40
                try:
                    height_squares = int(heightEntry.getText())
                except ValueError:
                    height_squares = 40
                try:
                    square_len = int(squareEntry.getText())
                except ValueError:
                    square_len = 15
                if alg_selected is None:
                    warning.draw(startingWindow)
                    continue
                startingWindow.close()
                return width_squares, height_squares, square_len, alg_selected


# Constants
w, h, l, alg_sel = make_starting_window()

num_square_width = w  # Width of board in squares, default 40
num_square_height = h  # # Height of board in squares, default 40
square_length = l  # Length of one side of a square in pixels, default 15

text_label_height = 20  # Height of the text label at the top

width = num_square_width * square_length  # Width of region of the window with the squares
height = (num_square_height * square_length) + text_label_height * 2  # Height of the region with the squares

squares = [x[:] for x in [[(Rectangle(Point(0, 0), Point(0, 0)), False)] * num_square_width] * num_square_height]

win = GraphWin('Searching Visualizer', width, height)  # The window that will hold everything

# Handling the text label
message = Text(Point(win.getWidth() / 2, text_label_height), 'Creating Board')
message.setTextColor('blue')
message.setStyle('italic')
message.setSize(20)
message.draw(win)

# Drawing a line under the label
label_line = Line(Point(0, text_label_height * 2), Point(width, text_label_height * 2))
label_line.draw(win)

# Draw the vertical lines
starting_y = text_label_height * 2

# Create the squares that act as nodes
for i in range(num_square_height):
    for j in range(num_square_width):
        shape = Rectangle(Point(j * square_length, i * square_length + starting_y),
                          Point((j + 1) * square_length, (i + 1) * square_length + starting_y))
        squares[i][j] = (shape, False)

# Draw the vertical lines
for i in range(num_square_width + 1):
    if i == num_square_width:
        line = Line(Point(width - 1, starting_y), Point(width - 1, height))
        line.draw(win)
        break
    line = Line(Point(i * square_length, starting_y), Point(i * square_length, height))
    line.draw(win)

# Draw the horizontal lines, which give the illusion of drawing squares but is faster
for i in range(num_square_height + 1):
    line = Line(Point(0, (i * square_length) + starting_y), Point(width, (i * square_length) + starting_y))
    line.draw(win)


def get_row_col_chosen(point: Point):
    row = math.floor((point.y - starting_y) / square_length)
    col = math.floor(point.x / square_length)
    return row, col


# Update the message as the board has been drawn
message.setText('Pick a starting node')

# Get the starting node that the user picks
starting = win.getMouse()
startingRow, startingCol = get_row_col_chosen(starting)
square, isWall = squares[startingRow][startingCol]
square.setFill('green')
square.draw(win)

message.setText('Pick a ending node')

# Get the ending node that the user picks
ending = win.getMouse()
endingRow, endingCol = get_row_col_chosen(ending)

# Check to make sure the ending node is different
while endingRow == startingRow and endingCol == startingCol:
    message.setText("Please choose a different ending node than starting node")
    ending = win.getMouse()
    endingRow, endingCol = get_row_col_chosen(ending)
square, isWall = squares[endingRow][endingCol]
square.setFill('red')
square.draw(win)

# Now the user should choose between dfs bfs or astar

# Now allow the user to place walls that the path must go around
message.setText("Place as many walls as you would like, then press the green node to start")
wall_count = 0
while True:
    point = win.getMouse()
    row, col = get_row_col_chosen(point)
    if row == startingRow and col == startingCol:
        break
    square, isWall = squares[row][col]
    if not (row == endingRow and col == endingCol) and not isWall:
        square.setFill('orange')
        squares[row][col] = (square, True)
        square.draw(win)
    wall_count += 1


def check_for_edge(curr_row, curr_col, visited, worklist):
    if 0 <= curr_row < num_square_height and 0 <= curr_col < num_square_width \
            and (curr_row, curr_col) not in visited and (curr_row, curr_col) not in worklist:
        currShape, isWall = squares[curr_row][curr_col]
        return not isWall
    return False


# True for dfs, False for bfs
def dfs_bfs(dfs):
    if dfs:
        message.setText('Searching using DFS')
    else:
        message.setText('Searching using BFS')
    # A node in this grid is a (row, col)
    worklist = []  # A stack to represent the nodes to explore
    visited = []  # List of nodes that have been explored
    correct_path = {}

    worklist.append((startingRow, startingCol))
    correct_path[(startingRow, startingCol)] = None
    visited.append((startingRow, startingCol))

    while len(worklist) > 0:
        currRow, currCol = worklist.pop()
        visited.append((currRow, currCol))
        if currRow == endingRow and currCol == endingCol:
            if dfs:
                message.setText('Found a path using Depth First Search!')
            else:
                message.setText('Found a path using Breadth First Search!')
            return correct_path

        square, isWall = squares[currRow][currCol]
        if not (currRow == startingRow and currCol == startingCol):
            square.setFill('blue')
            square.draw(win)

        # Start with the top left of the current node, and work clockwise
        # This checks if there is an edge to the next possible node, and if that node
        # is not a wall
        for i in range(-1, 2):
            if check_for_edge(currRow - 1, currCol + i, visited, worklist):
                if dfs:
                    worklist.append((currRow - 1, currCol + i))
                else:
                    worklist.insert(0, (currRow - 1, currCol + i))
                correct_path[(currRow - 1, currCol + i)] = (currRow, currCol)

        if check_for_edge(currRow, currCol + 1, visited, worklist):
            if dfs:
                worklist.append((currRow, currCol + 1))
            else:
                worklist.insert(0, (currRow, currCol + 1))
            correct_path[(currRow, currCol + 1)] = (currRow, currCol)

        for i in range(-1, 2):
            if check_for_edge(currRow + 1, currCol + i, visited, worklist):
                if dfs:
                    worklist.append((currRow + 1, currCol + i))
                else:
                    worklist.insert(0, (currRow + 1, currCol + i))
                correct_path[(currRow + 1, currCol + i)] = (currRow, currCol)

        if check_for_edge(currRow, currCol - 1, visited, worklist):
            if dfs:
                worklist.append((currRow, currCol - 1))
            else:
                worklist.insert(0, (currRow, currCol - i))
            correct_path[(currRow, currCol - 1)] = (currRow, currCol)
    message.setText('No path from the starting node to the ending node')
    return None


def astar():
    # heap to store a tuple of (distance to ending node, (row, col))
    heap = []
    visited = []
    correctPath = {}
    pure_worklist = []  # used to keep track of just the tuples in heap

    heap.append((getDistance(startingRow, startingCol), (startingRow, startingCol)))
    pure_worklist.append((startingRow, startingCol))
    correctPath[(startingRow, startingCol)] = None
    visited.append((startingRow, startingCol))

    heapq.heapify(heap)

    while len(heap) > 0:
        dist, (currRow, currCol) = heapq.heappop(heap)
        currRow, currCol = (currRow, currCol)
        visited.append((currRow, currCol))

        if currRow == endingRow and currCol == endingCol:
            message.setText('Found a path using A*')
            return correctPath

        square, isWall = squares[currRow][currCol]
        if not (currRow == startingRow and currCol == startingCol):
            square.setFill('blue')
            square.draw(win)

        # Top 3
        for i in range(-1, 2):
            if check_for_edge(currRow - 1, currCol + i, visited, pure_worklist):
                heapq.heappush(heap, (getDistance(currRow - 1, currCol + i), (currRow - 1, currCol + i)))
                pure_worklist.append((currRow - 1, currCol + i))
                correctPath[(currRow - 1, currCol + i)] = (currRow, currCol)

        # Right 1
        if check_for_edge(currRow, currCol + 1, visited, pure_worklist):
            heapq.heappush(heap, (getDistance(currRow, currCol + 1), (currRow, currCol + 1)))
            pure_worklist.append((currRow, currCol + 1))
            correctPath[(currRow, currCol + 1)] = (currRow, currCol)
        # Left 1
        if check_for_edge(currRow, currCol - 1, visited, pure_worklist):
            heapq.heappush(heap, (getDistance(currRow, currCol - 1), (currRow, currCol - 1)))
            pure_worklist.append((currRow, currCol - 1))
            correctPath[(currRow, currCol - 1)] = (currRow, currCol)

        # Bottom 3
        for i in range(-1, 2):
            if check_for_edge(currRow + 1, currCol + i, visited, pure_worklist):
                heapq.heappush(heap, (getDistance(currRow + 1, currCol + i), (currRow + 1, currCol + i)))
                pure_worklist.append((currRow + 1, currCol + i))
                correctPath[(currRow + 1, currCol + i)] = (currRow, currCol)


def getDistance(row, col):
    aSq = (row - endingRow) ** 2
    bSq = (col - endingCol) ** 2
    return math.sqrt(aSq + bSq)


if alg_sel == 'dfs':
    path = dfs_bfs(True)
elif alg_sel == 'bfs':
    path = dfs_bfs(False)
elif alg_sel == 'astar':
    path = astar()

if path:
    row_col = path[(endingRow, endingCol)]
    while row_col:
        row, col = row_col
        square, isWall = squares[row][col]
        square.setFill('yellow') if path[(row, col)] else None
        row_col = path[(row, col)]

win.getMouse()
