score: list[int] = []
edges: list[list[int]] = []
chains: list[list[str]] = []


def get_longest_chain(size: int, words: list[str]) -> tuple[int, list[str]]:
    length = 0
    result_index = 0
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
        chains.append([])
        curr_lenth = get_length(i, i, words)
        if curr_lenth > length:
            length = curr_lenth
            result_index = i

    return length, chains[result_index]


def get_length(vertex: int, index, words: list[str]) -> int:
    if not chain_has_of_length(index, words[vertex].__len__()):
        chains[index].append(words[vertex])
    if score[vertex] > 0:
        return score[vertex]
    score[vertex] = 1
    for dest in edges[vertex]:
        score[vertex] = max(score[vertex], get_length(dest, index, words) + 1)
    return score[vertex]


def chain_has_of_length(index, len):
    for word in chains[index]:
        if word.__len__() == len:
            return True
    return False


def main():
    size = 0
    words: list[str] = []

    with open("Lab 4/wchain.in") as reader:
        size = int(reader.readline().replace('\n', ''))
        for word in reader:
            words.append(word.replace('\n', ''))

    print(f"Size: {size}")
    print(f"All words: {words}")
    length, chain = get_longest_chain(size, words)
    print(f"Chain: {chain}")
    print(f"Length: {length}")

    with open('Lab 4/wchain.out', "a") as writer:
        writer.write(str(length) + "\n")
    

if __name__ == "__main__":
    main()