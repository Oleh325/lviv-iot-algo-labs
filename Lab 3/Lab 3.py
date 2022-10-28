class Graph:

    def __init__(self, graph: dict) -> None:
        self.graph: dict[int, set[int]] = {}
        self.all_paths: list[list[int]] = []
        for i in graph:
            for j in graph:
                if i != j:
                    self.graph.setdefault(i, set()).add(j)

    # Adds all available paths from start to end vertecies to all_paths
    def update_all_paths(self, start, end, visited: list[bool], path: list[int], max_length):
        
        visited[start - 1] = True
        path.append(start)

        if path.__len__() > max_length:
            path.pop()
            visited[start - 1] = False
            return
        if start == end:
            self.all_paths.append(list(path))
        for i in self.graph[start]:
            if not visited[i - 1]:
                self.update_all_paths(i, end, visited, path, max_length)

        path.pop()
        visited[start - 1] = False

    # Returns all paths from all vertrcies (ie all beer combinations in our case)
    def get_all_paths_from_element(self, element, max_length) -> list[list[int]]:
        self.all_paths = []
        visited = [False] * self.graph.__len__()
        path = []
        for i in self.graph.get(element):
            self.update_all_paths(element, i, visited, path, max_length)
        
        return self.all_paths


def beers_algorithm(n: int, b: int, graph: dict) -> int:
    beer_types = []
    lowest_amount = 50
    lowest_amount_types = []
    amount_of_beers = 0
    beer_graph = Graph(graph)
    combinations = beer_graph.get_all_paths_from_element(1, lowest_amount)

    i = 0
    for combination in combinations:
        amount_of_beers = 0
        satisfied_employees = set()
        for beer in combination:
            amount_of_beers += 1
            beer_types.append(beer)
            satisfied_employees.update(graph[beer])
            if satisfied_employees.__len__() == n:
                if lowest_amount > amount_of_beers:
                    lowest_amount = amount_of_beers
                    lowest_amount_types = list(beer_types)
                    break
        beer_types = []
        if combinations[i] == combinations[len(combinations) - 1] and (combination[0] + 1) in graph.keys():
            for combo in beer_graph.get_all_paths_from_element(combination[0] + 1, lowest_amount):
                combinations.append(combo)
        i += 1
                

    print(f"Types needed: {lowest_amount_types}")
    return lowest_amount

    
def main():
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

if __name__ == "__main__":
    main()