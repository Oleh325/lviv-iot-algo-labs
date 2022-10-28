class Graph:

    def __init__(self, graph: dict) -> None:
        self.graph: dict[int, set[int]] = {}
        self.all_paths: list[list[int]] = []
        for i in graph:
            for j in graph:
                if i != j:
                    self.graph.setdefault(i, set()).add(j)

    def update_all_paths(self, from_vertex, to_vertex, visited: list[bool], path: list[int]):
        
        visited[from_vertex - 1] = True
        path.append(from_vertex)

        if from_vertex == to_vertex:
            self.all_paths.append(list(path))
        for i in self.graph[from_vertex]:
            if not visited[i - 1]:
                self.update_all_paths(i, to_vertex, visited, path)

        path.pop()
        visited[from_vertex - 1] = False

    def get_all_paths(self) -> list[list[int]]:
        
        for i in self.graph:
            visited = [False] * self.graph.__len__()
            path = []
            for j in self.graph:
                if i != j:
                    self.update_all_paths(i, j, visited, path)
        
        return self.all_paths


def beers_algorithm(n: int, b: int, graph: dict) -> int:
    beer_types = []
    lowest_amount = 0
    lowest_amount_types = []
    amount_of_beers = 0
    combinations = Graph(graph).get_all_paths()

    i = 0
    for combination in combinations:
        amount_of_beers = 0
        satisfied_employees = set()
        for beer in combination:
            amount_of_beers += 1
            beer_types.append(beer)
            satisfied_employees.update(graph[beer])
            if satisfied_employees.__len__() == n:
                if lowest_amount == 0 or lowest_amount > amount_of_beers:
                    lowest_amount = amount_of_beers
                    lowest_amount_types = list(beer_types)
                    break
        beer_types = []
        i += 1
                

    print(f"Types needed: {lowest_amount_types}")
    return lowest_amount

    

employees = 0
beers = 0
compatibilityArray = []
minAmount = 0

with open("Lab 3/input.txt") as reader:
    employees, beers = reader.readline().split(" ")
    employees = int(employees)
    beers = int(beers)
    for entry in reader.readline().split(" "):
        compatibilityArray.append(entry)

print(f"Amount of employees: {employees}")
print(f"Amount of beers: {beers}\n\n")
graph: dict[int, set[int]] = {}
i = 1
for entry in compatibilityArray:
    j = 1
    print(f'Employee №{i}:')
    output = ""
    for isCompatible in entry:
        graph.setdefault(j, set())
        if isCompatible == "Y":
            graph[j].add(i)
        output += f'{"likes" if isCompatible == "Y" else "dislikes"} beer №{j}, '
        j += 1
    output = output[:-2]
    print(f"{output}\n")
    i += 1

minAmount = beers_algorithm(employees, beers, graph)

print(f"Minimum amount of beer types that should be bought: {minAmount}")