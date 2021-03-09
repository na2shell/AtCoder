from copy import deepcopy


def solve(maze, i, j, h, w, count):
    distance = 0
    if maze[i][j] == ".":
        distance = 0
        next_search = [(i, j)]
        while not next_search == []:
            now = next_search.pop(0)
            if maze[now[0]][now[1]] == ".":
                maze[now[0]][now[1]] = "#"
                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    search = [direction[0] + now[0], direction[1] + now[1]]
                    if search[0] < 0 or h <= search[0] or search[1] < 0 or w <= search[1] or \
                            maze[search[0]][search[1]] == "#":
                        continue
                    else:
                        count[search[0]][search[1]] = count[now[0]][now[1]] + 1
                        next_search.append(tuple(search))
                        distance = max(distance, count[search[0]][search[1]])
    return distance


def main():
    height, width = map(int, input().split(" "))
    maze = []
    answer = 0
    for _ in range(height):
        maze.append(list(input()))
    count = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            answer = max(answer, solve(deepcopy(maze), i, j, height, width, deepcopy(count)))
    print(answer)


if __name__ == '__main__':
    main()

