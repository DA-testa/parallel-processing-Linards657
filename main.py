# python3

def parallel_processing(n, m, data):
    output = []
    check = []
    jobs = []
    for i in range(n):
        check.append(False)
        jobs.append([0, 0])
    # TODO: write the function for simulating parallel tasks,
    # create the output pairs

    while len(data) > 0:
        for i, value in enumerate(check):
            if not value:
                output.append((i, jobs[i][1]))
                check[i] = True
                jobs[i][0] = data.pop(0)
                jobs[i][1] = jobs[i][1] + jobs[i][0]
            else:
                if jobs[i][0] == 0:
                    check[i] = False
                else:
                    jobs[i][0] = jobs[i][0] - 1
    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    text = list(map(int, input().split()))
    # n - thread count
    # m - job count
    n = text[0]
    m = text[1]

    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)

    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
