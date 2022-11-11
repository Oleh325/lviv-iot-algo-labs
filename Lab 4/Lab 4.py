score: list[int] = []
edges: list[list[int]] = []
chain: list[str] = []

def get_longest_chain(size: int, words: list[str]) -> int:
    length = 0
    position: dict[str, int] = {}

    i = 0
    for word in words:
        position[word] = i
        edges.append([])
        score.append(0)
        i += 1

    i = 0
    for word in words:
        for j in range(word.__len__()):
            prev = position.get(words[i][:j] + words[i][j + 1:])
            if prev is not None:
                edges[i].append(prev)
        i += 1

    for i in range(size):
        length = max(length, get_length(i))

    return length

def get_length(vertex: int) -> int:
    if score[vertex] > 0:
        return score[vertex]
    score[vertex] = 1
    for dest in edges[vertex]:
        score[vertex] = max(score[vertex], get_length(dest) + 1)
    return score[vertex]

def main():
    size = 0
    words: list[str] = []

    with open("Lab 4/wchain.in") as reader:
        size = int(reader.readline().replace('\n', ''))
        for word in reader:
            words.append(word.replace('\n', ''))

    print(f"Size: {size}")
    print(f"All words: {words}")
    length = get_longest_chain(size, words)
    print(f"Length: {length}")

    with open('Lab 4/wchain.out', "a") as writer:
        writer.write(str(length) + "\n")
    

if __name__ == "__main__":
    main()