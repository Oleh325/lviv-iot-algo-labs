from queue import Queue

class Node():

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Grid():

    def __init__(self, width, height):
        self.nodes = []
        self.width = width
        self.height = height
    
    def addNode(self, node: Node):
        self.nodes.append(node)

    def findNode(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None
    
    def paintNode(self, x, y, new_color):
        for node in self.nodes:
            if node.x == x and node.y == y:
                node.color = new_color

    def printGrid(self):
        i = 1
        for node in self.nodes:
            print(node.color + " ", end="")
            if i == self.width:
                print()
                i = 0
            i += 1

    def getAllNodes(self):
        return self.nodes


def floodFill(grid: Grid, node: Node, new_color):
    target_color = node.color
    if new_color == target_color:
        return
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        currentNode = queue.get()
        if currentNode != None:
            if  currentNode.color != target_color:
                continue
            else:
                grid.paintNode(currentNode.x, currentNode.y, new_color)
                queue.put(grid.findNode(currentNode.x + 1, currentNode.y))
                queue.put(grid.findNode(currentNode.x - 1, currentNode.y))
                queue.put(grid.findNode(currentNode.x, currentNode.y + 1))
                queue.put(grid.findNode(currentNode.x, currentNode.y - 1))


def main():
    width = 0
    height = 0
    x = 0
    y = 0
    new_color = ''

    with open('Lab 2/input.txt') as reader:
        size = reader.readline().split(",")
        width = int(size[0])
        height = int(size[1])
        grid = [['W' for x in range(width)] for y in range(height)]
        coordinates = reader.readline().split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])
        new_color = reader.readline().replace("'", "").replace("\n", "")
        content = reader.readline()
        i = 0
        while content:
            j = 0
            for element in content.replace("[", "").replace("]", "").replace(",", "").split('\'')[1::2]:
                grid[i][j] = element
                j += 1
            content = reader.readline()
            i += 1

    gridOfNodes = Grid(width, height)
    print(f"\nCanvas size: {width} x {height}")
    print(f"Coordinates of the fill tool target: x = {x}, y = {y}")
    print(f"New color: {new_color}")
    print("Before fill: ")
    i = 0
    for row in grid:
        j = 0
        for element in row:
            node = Node(i, j, element)
            gridOfNodes.addNode(node)
            j += 1
        i += 1

    gridOfNodes.printGrid()

    node = gridOfNodes.findNode(x, y)
    floodFill(gridOfNodes, node, new_color)

    print("\nAfter fill: ")
    gridOfNodes.printGrid()

    i = 0
    for row in grid:
        j = 0
        for element in row:
            grid[i][j] = gridOfNodes.findNode(i, j).color
            j += 1
        i += 1


    with open('Lab 2/output.txt', "a") as writer:
        content = ""
        for row in grid:
            content += "["
            for element in row:
                content += "'" + element + "', "
            content = content[:-2]
            content += "],\n"
        content = content[:-2]

        writer.write(content)


if __name__ == "__main__":
    main()